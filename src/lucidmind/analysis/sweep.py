import numpy as np
import json
import os
from typing import Dict, List, Any, Tuple
from ..experiments.runner import ExperimentRunner
from .stability import classify_run, compute_stability_report

class ParameterSweeper:
    """
    Framework for exploring the parameter space of the LucidMind kernel.
    """
    def __init__(self, base_config: Dict[str, Any]):
        self.base_config = base_config

    def sweep_1d(
        self, 
        param_name: str, 
        values: List[Any], 
        n_runs: int = 10,
        T: int = 1000
    ) -> Dict[str, Any]:
        """
        Runs a 1D sweep across a parameter and records stability stats.
        """
        results = []
        
        print(f"Starting 1D sweep for {param_name} across {len(values)} values")
        
        for val in values:
            config = self.base_config.copy()
            config[param_name] = val
            config['T'] = T
            
            runner = ExperimentRunner(config)
            run_metrics = []
            for r in range(n_runs):
                metrics = runner.run_metrics_only(seed=42+r)
                run_metrics.append(metrics)
                
            report = compute_stability_report(run_metrics)
            results.append({
                'value': val,
                'stable_pct': report['percentages']['STABLE'],
                'explosion_pct': report['percentages']['EXPLOSION'],
                'collapse_pct': report['percentages']['COLLAPSE'],
                'avg_window': report['avg_stability_window']
            })
            
            print(f"  {param_name}={val}: stable={report['percentages']['STABLE']:.2f}")
            
        return {
            'parameter': param_name,
            'values': values,
            'results': results
        }

    def save_results(self, results: Dict, filename: str):
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Sweep results saved to {filename}")
