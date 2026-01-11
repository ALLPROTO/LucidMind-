import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, Optional

def plot_phase_diagram(
    sweep_results: Dict[str, Any],
    save_path: Optional[str] = None
):
    """
    Plots a 2D phase diagram from sweep results.
    """
    grid = np.array(sweep_results['grid'])
    range1 = sweep_results['range1']
    range2 = sweep_results['range2']
    param1 = sweep_results['param1']
    param2 = sweep_results['param2']
    
    plt.figure(figsize=(8, 7))
    
    # Custom colormap
    # 0=STABLE (Green), 1=EXPLOSION (Red), 2=COLLAPSE (Blue), 3=UNSTABLE (Yellow)
    from matplotlib.colors import ListedColormap
    colors = ['#2ca02c', '#d62728', '#1f77b4', '#ff7f0e']
    cmap = ListedColormap(colors)
    
    im = plt.imshow(
        grid.T, 
        origin='lower', 
        extent=[min(range1), max(range1), min(range2), max(range2)],
        aspect='auto',
        cmap=cmap,
        vmin=0, vmax=3
    )
    
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.title(f"Phase Diagram: {param1} vs {param2}")
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2ca02c', label='STABLE'),
        Patch(facecolor='#d62728', label='EXPLOSION'),
        Patch(facecolor='#1f77b4', label='COLLAPSE'),
        Patch(facecolor='#ff7f0e', label='UNSTABLE')
    ]
    plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
