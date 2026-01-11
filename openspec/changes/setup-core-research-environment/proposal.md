# Change: Setup Core Research Environment

## Why

LucidMind is currently in the **Core Dynamics Research Phase** where the focus is on understanding and stabilizing the self-organizing kernel dynamics before adding any semantic/text processing. The project needs a proper development environment, directory structure, and foundational infrastructure to support rigorous experimentation and metric collection.

The current `lucid_v0.py` prototype demonstrates a working self-dynamics engine with:
- Rule-based state evolution with soft gating
- Birth/death lifecycle for rules
- Complexity tracking

However, there is no formal project structure, dependency management, or experimental framework to systematically study the kernel behavior.

## What Changes

- **Add conda environment configuration** (`environment.yml`) for reproducible Python environment with NumPy, SciPy, Matplotlib, and analysis tools
- **Establish source code directory structure** under `src/lucidmind/` with modular organization
- **Create core module** (`src/lucidmind/core/`) containing the frozen kernel logic
- **Add configuration management** for experiment parameters
- **Create experiment runner framework** for batch experimentation
- **Add logging infrastructure** for metric collection
- **Update project.md** with conda usage requirements

## Impact

- **Affected specs**: New `research-environment` capability
- **Affected code**: Creates new `src/`, adds `environment.yml`, updates `project.md`
- **Dependencies**: None (self-contained)
- **Breaking changes**: None
