# core-metrics Specification

## Purpose
TBD - created by archiving change add-core-metrics-instrumentation. Update Purpose after archive.
## Requirements
### Requirement: Complexity Metric
The system SHALL compute a complexity metric for each state vector representing the "energy" or "saturation" of the state.

#### Scenario: Complexity computation
- **WHEN** a state vector `S` of dimension `N` is provided
- **THEN** complexity is computed as the count of components with absolute value greater than threshold `tau`
- **AND** the result is an integer in range `[0, N]`

#### Scenario: Complexity trace logging
- **WHEN** a simulation runs for `T` timesteps
- **THEN** a complexity value is recorded for each timestep
- **AND** the full trace is available for analysis

---

### Requirement: Entropy Metric
The system SHALL compute an entropy metric measuring the distribution of state values.

#### Scenario: Entropy computation
- **WHEN** a state vector `S` is provided
- **THEN** entropy is computed as `-sum(p * log(p))` where `p = |S| / sum(|S|)`
- **AND** the result is a non-negative float

#### Scenario: Maximum entropy
- **WHEN** all state components have equal absolute values
- **THEN** entropy is at its maximum value `log(N)`

#### Scenario: Minimum entropy
- **WHEN** only one state component is non-zero
- **THEN** entropy approaches zero

---

### Requirement: Entropy Drift Tracking
The system SHALL track entropy drift as the change in entropy between consecutive timesteps.

#### Scenario: Drift computation
- **WHEN** entropy is computed at timesteps `t` and `t-1`
- **THEN** drift is computed as `entropy(t) - entropy(t-1)`

#### Scenario: Monotonic drift detection
- **WHEN** drift is consistently positive over a window of `W` steps
- **THEN** the system flags a "monotonic entropy increase" warning

#### Scenario: Healthy drift pattern
- **WHEN** drift alternates between positive and negative values
- **THEN** no warning is raised

---

### Requirement: Explosion Detection
The system SHALL detect explosion conditions defined as pathological states where dynamics become uncontrolled.

#### Scenario: E1 - Unbounded Growth
- **WHEN** complexity grows exponentially (R² > 0.9 on log-linear fit) over a sliding window
- **THEN** condition E1 is flagged as TRUE

#### Scenario: E2 - Entropy Lock
- **WHEN** entropy remains nearly constant (variance < ε) at a high value for `N` consecutive steps
- **THEN** condition E2 is flagged as TRUE

#### Scenario: E3 - Rule Saturation
- **WHEN** the damping ratio (`killed/born`) falls below minimum threshold for `N` consecutive steps
- **AND** rules continue to be born
- **THEN** condition E3 is flagged as TRUE

#### Scenario: E4 - Irreversible Sensitivity
- **WHEN** a micro-perturbation (magnitude < δ) is applied to the state
- **AND** the resulting state change is disproportionately large (> K * δ)
- **AND** the system does not return to baseline within `M` steps
- **THEN** condition E4 is flagged as TRUE

#### Scenario: Explosion event
- **WHEN** any explosion condition (E1, E2, E3, or E4) is TRUE
- **THEN** an explosion event is recorded with the condition identifier and timestep

---

### Requirement: Rule Lifecycle Metrics
The system SHALL track the lifecycle of rules including birth, death, and survival statistics.

#### Scenario: Birth tracking
- **WHEN** a new rule is created
- **THEN** the birth count is incremented
- **AND** the rule's birth timestep is recorded

#### Scenario: Death tracking
- **WHEN** a rule's strength falls below the death threshold and it is removed
- **THEN** the death count is incremented
- **AND** the rule's death timestep is recorded

#### Scenario: Damping ratio computation
- **WHEN** at least one rule has been born
- **THEN** damping ratio is computed as `killed_count / born_count`
- **AND** the ratio is in range `[0, 1]`

#### Scenario: Rule strength distribution
- **WHEN** queried at any timestep
- **THEN** the distribution of rule strengths (mean, std, min, max) is available

---

### Requirement: Collapse Detection
The system SHALL detect collapse events where complexity falls below a minimum threshold and remains there.

#### Scenario: Collapse condition
- **WHEN** complexity falls below `C_min` threshold
- **AND** remains below for `N` consecutive steps
- **THEN** a collapse event is recorded

#### Scenario: Collapse frequency
- **WHEN** multiple collapse events occur during a simulation
- **THEN** collapse frequency is computed as `collapse_count / total_time`

---

### Requirement: Trajectory Diversity
The system SHALL measure diversity across multiple trajectories from the same starting conditions.

#### Scenario: Trajectory storage
- **WHEN** multiple simulation runs are executed
- **THEN** state trajectories from each run are stored for comparison

#### Scenario: Diversity computation
- **WHEN** at least two trajectories are available
- **THEN** diversity at timestep `t` is computed as `mean(pairwise_L2_distance)` across all trajectory pairs

#### Scenario: Diversity interpretation
- **WHEN** diversity is very low (< ε) across all timesteps
- **THEN** the system is flagged as "deterministically locked"
- **WHEN** diversity grows unboundedly
- **THEN** the system is flagged as "chaotic"

---

### Requirement: Metrics Aggregation
The system SHALL aggregate metrics across multiple runs to produce summary statistics.

#### Scenario: Per-timestep aggregation
- **WHEN** `N` runs have completed
- **THEN** for each metric and each timestep, compute mean, std, min, max, and percentiles (5, 25, 50, 75, 95)

#### Scenario: Stability window bounds
- **WHEN** complexity traces from multiple runs are available
- **THEN** identify the complexity range `[C_min_stable, C_max_stable]` where the system operates without explosion or collapse
- **AND** report the percentage of time spent in this range

