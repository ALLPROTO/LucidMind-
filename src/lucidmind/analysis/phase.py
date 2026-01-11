import numpy as np
import os
from typing import Dict, List, Tuple, Any
from .stability import classify_run
from ..experiments.runner import ExperimentRunner

class PhaseAnalyzer:
    """
    Computes 2D phase diagrams of stability across parameter grids.
    """
    def __init__(self, base_config: Dict[str, Any]):
        self.base_config = base_config
        self.class_map = {'STABLE': 0, 'EXPLOSION': 1, 'COLLAPSE': 2, 'UNSTABLE': 3}
        self.inv_class_map = {v: k for k, v in self.class_map.items()}

    def sweep_2d(
        self, 
        param1: str, range1: np.ndarray, 
        param2: str, range2: np.ndarray,
        n_runs: int = 5,
        T: int = 1000
    ) -> Dict[str, Any]:
        """
        Sweeps two parameters and classifies the outcome at each point.
        """
        grid = np.zeros((len(range1), len(range2)), dtype=int)
        confidence = np.zeros((len(range1), len(range2)), dtype=float)
        
        print(f"Starting 2D sweep: {param1} vs {param2}")
        print(f"Grid size: {len(range1)}x{len(range2)}, {n_runs} runs per point")
        
        for i, val1 in enumerate(range1):
            for j, val2 in enumerate(range2):
                config = self.base_config.copy()
                config[param1] = val1
                config[param2] = val2
                config['T'] = T
                
                runner = ExperimentRunner(config)
                point_classes = []
                
                for r in range(n_runs):
                    metrics = runner.run_metrics_only(seed=42+r)
                    cls = classify_run(metrics)
                    point_classes.append(self.class_map[cls])
                
                # Assign mode (most frequent class)
                counts = np.bincount(point_classes, minlength=4)
                grid[i, j] = np.argmax(counts)
                confidence[i, j] = counts[grid[i, j]] / n_runs
                
            print(f"  Row {i+1}/{len(range1)} complete")

        return {
            'param1': param1,
            'param2': param2,
            'range1': range1.tolist(),
            'range2': range2.tolist(),
            'grid': grid.tolist(),
            'confidence': confidence.tolist(),
            'class_map': self.inv_class_map
        }

    def save_results(self, results: Dict, filename: str):
        """
        Saves sweep results as a JSON or NPZ file.
        """
        import json
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Phase diagram results saved to {filename}")
