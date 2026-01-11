# Tasks: Add Core Metrics Instrumentation

## 1. Core State Metrics
- [ ] 1.1 Create `src/lucidmind/metrics/complexity.py` with configurable complexity calculation
- [ ] 1.2 Create `src/lucidmind/metrics/entropy.py` with state entropy computation
- [ ] 1.3 Add entropy drift calculation (delta between consecutive timesteps)
- [ ] 1.4 Add complexity trace logging (full history per run)

## 2. Explosion Detection
- [ ] 2.1 Implement E1: Unbounded Growth detection (exponential complexity)
- [ ] 2.2 Implement E2: Entropy Lock detection (constant high entropy)
- [ ] 2.3 Implement E3: Rule Saturation detection (rules never die)
- [ ] 2.4 Implement E4: Irreversible Sensitivity detection (large response to small perturbation)
- [ ] 2.5 Create `src/lucidmind/metrics/explosion.py` with unified explosion checker

## 3. Rule Lifecycle Metrics
- [ ] 3.1 Create `src/lucidmind/metrics/rules.py` for rule lifecycle tracking
- [ ] 3.2 Add birth count, death count, and current alive count
- [ ] 3.3 Compute damping ratio: `killed / born`
- [ ] 3.4 Track rule strength distribution over time

## 4. Collapse Detection
- [ ] 4.1 Define collapse condition (complexity drops below threshold and stays)
- [ ] 4.2 Implement collapse event detection
- [ ] 4.3 Track collapse frequency: `collapses / time`
- [ ] 4.4 Create `src/lucidmind/metrics/collapse.py`

## 5. Trajectory Analysis (Multi-run)
- [ ] 5.1 Create `src/lucidmind/metrics/trajectory.py` for trajectory storage
- [ ] 5.2 Implement pairwise trajectory distance calculation
- [ ] 5.3 Compute trajectory diversity: `mean(pairwise_distance)`
- [ ] 5.4 Add trajectory statistics (mean, std, range per timestep)

## 6. Metrics Aggregation
- [ ] 6.1 Create `src/lucidmind/metrics/aggregator.py` for multi-run statistics
- [ ] 6.2 Implement per-timestep aggregation (mean, std, min, max, percentiles)
- [ ] 6.3 Create summary statistics for full experiment (stability window bounds)

## 7. Validation
- [ ] 7.1 Unit tests for each metric function
- [ ] 7.2 Verify entropy calculation matches theoretical definition
- [ ] 7.3 Verify explosion detection triggers on synthetic edge cases
- [ ] 7.4 Integration test: run 100 experiments and confirm all metrics collected
