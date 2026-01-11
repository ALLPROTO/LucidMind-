import numpy as np
from typing import Dict, Any, Optional
from ..core.kernel import Kernel
from .logger import ExperimentLogger

class ExperimentRunner:
    """
    Executes simulations and handles logging.
    """
    def __init__(self, config: Dict[str, Any], output_root: str = "experiments/results"):
        self.config = config
        self.output_root = output_root

    def run_single(self, seed: Optional[int] = None) -> str:
        """
        Runs a single simulation experiment.
        
        Returns:
            The directory where results were saved.
        """
        rng = np.random.default_rng(seed)
        kernel = Kernel(self.config, rng=rng)
        logger = ExperimentLogger(self.output_root)
        
        logger.log_config({**self.config, 'seed': seed})
        
        trajectory = []
        T = self.config.get('T', 3000)
        
        for t in range(1, T + 1):
            step_result = kernel.step()
            logger.log_step(step_result)
            trajectory.append(step_result['state'])
            
        logger.save()
        logger.save_trajectory(trajectory)
        
        return logger.run_dir

    def run_batch(self, n_runs: int, seed_start: int = 42):
        """
        Runs a batch of experiments with sequential seeds.
        """
        print(f"Starting batch experiment: {n_runs} runs, seed_start={seed_start}")
        for i in range(n_runs):
            seed = seed_start + i
            run_dir = self.run_single(seed=seed)
            print(f"  Run {i+1}/{n_runs} complete: {run_dir}")

    def run_metrics_only(self, seed: Optional[int] = None) -> Dict[str, Any]:
        """
        Runs a simulation and returns final aggregated metrics without disk IO.
        """
        rng = np.random.default_rng(seed)
        kernel = Kernel(self.config, rng=rng)
        
        comp_hist = []
        ent_hist = []
        T = self.config.get('T', 1000)
        
        for t in range(T):
            res = kernel.step()
            comp_hist.append(res['complexity'])
            ent_hist.append(res['entropy'])
            
        stats = kernel.get_stats()
        
        return {
            'complexity_history': comp_hist,
            'entropy_history': ent_hist,
            'damping_ratio': stats['damping_ratio'],
            'born_total': stats['born_total'],
            'alive_count': stats['alive_count']
        }
