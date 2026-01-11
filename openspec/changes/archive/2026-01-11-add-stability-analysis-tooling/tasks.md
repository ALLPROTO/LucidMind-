# Tasks: Add Stability Analysis Tooling

## 1. Stability Window Analysis
- [x] 1.1 Create `src/lucidmind/analysis/stability.py` with stability window finder
- [x] 1.2 Implement automatic detection of complexity bounds `[C_min_stable, C_max_stable]`
- [x] 1.3 Compute percentage of timesteps within stability window per run
- [x] 1.4 Aggregate stability statistics across multiple runs
- [x] 1.5 Generate stability report with pass/fail criteria

## 2. Phase Diagram Generation
- [x] 2.1 Create `src/lucidmind/analysis/phase.py` for phase diagram computation
- [x] 2.2 Define 2D parameter grid (e.g., `tau` vs `alpha`, `noise_sigma` vs `gate_k`)
- [x] 2.3 Run experiments at each grid point and classify as stable/explosion/collapse
- [x] 2.4 Generate heatmap visualization of phase diagram
- [x] 2.5 Export phase diagram data for external analysis

## 3. Rule Lifecycle Analyzer
- [x] 3.1 Create `src/lucidmind/analysis/rules.py` for rule pattern analysis
- [x] 3.2 Compute rule lifespan distribution (time from birth to death)
- [x] 3.3 Analyze rule strength trajectories over lifetime
- [x] 3.4 Identify characteristics of "successful" rules (long-lived, high strength)
- [x] 3.5 Identify characteristics of "parasitic" rules (short-lived, negative contribution)
- [x] 3.6 Compute damping ratio over time and identify healthy operating regions

## 4. Recovery Analysis
- [x] 4.1 Create `src/lucidmind/analysis/recovery.py` for perturbation response
- [x] 4.2 Implement controlled perturbation injection (single component modification)
- [x] 4.3 Measure recovery time (timesteps to return within ε of baseline trajectory)
- [x] 4.4 Classify perturbation response: recovered / diverged / collapsed
- [x] 4.5 Create recovery time distribution across multiple perturbation magnitudes

## 5. Visualization Module
- [x] 5.1 Create `src/lucidmind/visualization/` subpackage
- [x] 5.2 Implement complexity trace plots (single run and multi-run overlay)
- [x] 5.3 Implement entropy trace plots with drift annotations
- [x] 5.4 Implement phase diagram heatmaps (Matplotlib + optional Plotly)
- [x] 5.5 Implement rule lifecycle timeline visualization
- [x] 5.6 Create summary dashboard figure with key metrics

## 6. Parameter Sweep Framework
- [x] 6.1 Create `src/lucidmind/analysis/sweep.py` for parameter exploration
- [x] 6.2 Define sweep configuration schema (parameter name, range, steps)
- [x] 6.3 Implement 1D sweep with metric plotting
- [x] 6.4 Implement 2D sweep with phase diagram output
- [x] 6.5 Add parallel execution support for sweep (optional, joblib or multiprocessing)

## 7. Analysis Scripts
- [x] 7.1 Create `scripts/run_stability_analysis.py` for single-config stability check
- [x] 7.2 Create `scripts/run_parameter_sweep.py` for automated sweeps
- [x] 7.3 Create `scripts/run_rule_analysis.py` for rule lifecycle investigation
- [x] 7.4 Create `scripts/generate_phase_diagram.py` for phase diagram creation
- [x] 7.5 Add CLI argument parsing for all scripts

## 8. Validation
- [x] 8.1 Verify stability window detection on known stable/unstable configurations
- [x] 8.2 Verify phase diagram correctly classifies test parameter combinations
- [x] 8.3 Integration test: full analysis pipeline from experiment to visualization
- [x] 8.4 Document interpretation guidelines for each visualization type
