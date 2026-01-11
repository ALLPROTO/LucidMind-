from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    # State space dimension
    'N': 32,
    
    # Simulation steps
    'T': 3000,
    
    # Dynamics parameters
    'tau': 0.2,
    'noise_sigma': 0.03,
    'alpha': 0.05,
    'beta': 0.03,
    'death_threshold': -0.5,
    'birth_window': 25,
    'bad_steps_to_birth': 15,
    'k_delta': 0.05,
    
    # Gating parameters
    'gate_k': 3.0,
    'gate_T': 0.8,
}
