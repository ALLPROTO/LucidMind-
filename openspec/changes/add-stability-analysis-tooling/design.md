# Design: Add Stability Analysis Tooling

## Context

With core metrics instrumentation complete, we need systematic tools to:
1. Find stable operating regions ("zone of life")
2. Map parameter space boundaries (where explosion/collapse occur)
3. Understand rule lifecycle patterns
4. Measure system robustness to perturbations

This is the final piece needed before adding any external inputs to the kernel.

## Goals / Non-Goals

### Goals
- Automatically identify stability windows from experimental data
- Generate phase diagrams for parameter pairs
- Characterize "healthy" vs "parasitic" rules
- Quantify perturbation recovery capability

### Non-Goals
- Modifying kernel dynamics
- Machine learning on metrics
- Real-time monitoring (batch analysis focus)

## Decisions

### Decision 1: Stability Classification Criteria
**What**: A run is classified using formal criteria:

| Classification | Criteria |
|----------------|----------|
| **STABLE** | No explosion conditions triggered AND complexity stays in `[C_min, C_max]` for >90% of timesteps AND damping_ratio ∈ `[0.3, 0.9]` |
| **EXPLOSION** | Any explosion condition (E1-E4) triggered |
| **COLLAPSE** | Complexity < C_min for >50 consecutive steps AND no explosion |
| **UNSTABLE** | Does not meet STABLE criteria but not EXPLOSION or COLLAPSE |

**Why**: Clear binary classification enables automated phase diagram generation.

### Decision 2: Phase Diagram Methodology
**What**: 2D parameter sweep with classification at each grid point.

**Implementation**:
```python
def generate_phase_diagram(
    param1: str, range1: Tuple[float, float], steps1: int,
    param2: str, range2: Tuple[float, float], steps2: int,
    n_runs_per_point: int = 10
) -> PhaseDiagram:
    """
    Returns NxM grid with classification at each point.
    Classification = mode(run_classifications) for that point.
    """
```

**Visualization**: Heatmap with:
- Green = STABLE
- Red = EXPLOSION
- Blue = COLLAPSE  
- Yellow = UNSTABLE

### Decision 3: Rule Characterization
**What**: Rules are characterized by lifecycle metrics:

| Metric | Definition | Good Rule | Parasitic Rule |
|--------|------------|-----------|----------------|
| Lifespan | death_t - birth_t | > median | < 10% median |
| Peak strength | max(strength over lifetime) | > 0.5 | < 0.1 |
| Contribution | sum(complexity_reduction when applied) | > 0 | ≤ 0 |

**Why**: Understanding what makes rules "good" informs future kernel improvements (after research phase).

### Decision 4: Recovery Time Protocol
**What**: Formal perturbation-recovery measurement:

1. Run kernel to timestep T₀ (steady state)
2. Save state S₀ and continue unperturbed run as baseline
3. Apply perturbation: S₀' = S₀ + ε·e_i (single component)
4. Run from S₀' for N steps
5. Compute distance to baseline at each step
6. Recovery time = first step where distance < δ (or ∞ if never)

**Why**: Quantifies robustness and readiness for external input.

## Analysis Module Structure

```
src/lucidmind/
├── analysis/
│   ├── __init__.py
│   ├── stability.py    # Stability window detection
│   ├── phase.py        # Phase diagram generation
│   ├── rules.py        # Rule lifecycle analysis
│   ├── recovery.py     # Perturbation response
│   └── sweep.py        # Parameter sweep framework
└── visualization/
    ├── __init__.py
    ├── traces.py       # Time series plots
    ├── phase_diagram.py # Heatmap plots
    ├── rules.py        # Rule lifecycle plots
    └── dashboard.py    # Summary figures

scripts/
├── run_stability_analysis.py
├── run_parameter_sweep.py
├── run_rule_analysis.py
└── generate_phase_diagram.py
```

## Parameter Sweep Strategy

**Day 1-2 Priority Parameters** (based on lucid_v0.py):

| Parameter | Range to Explore | Why |
|-----------|------------------|-----|
| `tau` | 0.1 - 0.5 | Complexity threshold sensitivity |
| `alpha` | 0.01 - 0.2 | Positive reinforcement rate |
| `beta` | 0.01 - 0.2 | Negative reinforcement rate |
| `noise_sigma` | 0.01 - 0.1 | System noise level |
| `gate_k` | 1.0 - 10.0 | Sigmoid steepness |
| `death_threshold` | -1.0 - 0.0 | Rule death sensitivity |

**Key 2D Sweeps**:
1. `alpha` vs `beta` — reinforcement balance
2. `tau` vs `noise_sigma` — signal vs noise threshold
3. `gate_k` vs `gate_T` — gating dynamics

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Sweep takes too long | Start with coarse grid (5x5), refine interesting regions |
| Classification thresholds too strict/loose | Make configurable; iterate based on results |
| Visualization overwhelming | Focus on key plots; add dashboard view |

## Open Questions

- **Q1**: How many runs per parameter combination for reliable classification?
  - **Tentative**: 10 runs minimum; report classification confidence.

- **Q2**: Should recovery analysis perturb all components or just one?
  - **Tentative**: Single component first; full perturbation analysis later.

- **Q3**: What defines "steady state" for recovery protocol starting point?
  - **Tentative**: T₀ = 500 steps (after initial transient).
