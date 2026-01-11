import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Optional

def plot_complexity_traces(
    traces: List[np.ndarray], 
    labels: Optional[List[str]] = None,
    title: str = "Complexity Traces",
    save_path: Optional[str] = None
):
    """
    Plots multiple complexity traces on one figure.
    """
    plt.figure(figsize=(10, 6))
    for i, trace in enumerate(traces):
        label = labels[i] if labels else f"Run {i}"
        plt.plot(trace, alpha=0.7, label=label)
        
    plt.xlabel("Timestep")
    plt.ylabel("Complexity")
    plt.title(title)
    if labels:
        plt.legend()
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()

def plot_entropy_with_drift(
    entropy: np.ndarray,
    title: str = "Entropy and Drift",
    save_path: Optional[str] = None
):
    """
    Plots entropy and its drift (derivative).
    """
    drift = np.diff(entropy)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    ax1.plot(entropy, color='blue')
    ax1.set_ylabel("Entropy")
    ax1.set_title(title)
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(drift, color='red', alpha=0.5)
    ax2.axhline(0, color='black', linestyle='--', alpha=0.3)
    ax2.set_ylabel("Drift")
    ax2.set_xlabel("Timestep")
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
