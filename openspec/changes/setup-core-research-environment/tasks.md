# Tasks: Setup Core Research Environment

## 1. Environment Configuration
- [ ] 1.1 Create `environment.yml` with conda configuration (Python 3.10+, NumPy, SciPy, Matplotlib, Plotly, PyYAML)
- [ ] 1.2 Update `openspec/project.md` to mandate conda usage and add environment setup instructions
- [ ] 1.3 Add `.gitignore` entries for Python/conda artifacts

## 2. Directory Structure
- [ ] 2.1 Create `src/lucidmind/` package structure with `__init__.py`
- [ ] 2.2 Create `src/lucidmind/core/` subpackage for frozen kernel logic
- [ ] 2.3 Create `src/lucidmind/metrics/` subpackage for metric computation
- [ ] 2.4 Create `src/lucidmind/experiments/` subpackage for experiment framework
- [ ] 2.5 Create `src/lucidmind/config/` subpackage for configuration management

## 3. Core Kernel Module
- [ ] 3.1 Port `lucid_v0.py` to `src/lucidmind/core/kernel.py` (frozen logic, no modifications to dynamics)
- [ ] 3.2 Create `src/lucidmind/core/rule.py` for Rule class extraction
- [ ] 3.3 Create `src/lucidmind/core/state.py` for state management utilities
- [ ] 3.4 Add type hints and docstrings linking to `docs/math_core.md`

## 4. Configuration System
- [ ] 4.1 Create `src/lucidmind/config/defaults.py` with default experiment parameters
- [ ] 4.2 Create `src/lucidmind/config/loader.py` for YAML configuration loading
- [ ] 4.3 Create `configs/` directory with sample experiment configuration files

## 5. Experiment Framework
- [ ] 5.1 Create `src/lucidmind/experiments/runner.py` for batch experiment execution
- [ ] 5.2 Create `src/lucidmind/experiments/logger.py` for structured metric logging
- [ ] 5.3 Create `experiments/` output directory structure for results

## 6. Validation
- [ ] 6.1 Verify conda environment installs correctly on macOS
- [ ] 6.2 Verify kernel produces identical output to original `lucid_v0.py` (determinism check)
- [ ] 6.3 Run a sample batch experiment (10 runs) and confirm logging works
