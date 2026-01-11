# Capability: Stability Analysis

## ADDED Requirements

### Requirement: Stability Window Detection
The system SHALL automatically detect stability windows from experimental runs.

#### Scenario: Single run classification
- **WHEN** a simulation run completes with metrics collected
- **THEN** the run is classified as one of: STABLE, EXPLOSION, COLLAPSE, or UNSTABLE
- **AND** the classification criteria are logged

#### Scenario: Stability bounds computation
- **WHEN** multiple runs are analyzed
- **THEN** the system identifies the complexity range `[C_min_stable, C_max_stable]` where stable operation occurs
- **AND** reports the percentage of timesteps within this range

#### Scenario: Stability report generation
- **WHEN** a stability analysis completes
- **THEN** a structured report is generated with:
  - Classification result
  - Time in stable region (percentage)
  - Explosion condition triggers (if any)
  - Damping ratio statistics
  - Recommendations

---

### Requirement: Phase Diagram Generation
The system SHALL generate phase diagrams showing stability classification across parameter combinations.

#### Scenario: 2D parameter sweep
- **WHEN** two parameters, their ranges, and step counts are specified
- **THEN** experiments are run at each grid point
- **AND** each point is classified (STABLE/EXPLOSION/COLLAPSE/UNSTABLE)

#### Scenario: Phase diagram visualization
- **WHEN** a 2D sweep completes
- **THEN** a heatmap is generated with color-coded classifications
- **AND** stability boundaries are clearly visible

#### Scenario: Phase diagram export
- **WHEN** a phase diagram is generated
- **THEN** the underlying data is exportable as CSV or JSON
- **AND** the visualization is exportable as PNG and SVG

---

### Requirement: Rule Lifecycle Analysis
The system SHALL analyze rule lifecycle patterns to identify characteristics of healthy vs parasitic rules.

#### Scenario: Lifespan distribution
- **WHEN** a simulation with rule tracking completes
- **THEN** the distribution of rule lifespans is computed
- **AND** statistics (mean, median, std, percentiles) are reported

#### Scenario: Rule characterization
- **WHEN** rule lifecycle data is available
- **THEN** each rule is characterized by:
  - Lifespan (steps from birth to death)
  - Peak strength achieved
  - Net contribution to complexity reduction

#### Scenario: Healthy rule identification
- **WHEN** rules are characterized
- **THEN** "healthy" rules are identified as those with:
  - Lifespan > median
  - Peak strength > threshold
  - Positive complexity contribution

#### Scenario: Parasitic rule identification
- **WHEN** rules are characterized
- **THEN** "parasitic" rules are identified as those with:
  - Lifespan < 10% of median
  - Low peak strength
  - Zero or negative complexity contribution

#### Scenario: Damping ratio analysis
- **WHEN** rule birth/death events are tracked
- **THEN** damping ratio (killed/born) is computed over time
- **AND** periods of healthy (0.3-0.9) and unhealthy damping are identified

---

### Requirement: Recovery Time Measurement
The system SHALL measure the system's ability to recover from perturbations.

#### Scenario: Perturbation injection
- **WHEN** a perturbation magnitude ε and component index i are specified
- **THEN** the perturbation `ε * e_i` is added to the current state
- **AND** both perturbed and baseline trajectories continue

#### Scenario: Recovery detection
- **WHEN** a perturbed trajectory is compared to baseline
- **THEN** recovery time is computed as the first timestep where distance < δ
- **OR** recovery time is marked as ∞ if never recovered within N steps

#### Scenario: Recovery classification
- **WHEN** recovery analysis completes
- **THEN** the response is classified as:
  - RECOVERED (distance < δ achieved)
  - DIVERGED (distance grew unboundedly)
  - COLLAPSED (perturbed trajectory collapsed)

#### Scenario: Recovery time distribution
- **WHEN** multiple perturbation magnitudes are tested
- **THEN** recovery time vs perturbation magnitude is plotted
- **AND** the critical perturbation threshold (beyond which no recovery) is identified

---

### Requirement: Visualization Module
The system SHALL provide visualization tools for analysis results.

#### Scenario: Complexity trace plot
- **WHEN** complexity history is available
- **THEN** a time series plot is generated
- **AND** stability bounds are shown as horizontal lines
- **AND** explosion/collapse events are marked

#### Scenario: Entropy trace plot
- **WHEN** entropy history is available
- **THEN** a time series plot is generated with drift annotations
- **AND** entropy lock warnings are highlighted

#### Scenario: Multi-run overlay
- **WHEN** multiple runs are available
- **THEN** traces can be overlaid with mean ± std bands

#### Scenario: Rule timeline
- **WHEN** rule lifecycle data is available
- **THEN** a timeline visualization shows rule births, deaths, and strengths
- **AND** rule classification (healthy/parasitic) is color-coded

#### Scenario: Summary dashboard
- **WHEN** a full analysis completes
- **THEN** a single figure combines:
  - Complexity trace with bounds
  - Entropy trace
  - Rule lifecycle summary
  - Classification result

---

### Requirement: Parameter Sweep Framework
The system SHALL support systematic parameter exploration.

#### Scenario: 1D sweep
- **WHEN** a single parameter, range, and step count are specified
- **THEN** experiments are run at each value
- **AND** metrics are plotted as a function of the parameter

#### Scenario: 2D sweep
- **WHEN** two parameters are specified
- **THEN** experiments are run on the Cartesian product grid
- **AND** results are available as a 2D array

#### Scenario: Sweep configuration
- **WHEN** a sweep is defined
- **THEN** configuration includes:
  - Parameter name(s) and ranges
  - Number of runs per point
  - Metrics to collect
  - Output directory

#### Scenario: Parallel execution
- **WHEN** parallel execution is enabled
- **THEN** sweep points are distributed across available cores
- **AND** results are correctly aggregated
