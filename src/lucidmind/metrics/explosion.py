import numpy as np
from scipy import stats
from .entropy import detect_entropy_lock

def detect_unbounded_growth(complexity_history: np.ndarray, min_window: int = 50) -> bool:
    """
    Detects exponential growth in complexity (Condition E1).
    """
    if len(complexity_history) < min_window:
        return False
        
    y = np.array(complexity_history[-min_window:], dtype=float)
    x = np.arange(len(y))
    
    # Check for exponential growth by linear fit on log values
    # Add small constant to avoid log(0)
    y_log = np.log(y + 1e-6)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y_log)
    
    # Growth is unbounded if slope is positive and fit is strong
    # Slope > 0.1 corresponds to doubling approximately every 7 steps
    return slope > 0.1 and r_value**2 > 0.9

def detect_rule_saturation(damping_ratio: float, born_total: int, min_born: int = 10) -> bool:
    """
    Detects if rules are being born but not dying (Condition E3).
    """
    if born_total < min_born:
        return False
        
    return damping_ratio < 0.1

def detect_irreversible_sensitivity(
    baseline_traj: np.ndarray, 
    perturbed_traj: np.ndarray, 
    delta: float, 
    k: float = 10.0, 
    m: int = 20
) -> bool:
    """
    Detects irreversible sensitivity to small perturbations (Condition E4).
    """
    if len(baseline_traj) != len(perturbed_traj):
        return False
        
    distances = np.linalg.norm(baseline_traj - perturbed_traj, axis=1)
    large_response = np.any(distances > k * delta)
    
    # Check last m steps
    if len(distances) < m:
        return False
        
    recent_distances = distances[-m:]
    not_returned = np.all(recent_distances > delta)
    
    return large_response and not_returned

def check_explosion(metrics: dict) -> list:
    """
    Checks all explosion conditions.
    
    Returns:
        List of triggered condition IDs (E1, E2, E3, E4)
    """
    triggered = []
    
    if metrics.get('complexity_history') is not None:
        if detect_unbounded_growth(metrics['complexity_history']):
            triggered.append('E1')
            
    if metrics.get('entropy_history') is not None:
        if detect_entropy_lock(metrics['entropy_history']):
            triggered.append('E2')
            
    if metrics.get('damping_ratio') is not None:
        if detect_rule_saturation(metrics['damping_ratio'], metrics.get('born_total', 0)):
            triggered.append('E3')
            
    if metrics.get('baseline_trajectory') is not None and metrics.get('perturbed_trajectory') is not None:
        delta = metrics.get('perturbation_delta', 1e-6)
        if detect_irreversible_sensitivity(metrics['baseline_trajectory'], metrics['perturbed_trajectory'], delta):
            triggered.append('E4')
            
    return triggered
