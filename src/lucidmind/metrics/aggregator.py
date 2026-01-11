import numpy as np
from typing import List, Dict, Any

def aggregate_metrics(all_run_metrics: List[Dict[str, np.ndarray]]) -> Dict[str, Dict[str, np.ndarray]]:
    """
    Aggregates metrics across multiple runs (mean, std, percentiles).
    
    See: docs/math_core.md#71-statistical-aggregation
    
    Args:
        all_run_metrics: List of dicts, where each dict has metric names as keys 
                         and 1D arrays of values over time as values.
                         
    Returns:
        Dict of metric names -> Dict of stats (mean, std, p5, p25, p50, p75, p95)
    """
    if not all_run_metrics:
        return {}
        
    metric_names = all_run_metrics[0].keys()
    aggregated = {}
    
    for name in metric_names:
        # Stack all runs for this metric: (n_runs, T)
        data = np.stack([run[name] for run in all_run_metrics if name in run])
        
        aggregated[name] = {
            'mean': np.mean(data, axis=0),
            'std': np.std(data, axis=0),
            'p5': np.percentile(data, 5, axis=0),
            'p25': np.percentile(data, 25, axis=0),
            'p50': np.percentile(data, 50, axis=0),
            'p75': np.percentile(data, 75, axis=0),
            'p95': np.percentile(data, 95, axis=0)
        }
        
    return aggregated

def find_stability_window(aggregated_complexity: Dict[str, np.ndarray]) -> Dict[str, float]:
    """
    Identifies the stability window bounds based on aggregated complexity.
    """
    mean_comp = aggregated_complexity['mean']
    p5 = aggregated_complexity['p5']
    p95 = aggregated_complexity['p95']
    
    return {
        'c_min_stable': float(np.min(p5)),
        'c_max_stable': float(np.max(p95)),
        'c_avg_stable': float(np.mean(mean_comp))
    }
