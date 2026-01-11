import argparse
import os
import numpy as np
import yaml
from lucidmind.experiments.runner import ExperimentRunner
from lucidmind.analysis.stability import compute_stability_report
from lucidmind.config.loader import load_config

def main():
    parser = argparse.ArgumentParser(description="Run stability analysis for a single configuration")
    parser.add_argument("--config", type=str, help="Path to experimental config YAML")
    parser.add_argument("--runs", type=int, default=10, help="Number of runs")
    parser.add_argument("--steps", type=int, default=1000, help="Timesteps per run")
    args = parser.parse_args()
    
    config = load_config(args.config) if args.config else load_config()
    config['T'] = args.steps
    
    runner = ExperimentRunner(config)
    print(f"Running stability analysis for: {config}")
    
    run_metrics = []
    for i in range(args.runs):
        print(f"  Run {i+1}/{args.runs}...")
        metrics = runner.run_metrics_only(seed=100+i)
        run_metrics.append(metrics)
        
    report = compute_stability_report(run_metrics)
    
    print("\n" + "="*40)
    print("STABILITY REPORT")
    print("="*40)
    print(f"Runs: {args.runs}")
    print(f"Timesteps: {args.steps}")
    print("-" * 20)
    for cls, pct in report['percentages'].items():
        print(f"{cls:10}: {pct*100:6.1f}% ({report['counts'][cls]} runs)")
    print("-" * 20)
    print(f"Avg Stability Window: [{report['avg_stability_window'][0]:.2f}, {report['avg_stability_window'][1]:.2f}]")
    print(f"OVERALL STATUS: {'PASS' if report['passed'] else 'FAIL'}")
    print("="*40)

if __name__ == "__main__":
    main()
