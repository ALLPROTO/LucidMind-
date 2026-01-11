import numpy as np
from typing import List, Dict, Any

def compute_damping_ratio(killed_total: int, born_total: int) -> float:
    """
    Computes the damping ratio (killed/born).
    
    See: docs/math_core.md#6-lifecycle-and-damping
    
    Args:
        killed_total: Total number of rules killed
        born_total: Total number of rules born
        
    Returns:
        Damping ratio in [0, 1]
    """
    if born_total == 0:
        return 0.0
    return min(1.0, killed_total / born_total)

def get_rule_strength_stats(rules: List[Any]) -> Dict[str, float]:
    """
    Computes statistics for the current set of rules.
    """
    if not rules:
        return {'mean': 0.0, 'std': 0.0, 'min': 0.0, 'max': 0.0}
        
    strengths = np.array([r.strength for r in rules])
    return {
        'mean': float(np.mean(strengths)),
        'std': float(np.std(strengths)),
        'min': float(np.min(strengths)),
        'max': float(np.max(strengths))
    }
