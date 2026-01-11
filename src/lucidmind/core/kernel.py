import numpy as np
from typing import List, Dict, Any, Optional
from .rule import Rule, choose_weighted
from .state import complexity, entropy

class Kernel:
    """
    LucidMind Core Kernel Dynamics.
    
    This class implements the self-organizing dynamics of the state space
    using rule-based evolution, birth/death cycles, and soft gating.
    
    This logic is FROZEN during the Research Phase.
    
    See: docs/math_core.md#4-transition-operator
    """
    def __init__(self, config: Dict[str, Any], rng: Optional[np.random.Generator] = None):
        self.config = config
        self.rng = rng if rng is not None else np.random.default_rng()
        
        self.N = config.get('N', 32)
        self.tau = config.get('tau', 0.2)
        self.noise_sigma = config.get('noise_sigma', 0.03)
        self.alpha = config.get('alpha', 0.05)
        self.beta = config.get('beta', 0.03)
        self.death_threshold = config.get('death_threshold', -0.5)
        self.birth_window = config.get('birth_window', 25)
        self.bad_steps_to_birth = config.get('bad_steps_to_birth', 15)
        self.k_delta = config.get('k_delta', 0.05)
        self.gate_k = config.get('gate_k', 3.0)
        self.gate_T = config.get('gate_T', 0.8)
        
        self.S = self.rng.normal(0, 0.1, size=self.N)
        self.rules: List[Rule] = []
        self.memory: List[np.ndarray] = []
        
        # Statistics & Lifecycle Tracking
        self.t = 0
        self.rule_counter = 0
        self.born_total = 0
        self.died_total = 0
        self.rule_lifecycles = {} # uid -> dict

    def synthesize_rule_from_memory(self, memory_slice: List[np.ndarray]) -> Rule:
        """Creates a new rule based on recent state history."""
        M = np.stack(memory_slice, axis=0)
        S_bar = np.mean(M, axis=0)

        norm = np.linalg.norm(S_bar) + 1e-9
        w = S_bar / norm
        b = 0.0

        delta = np.zeros_like(S_bar)
        active = np.abs(S_bar) > self.tau
        delta[active] = -self.k_delta * np.sign(S_bar[active])

        uid = f"rule_{self.rule_counter}"
        self.rule_counter += 1
        return Rule(w=w, b=b, delta=delta, strength=0.0, uid=uid)

    def step(self) -> Dict[str, Any]:
        """Performs a single simulation step."""
        self.t += 1
        # 1) Soft gating
        candidates = []
        for r in self.rules:
            # Update peak strength tracking
            if r.uid in self.rule_lifecycles:
                self.rule_lifecycles[r.uid]['peak_strength'] = max(
                    self.rule_lifecycles[r.uid]['peak_strength'], 
                    r.strength
                )
                
            p = r.gate_prob(self.S, self.gate_k)
            if self.rng.random() < p:
                candidates.append(r)

        applied_rule = None
        gain = 0
        
        if not candidates:
            # Only noise and accumulation
            self.S = self.S + self.rng.normal(0, self.noise_sigma, size=self.N)
            self.memory.append(self.S.copy())
        else:
            # 2) Choose rule
            applied_rule = choose_weighted(candidates, self.gate_T, rng=self.rng)

            # 3) Apply + noise
            S_old_comp = complexity(self.S, self.tau)
            S_new = applied_rule.apply(self.S) + self.rng.normal(0, self.noise_sigma, size=self.N)
            S_new_comp = complexity(S_new, self.tau)

            # 4) Evaluate gain
            gain = S_old_comp - S_new_comp

            # 5) Update strength
            if gain > 0:
                applied_rule.strength += self.alpha * gain
            else:
                applied_rule.strength -= self.beta * abs(gain)

            # 6) Death check
            if applied_rule.strength < self.death_threshold:
                self.rules.remove(applied_rule)
                self.died_total += 1
                if applied_rule.uid in self.rule_lifecycles:
                    self.rule_lifecycles[applied_rule.uid]['death_t'] = self.t

            # 7) Update state
            self.S = S_new
            self.memory.append(self.S.copy())

        # 9) Rule birth
        if len(self.memory) >= self.birth_window:
            recent = self.memory[-self.birth_window:]
            recent_comp = [complexity(x, self.tau) for x in recent]
            
            median_comp = np.median(recent_comp)
            bad = sum(1 for c in recent_comp if c >= median_comp)

            if bad >= self.bad_steps_to_birth:
                new_rule = self.synthesize_rule_from_memory(recent)
                self.rules.append(new_rule)
                self.born_total += 1
                self.rule_lifecycles[new_rule.uid] = {
                    'birth_t': self.t,
                    'death_t': None,
                    'peak_strength': 0.0
                }
                self.memory.clear()

        return {
            'step': self.t,
            'state': self.S.copy(),
            'complexity': complexity(self.S, self.tau),
            'entropy': entropy(self.S),
            'n_rules': len(self.rules),
            'applied_rule': applied_rule,
            'gain': gain,
            'born': self.born_total,
            'died': self.died_total
        }

    def get_stats(self) -> Dict[str, Any]:
        """Returns statistics of the kernel."""
        born = self.born_total
        died = self.died_total
        damping = died / born if born > 0 else 0.0
        
        return {
            'born_total': born,
            'died_total': died,
            'alive_count': len(self.rules),
            'damping_ratio': damping,
            'rule_lifecycles': self.rule_lifecycles
        }
