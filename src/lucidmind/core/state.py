import numpy as np

def complexity(S: np.ndarray, tau: float = 0.2) -> int:
    """
    Measures the 'uncompressed' complexity of the state S.
    
    Count of components with absolute value greater than threshold tau.
    
    See: docs/math_core.md#51-high-gradient-manifold-hgm
    """
    return int(np.sum(np.abs(S) > tau))

def entropy(S: np.ndarray) -> float:
    """
    Calculates the normalized entropy of the state vector distribution.
    
    Args:
        S: State vector
        
    Returns:
        Entropy value (scalar)
    """
    p = np.abs(S) / (np.sum(np.abs(S)) + 1e-9)
    return -float(np.sum(p * np.log(p + 1e-9)))
