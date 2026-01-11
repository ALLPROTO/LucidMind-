# Design: Add Core Metrics Instrumentation

## Context

The LucidMind kernel is a self-organizing system that must be studied in isolation before adding semantic inputs. This requires comprehensive metrics to:
1. Characterize stable operating regions ("stability windows")
2. Detect pathological states (explosion, collapse)
3. Measure the effectiveness of the rule lifecycle (immune system)
4. Enable comparison across parameter sweeps

## Goals / Non-Goals

### Goals
- Provide real-time metrics computation during simulation
- Enable post-hoc analysis from saved trajectories
- Define formal criteria for explosion and collapse
- Support both single-run and multi-run analysis

### Non-Goals
- Modifying kernel dynamics
- Real-time visualization (separate concern)
- Statistical modeling or ML on metrics

## Decisions

### Decision 1: Metric Computation Strategy
**What**: Metrics are computed both online (during simulation) and offline (from saved state histories).
**Why**:
- Online: Enables early termination on explosion
- Offline: Allows new metrics to be computed on historical data

**Implementation**:
```python
class MetricsCollector:
    def on_step(self, state: np.ndarray, rules: List[Rule], t: int) -> None:
        """Called after each simulation step."""
        
    def finalize(self) -> MetricsResult:
        """Compute final metrics after simulation ends."""
```

### Decision 2: Explosion Conditions (Formal Definitions)
**What**: Four formal conditions define "explosion" (any sufficient):

| Condition | Definition | Detection |
|-----------|------------|-----------|
| E1: Unbounded Growth | `complexity(S_t)` grows exponentially | Exponential fit with R² > 0.9 on sliding window |
| E2: Entropy Lock | `entropy(S_t) ≈ constant_high` for `t > T` | Variance of entropy < ε for last N steps, value > threshold |
| E3: Rule Saturation | Rules never die | `killed/born < min_damping_ratio` for last N steps |
| E4: Irreversible Sensitivity | Small perturbation → large permanent change | `|S_{t+1} - S_t| >> ε` after micro perturbation |

**Why**: Formal definitions enable automated detection and reproducible classification.

### Decision 3: Entropy Definition
**What**: Use normalized absolute-value distribution entropy.
```python
def entropy(S: np.ndarray) -> float:
    p = np.abs(S) / (np.sum(np.abs(S)) + 1e-9)
    return -np.sum(p * np.log(p + 1e-9))
```
**Why**: 
- Handles signed state values
- Bounded for fixed dimension N
- Interpretable: max when uniform, low when concentrated

**Alternative considered**: Shannon entropy on discretized bins — rejected as too sensitive to binning choices.

### Decision 4: Damping Ratio for Immune System Health
**What**: Track `damping_ratio = killed_rules / born_rules` as measure of self-regulation.
**Why**:
- Ratio ≈ 0: No immune response (accumulating parasites)
- Ratio ≈ 1: Perfect balance (healthy turnover)
- Ratio > 1: Not possible (can't kill more than born)

**Healthy range**: `0.3 < damping_ratio < 0.9` (tentative, to be determined empirically)

### Decision 5: Trajectory Diversity for Multi-Run Analysis
**What**: Compute pairwise L2 distance between trajectories at each timestep.
```python
diversity(t) = mean([||S_i(t) - S_j(t)||_2 for all i < j])
```
**Why**:
- Measures potential for varied responses from same initial conditions
- Too high: chaos; Too low: deterministic lock

## Metrics Module Structure

```
src/lucidmind/metrics/
├── __init__.py
├── complexity.py      # Complexity computation and thresholds
├── entropy.py         # State entropy and drift
├── explosion.py       # E1-E4 detection
├── collapse.py        # Collapse detection
├── rules.py           # Rule lifecycle tracking
├── trajectory.py      # Trajectory storage and analysis
└── aggregator.py      # Multi-run aggregation
```

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Metrics computation overhead slows simulation | Profile; use vectorized numpy operations |
| Threshold sensitivity for explosion detection | Make thresholds configurable; report raw metrics too |
| Entropy definition may not capture all structure loss | Monitor alongside complexity; treat as complementary |

## Open Questions

- **Q1**: Should explosion detection halt the simulation immediately?
  - **Tentative**: Yes, with configurable `halt_on_explosion: bool` flag.

- **Q2**: What window size for sliding-window metrics?
  - **Tentative**: 50 steps default, configurable.
