import numpy as np
from lucidmind.core.state import complexity

def compute_complexity(S: np.ndarray, tau: float = 0.2) -> int:
    """
    Computes the complexity of state S based on a threshold tau.
    
    See: docs/math_core.md#51-high-gradient-manifold-hgm
    
    Args:
        S: State vector
        tau: Threshold for considering a component active
        
    Returns:
        Number of active components
    """
    return complexity(S, tau)

def is_within_bounds(complexity: int, c_min: int, c_max: int) -> bool:
    """Checks if complexity is within specified stable bounds."""
    return c_min <= complexity <= c_max
