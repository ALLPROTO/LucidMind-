import numpy as np
import copy
from typing import Dict, Any, List, Tuple
from ..core.kernel import Kernel

def measure_recovery(
    kernel: Kernel,
    n_steps: int = 200,
    perturbation_mag: float = 0.01,
    recovery_threshold: float = 0.05
) -> Dict[str, Any]:
    """
    Measures recovery time from a perturbation at the current state.
    
    Args:
        kernel: Current kernel state (will be cloned)
        n_steps: How many steps to run for recovery
        perturbation_mag: Magnitude of change to first state component
        recovery_threshold: Distance below which system is considered "recovered"
        
    Returns:
        Dict with recovery metrics
    """
    k_baseline = copy.deepcopy(kernel)
    k_perturbed = copy.deepcopy(kernel)
    
    # Apply perturbation
    k_perturbed.S[0] += perturbation_mag
    
    distances = []
    recovered_at = -1
    
    for t in range(n_steps):
        res_b = k_baseline.step()
        res_p = k_perturbed.step()
        
        dist = np.linalg.norm(res_b['state'] - res_p['state'])
        distances.append(float(dist))
        
        if recovered_at == -1 and dist < recovery_threshold:
            # Check if it STAYS below threshold for a bit
            recovered_at = t
            
    return {
        'distances': distances,
        'recovery_time': recovered_at if recovered_at != -1 else n_steps,
        'recovered': recovered_at != -1,
        'max_divergence': float(np.max(distances)),
        'final_distance': float(distances[-1])
    }
