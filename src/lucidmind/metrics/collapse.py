import numpy as np

def detect_collapse(complexity_history: np.ndarray, c_min: int = 2, window: int = 50) -> bool:
    """
    Detects if the system has collapsed (Condition: low complexity for long duration).
    
    See: docs/math_core.md#54-collapse-detection
    """
    if len(complexity_history) < window:
        return False
        
    recent = complexity_history[-window:]
    return bool(np.all(recent < c_min))
