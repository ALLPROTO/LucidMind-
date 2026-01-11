import numpy as np
from typing import List, Optional

class Rule:
    """
    Represents a deterministic transformation rule in the LucidMind state space.
    
    A rule consists of a gating condition (w, b) and a state delta (delta).
    The gating probability determines if the rule is applied based on the current state.
    
    See: docs/math_core.md#4-transition-operator
    """
    def __init__(self, w: np.ndarray, b: float, delta: np.ndarray, strength: float = 0.0, uid: str = ""):
        self.w = np.array(w, dtype=float)
        self.b = float(b)
        self.delta = np.array(delta, dtype=float)
        self.strength = float(strength)
        self.uid = uid

    def gate_prob(self, S: np.ndarray, k: float = 3.0) -> float:
        """
        Calculates the probability of applying this rule given current state S.
        
        Args:
            S: Current state vector
            k: Sigmoid steepness (gate_k)
            
        Returns:
            Probability value in [0, 1]
        """
        # probability of "passing" the rule (soft gating)
        g = float(np.dot(self.w, S) + self.b)
        return float(1.0 / (1.0 + np.exp(-k * g)))

    def apply(self, S: np.ndarray) -> np.ndarray:
        """Applies the rule's delta to state S."""
        return S + self.delta

def choose_weighted(rules: List[Rule], T: float = 0.8, rng: Optional[np.random.Generator] = None) -> Rule:
    """
    Selects a rule based on their strengths using softmax with temperature T.
    
    Args:
        rules: List of candidate rules
        T: Softmax temperature (lower = more deterministic towards strong rules)
        rng: Random number generator
        
    Returns:
        The selected Rule instance
    """
    def softmax(x):
        x = np.array(x, dtype=float)
        x = x - np.max(x)
        ex = np.exp(x)
        s = np.sum(ex)
        return ex / s if s > 0 else np.ones_like(ex) / len(ex)

    strengths = np.array([r.strength for r in rules], dtype=float)
    weights = softmax(strengths / max(T, 1e-6))
    
    if rng is not None:
        idx = rng.choice(len(rules), p=weights)
    else:
        idx = np.random.choice(len(rules), p=weights)
        
    return rules[idx]
