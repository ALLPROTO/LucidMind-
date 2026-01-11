import numpy as np
from typing import Dict, List, Tuple
from ..metrics.explosion import check_explosion

def classify_run(
    metrics: Dict, 
    c_min: int = 5, 
    c_max_abs: int = 32, 
    t_min_consecutive: int = 50,
    stable_percentage: float = 0.9
) -> str:
    """
    Classifies a run into STABLE, EXPLOSION, COLLAPSE, or UNSTABLE.
    
    Returns:
        One of: 'STABLE', 'EXPLOSION', 'COLLAPSE', 'UNSTABLE'
    """
    # 1. Check for explosions (E1-E4)
    explosions = check_explosion(metrics)
    if len(explosions) > 0:
        return "EXPLOSION"
        
    # 2. Check for collapse
    comp_history = metrics.get('complexity_history', [])
    if len(comp_history) == 0:
        return "UNSTABLE"
        
    comp_history = np.array(comp_history)
    
    # Consecutive sub-sequences where comp < c_min
    below_min = comp_history < c_min
    max_consecutive = 0
    current_consecutive = 0
    for val in below_min:
        if val:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0
            
    if max_consecutive >= t_min_consecutive:
        return "COLLAPSE"
        
    # 3. Check for stability
    # Must be in range for most of the time
    in_range = (comp_history >= c_min) & (comp_history <= c_max_abs)
    percentage = np.mean(in_range)
    
    # Healthy damping ratio check (if available)
    damping_ratio = metrics.get('damping_ratio')
    healthy_damping = True
    if damping_ratio is not None:
        healthy_damping = 0.2 <= damping_ratio <= 0.95
        
    if percentage >= stable_percentage and healthy_damping:
        return "STABLE"
        
    return "UNSTABLE"

def find_stability_window(complexity_history: np.ndarray) -> Tuple[float, float]:
    """
    Identifies the complexity bounds [C_min_stable, C_max_stable] where the system operates.
    Uses the interquartile range or similar robust metric to filter outliers.
    """
    if len(complexity_history) < 50:
        return (0.0, 0.0)
        
    # Avoid initial transient (first 10%)
    steady_state = complexity_history[int(len(complexity_history)*0.1):]
    
    if len(steady_state) == 0:
        return (0.0, 0.0)
        
    c_min = np.percentile(steady_state, 5)
    c_max = np.percentile(steady_state, 95)
    
    return (float(c_min), float(c_max))

def compute_stability_report(run_metrics_list: List[Dict]) -> Dict:
    """
    Aggregates stability statistics across multiple runs.
    """
    classifications = [classify_run(m) for m in run_metrics_list]
    counts = {
        'STABLE': classifications.count('STABLE'),
        'EXPLOSION': classifications.count('EXPLOSION'),
        'COLLAPSE': classifications.count('COLLAPSE'),
        'UNSTABLE': classifications.count('UNSTABLE')
    }
    
    total = len(classifications)
    percentages = {k: v / total for k, v in counts.items()}
    
    windows = [find_stability_window(np.array(m['complexity_history'])) 
               for m in run_metrics_list if classify_run(m) == 'STABLE']
    
    if windows:
        avg_window_min = np.mean([w[0] for w in windows])
        avg_window_max = np.mean([w[1] for w in windows])
    else:
        avg_window_min = avg_window_max = 0.0
        
    return {
        'counts': counts,
        'percentages': percentages,
        'avg_stability_window': (avg_window_min, avg_window_max),
        'passed': percentages['STABLE'] > 0.8
    }
