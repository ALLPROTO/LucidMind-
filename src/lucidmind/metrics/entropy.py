import numpy as np
from typing import Optional
from lucidmind.core.state import entropy

def compute_entropy(S: np.ndarray) -> float:
    """
    Computes the normalized entropy of the state vector distribution.
    
    See: docs/math_core.md#52-entropy-and-distribution
    
    Args:
        S: State vector
        
    Returns:
        Entropy value (scalar)
    """
    return entropy(S)

def compute_entropy_drift(entropy_t: float, entropy_prev: float) -> float:
    """
    Computes the change in entropy between consecutive steps.
    """
    return entropy_t - entropy_prev

def detect_entropy_lock(entropy_history: np.ndarray, threshold: float = 0.5, epsilon: float = 0.01) -> bool:
    """
    Detects if entropy is locked at a high constant value (Condition E2).
    
    Args:
        entropy_history: Recent entropy values
        threshold: Minimum entropy value to consider "high"
        epsilon: Maximum variance allowed for "constant"
        
    Returns:
        True if entropy lock is detected
    """
    if len(entropy_history) < 10:
        return False
        
    avg = np.mean(entropy_history)
    var = np.var(entropy_history)
    
    return avg > threshold and var < epsilon
