import argparse
import numpy as np
import os
from lucidmind.analysis.phase import PhaseAnalyzer
from lucidmind.visualization.phase_diagram import plot_phase_diagram
from lucidmind.config.loader import load_config

def main():
    parser = argparse.ArgumentParser(description="Generate 2D phase diagram")
    parser.add_argument("--p1", type=str, default="alpha", help="Parameter 1")
    parser.add_argument("--p1_range", type=float, nargs=3, default=[0.01, 0.15, 5], help="min max steps")
    parser.add_argument("--p2", type=str, default="beta", help="Parameter 2")
    parser.add_argument("--p2_range", type=float, nargs=3, default=[0.01, 0.15, 5], help="min max steps")
    parser.add_argument("--runs", type=int, default=5, help="Runs per point")
    parser.add_argument("--steps", type=int, default=500, help="Timesteps per run")
    parser.add_argument("--out", type=str, default="phase_diagram.png", help="Output plot path")
    args = parser.parse_args()
    
    config = load_config()
    analyzer = PhaseAnalyzer(config)
    
    r1 = np.linspace(args.p1_range[0], args.p1_range[1], int(args.p1_range[2]))
    r2 = np.linspace(args.p2_range[0], args.p2_range[1], int(args.p2_range[2]))
    
    results = analyzer.sweep_2d(
        args.p1, r1,
        args.p2, r2,
        n_runs=args.runs,
        T=args.steps
    )
    
    plot_phase_diagram(results, save_path=args.out)
    
    # Save data too
    data_path = args.out.replace('.png', '.json')
    analyzer.save_results(results, data_path)

if __name__ == "__main__":
    main()
