# Capability: Research Environment

## ADDED Requirements

### Requirement: Conda Environment Configuration
The system SHALL provide a conda environment specification (`environment.yml`) that installs all required dependencies for core dynamics research.

#### Scenario: Fresh environment setup
- **WHEN** a developer clones the repository
- **AND** runs `conda env create -f environment.yml`
- **THEN** a working Python environment is created with all required packages

#### Scenario: Environment activation
- **WHEN** a developer runs `conda activate lucidmind`
- **THEN** the environment is active with Python 3.10+ and all dependencies available

---

### Requirement: Frozen Core Kernel
The system SHALL maintain the core kernel dynamics (`src/lucidmind/core/`) as read-only during the research phase, with any modifications requiring explicit approval.

#### Scenario: Kernel output consistency
- **WHEN** the ported kernel is executed with a fixed random seed
- **THEN** the output matches the original `lucid_v0.py` exactly (determinism)

#### Scenario: Kernel isolation
- **WHEN** metrics or experiments are added
- **THEN** the core kernel module remains unchanged

---

### Requirement: Modular Source Structure
The system SHALL organize source code under `src/lucidmind/` with distinct subpackages for core dynamics, metrics, experiments, and configuration.

#### Scenario: Package importability
- **WHEN** the conda environment is active
- **AND** the package is installed (`pip install -e .`)
- **THEN** imports like `from lucidmind.core import Kernel` work correctly

---

### Requirement: Configuration Management
The system SHALL support YAML-based configuration for experiment parameters with type-safe defaults.

#### Scenario: Default configuration usage
- **WHEN** no configuration file is specified
- **THEN** the system uses default parameters from `src/lucidmind/config/defaults.py`

#### Scenario: Custom configuration override
- **WHEN** a YAML configuration file is provided
- **THEN** specified parameters override defaults while unspecified parameters use defaults

---

### Requirement: Experiment Runner Framework
The system SHALL provide an experiment runner that executes batch experiments with different random seeds and logs results.

#### Scenario: Batch experiment execution
- **WHEN** an experiment is configured with `n_runs=100` and `seed_start=42`
- **THEN** 100 independent runs are executed with seeds 42, 43, ..., 141
- **AND** results are logged to the experiments output directory

#### Scenario: Structured logging
- **WHEN** an experiment completes
- **THEN** metrics are saved in a structured format (JSON or CSV) with timestamp and configuration metadata

---

### Requirement: Conda Mandate
All development and execution MUST use the conda environment. Direct `pip install` outside conda is prohibited for core dependencies.

#### Scenario: Environment check
- **WHEN** a script is executed outside the conda environment
- **THEN** a warning or error is raised indicating conda activation is required
