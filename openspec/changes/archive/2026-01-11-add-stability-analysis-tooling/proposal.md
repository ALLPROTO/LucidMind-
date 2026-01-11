# Change: Add Stability Analysis Tooling

## Why

With metrics instrumentation in place, the next step is building tools to systematically analyze kernel stability. The goal is to find the "zone of life" — the parameter region where the kernel:
1. Neither explodes nor collapses
2. Maintains healthy rule lifecycle (damping ratio in acceptable range)
3. Produces diverse but bounded trajectories
4. Can recover from perturbations

This tooling will answer the critical questions:
- **Where is the plateau?** — Stable operating region
- **Where is the explosion?** — Boundaries of instability
- **What makes a rule "good"?** — Principles of rule generation/deletion

## What Changes

- **Add stability window analysis** to automatically find stable parameter ranges
- **Add phase diagram generation** visualizing stability across parameter sweeps
- **Add rule lifecycle analyzer** to understand birth/death patterns
- **Add recovery time measurement** for perturbation response analysis
- **Add visualization module** for metrics plots (complexity, entropy, phase diagrams)
- **Add parameter sweep framework** for systematic exploration

## Impact

- **Affected specs**: New `stability-analysis` capability
- **Affected code**: Creates `src/lucidmind/analysis/` module and `scripts/` directory
- **Dependencies**: Requires `add-core-metrics-instrumentation` change
- **Breaking changes**: None (additive only)
