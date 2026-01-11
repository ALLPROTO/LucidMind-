# Change: Add Core Metrics Instrumentation

## Why

The LucidMind kernel must be studied as a physical system before adding semantic processing. Currently, the `lucid_v0.py` prototype tracks only basic `complexity` and rule counts. To understand kernel dynamics and find the "stability window" (the parameter space where the system neither explodes nor collapses), we need a comprehensive metrics system.

Key questions this instrumentation must answer:
1. **Where is the plateau vs. explosion?** — Stability Window analysis
2. **Does the system self-organize or just produce noise?** — Entropy tracking
3. **Is the immune system (rule lifecycle) working?** — Birth/death ratio analysis
4. **Can the system recover from perturbations?** — Recovery time measurement

## What Changes

- **Add complexity metrics** with configurable thresholds for plateau/explosion detection
- **Add entropy computation** for state distribution analysis
- **Add entropy drift tracking** to detect monotonic degradation
- **Add rule lifecycle metrics** (born, killed, damping ratio)
- **Add trajectory diversity measurement** for multi-run analysis
- **Add collapse detection** with frequency tracking
- **Add explosion condition detection** (E1-E4 from requirements)

## Impact

- **Affected specs**: New `core-metrics` capability
- **Affected code**: Creates `src/lucidmind/metrics/` module
- **Dependencies**: Requires `setup-core-research-environment` change
- **Breaking changes**: None (additive only)
