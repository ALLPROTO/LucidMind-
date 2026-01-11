# Tasks: Add Core Metrics Instrumentation

## 1. Core State Metrics
- [x] 1.1 Create `src/lucidmind/metrics/complexity.py` with configurable complexity calculation
- [x] 1.2 Create `src/lucidmind/metrics/entropy.py` with state entropy computation
- [x] 1.3 Add entropy drift calculation (delta between consecutive timesteps)
- [x] 1.4 Add complexity trace logging (full history per run)

## 2. Explosion Detection
- [x] 2.1 Implement E1: Unbounded Growth detection (exponential complexity)
- [x] 2.2 Implement E2: Entropy Lock detection (constant high entropy)
- [x] 2.3 Implement E3: Rule Saturation detection (rules never die)
- [x] 2.4 Implement E4: Irreversible Sensitivity detection (large response to small perturbation)
- [x] 2.5 Create `src/lucidmind/metrics/explosion.py` with unified explosion checker

## 3. Rule Lifecycle Metrics
- [x] 3.1 Create `src/lucidmind/metrics/rules.py` for rule lifecycle tracking
- [x] 3.2 Add birth count, death count, and current alive count
- [x] 3.3 Compute damping ratio: `killed / born`
- [x] 3.4 Track rule strength distribution over time

## 4. Collapse Detection
- [x] 4.1 Define collapse condition (complexity drops below threshold and stays)
- [x] 4.2 Implement collapse event detection
- [x] 4.3 Track collapse frequency: `collapses / time`
- [x] 4.4 Create `src/lucidmind/metrics/collapse.py`

## 5. Trajectory Analysis (Multi-run)
- [x] 5.1 Create `src/lucidmind/metrics/trajectory.py` for trajectory storage
- [x] 5.2 Implement pairwise trajectory distance calculation
- [x] 5.3 Compute trajectory diversity: `mean(pairwise_distance)`
- [x] 5.4 Add trajectory statistics (mean, std, range per timestep)

## 6. Metrics Aggregation
- [x] 6.1 Create `src/lucidmind/metrics/aggregator.py` for multi-run statistics
- [x] 6.2 Implement per-timestep aggregation (mean, std, min, max, percentiles)
- [x] 6.3 Create summary statistics for full experiment (stability window bounds)

## 7. Validation
- [x] 7.1 Unit tests for each metric function
- [x] 7.2 Verify entropy calculation matches theoretical definition
- [x] 7.3 Verify explosion detection triggers on synthetic edge cases
- [x] 7.4 Integration test: run 10 runs and confirm all metrics collected
