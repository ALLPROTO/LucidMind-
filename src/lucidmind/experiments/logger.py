import json
import os
import csv
from datetime import datetime
from typing import Dict, Any, List
import numpy as np

class ExperimentLogger:
    """
    Handles logging of experiment metrics and state trajectories.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Use microseconds to avoid collisions in rapid batch runs
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        self.run_dir = os.path.join(output_dir, f"run_{self.timestamp}")
        os.makedirs(self.run_dir, exist_ok=True)
        
        self.metrics_file = os.path.join(self.run_dir, "metrics.csv")
        self.config_file = os.path.join(self.run_dir, "config.json")
        
        self.history: List[Dict[str, Any]] = []

    def log_config(self, config: Dict[str, Any]):
        """Saves experiment configuration."""
        with open(self.config_file, 'w') as f:
            # Handle non-serializable objects if any
            clean_config = {k: v for k, v in config.items() if isinstance(v, (int, float, str, bool, list, dict))}
            json.dump(clean_config, f, indent=4)

    def log_step(self, step_data: Dict[str, Any]):
        """Logs data for a single step."""
        # Convert objects to serializable form if needed
        data = {k: v for k, v in step_data.items() if k != 'applied_rule' and k != 'state'}
        if step_data.get('applied_rule'):
            data['rule_strength'] = step_data['applied_rule'].strength
        else:
            data['rule_strength'] = None
            
        self.history.append(data)

    def save(self):
        """Saves collected history to CSV."""
        if not self.history:
            return
            
        keys = self.history[0].keys()
        with open(self.metrics_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.history)
            
    def save_trajectory(self, trajectory: List[np.ndarray]):
        """Saves full state trajectory to a numpy file."""
        traj_file = os.path.join(self.run_dir, "trajectory.npy")
        np.save(traj_file, np.array(trajectory))
