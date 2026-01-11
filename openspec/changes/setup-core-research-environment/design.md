# Design: Setup Core Research Environment

## Context

LucidMind is in the Core Dynamics Research Phase. The `lucid_v0.py` prototype contains a working self-dynamics engine that must be:
1. **Frozen** - The kernel logic must not change during this research phase
2. **Instrumented** - Metrics must be collectible without modifying dynamics
3. **Reproducible** - Experiments must be exactly reproducible across runs and machines

This design establishes the foundation for systematic study of kernel behavior.

## Goals / Non-Goals

### Goals
- Establish reproducible conda-based Python environment
- Create modular source structure that separates core dynamics from instrumentation
- Enable batch experimentation with different seeds and parameters
- Provide structured logging for metric collection

### Non-Goals
- Modifying the kernel dynamics (strict freeze)
- Adding text/semantic processing
- GPU acceleration
- Distributed computation

## Decisions

### Decision 1: Conda for Environment Management
**What**: Use conda with `environment.yml` for all dependency management.
**Why**: 
- Reproducible environments across machines
- NumPy/SciPy benefit from conda's optimized BLAS/LAPACK
- Standard in scientific Python community
- Easy to version-lock dependencies

**Alternatives considered**:
- `pip + requirements.txt`: Less reproducible, no system-level dependencies
- `poetry`: Overkill for numerical-focused project, less numpy optimization

### Decision 2: Source Layout
**What**: Use `src/lucidmind/` layout with subpackages.
**Why**:
- `src/` layout prevents accidental import of uninstalled package
- Subpackages (`core/`, `metrics/`, `experiments/`) enforce separation of concerns
- Matches scientific Python best practices

```
src/
└── lucidmind/
    ├── __init__.py
    ├── core/           # Frozen kernel dynamics
    │   ├── __init__.py
    │   ├── kernel.py   # Main simulation loop
    │   ├── rule.py     # Rule class
    │   └── state.py    # State utilities
    ├── metrics/        # Metric computation (separate change)
    ├── experiments/    # Batch execution
    │   ├── __init__.py
    │   ├── runner.py   # Experiment executor
    │   └── logger.py   # Structured logging
    └── config/         # Configuration
        ├── __init__.py
        ├── defaults.py # Default parameters
        └── loader.py   # YAML loading
```

### Decision 3: Frozen Kernel Pattern
**What**: The `core/` module is read-only during research phase. Modifications require explicit approval.
**Why**:
- If kernel is unstable, the problem is in dynamics not in input
- Prevents "fixing symptoms" instead of understanding root causes
- Clear separation: core = physics, metrics = observation

**Enforcement**: Document in `project.md`; code review gate.

### Decision 4: YAML Configuration
**What**: Use YAML files for experiment parameters with Python dataclasses for type safety.
**Why**:
- Human-readable configuration
- Easy to version and diff
- Supports parameter sweeps
- Separates configuration from code

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Conda environment differences across platforms | Pin exact versions; test on CI |
| Kernel refactoring introduces bugs | Verify output matches original before/after |
| Configuration proliferation | Use layered defaults with minimal overrides |

## Migration Plan

1. Create `environment.yml` and verify on macOS
2. Create directory structure with `__init__.py` files
3. Port `lucid_v0.py` to modular structure
4. Add determinism test comparing old vs new output
5. Update `project.md` with new conventions

No breaking changes; additive only.

## Open Questions

- **Q1**: Should the frozen kernel allow logging hooks, or should metrics be computed externally from saved trajectories?
  - **Tentative**: Allow callback hooks for efficiency, but design so metrics can also be computed from saved state histories.
