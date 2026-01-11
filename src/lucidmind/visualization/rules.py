import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, Optional

def plot_rule_lifespans(
    analysis_results: Dict[str, Any],
    save_path: Optional[str] = None
):
    """
    Plots a histogram of rule lifespans.
    """
    lifespans = analysis_results.get('lifespans', [])
    if not lifespans:
        print("No lifespans to plot")
        return
        
    plt.figure(figsize=(10, 6))
    plt.hist(lifespans, bins=30, color='purple', alpha=0.7)
    plt.xlabel("Lifespan (timesteps)")
    plt.ylabel("Frequency")
    plt.title("Rule Lifespan Distribution")
    plt.grid(True, alpha=0.1)
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def plot_rule_strengths(
    analysis_results: Dict[str, Any],
    save_path: Optional[str] = None
):
    """
    Plots peak strengths vs lifespans.
    """
    lifespans = analysis_results.get('lifespans', [])
    peaks = analysis_results.get('peak_strengths', [])
    
    if len(lifespans) != len(peaks):
        # Filter peaks to only those that died if necessary
        # But analyze_rule_lifecycles returns them properly
        pass
        
    plt.figure(figsize=(10, 6))
    plt.scatter(lifespans, peaks, alpha=0.5, color='green')
    plt.xlabel("Lifespan")
    plt.ylabel("Peak Strength")
    plt.title("Rule Quality: Lifespan vs Strength")
    plt.grid(True, alpha=0.1)
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
