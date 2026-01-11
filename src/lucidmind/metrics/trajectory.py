import numpy as np
from typing import List

def compute_pairwise_distances(trajectories: List[np.ndarray]) -> np.ndarray:
    """
    Computes L2 distance between all pairs of trajectories at each timestep.
    
    Args:
        trajectories: List of (T, N) arrays
        
    Returns:
        Array of shape (T,) with mean pairwise distance
    """
    if len(trajectories) < 2:
        return np.zeros(0)
        
    n_runs = len(trajectories)
    T = trajectories[0].shape[0]
    
    avg_distances = np.zeros(T)
    
    for t in range(T):
        states = np.stack([traj[t] for traj in trajectories]) # (n_runs, N)
        
        # Vectorized pairwise L2 distance
        diff = states[:, np.newaxis, :] - states[np.newaxis, :, :]
        dist = np.sqrt(np.sum(diff**2, axis=-1))
        
        # Average of upper triangle
        total_pairs = n_runs * (n_runs - 1) / 2
        avg_distances[t] = np.sum(np.triu(dist, k=1)) / total_pairs
        
    return avg_distances

def compute_trajectory_diversity(trajectories: List[np.ndarray]) -> float:
    """
    Computes overall diversity as average pairwise distance over time.
    """
    if not trajectories:
        return 0.0
    
    avg_over_time = compute_pairwise_distances(trajectories)
    return float(np.mean(avg_over_time))
