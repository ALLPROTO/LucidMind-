## Context
The project aims for high scientific rigor. Previous issues with `pip_require_venv` inside Conda environments suggest that mixing package managers is causing friction. Additionally, duplicate math logic increases the risk of divergence between internal kernel state and external analysis.

## Goals / Non-Goals
- **Goals**:
  - Pure Conda environment (no `pip` section in `environment.yml`).
  - Zero duplicate math code for state analysis.
  - Consistent docstrings with math references.
  - Verification of environment safety.
- **Non-Goals**:
  - Changing the core kernel logic (logic is frozen).
  - Adding new metrics (staying within cleanup scope).

## Decisions
- **Decision**: Authoritative math logic will reside in `src/lucidmind/core/state.py`.
  - **Rationale**: The kernel depends on this for its transition function, so it must be close to the core. Metrics should be "observations" of these core properties.
- **Decision**: Prohibit `.venv` explicitly in `research-environment` spec.
  - **Rationale**: To prevent confusion and ensure consistent library resolution across researcher machines.

## Risks / Trade-offs
- **Risk**: Moving `autograd` to conda-forge might fail if the channel is not correctly configured.
  - **Mitigation**: Ensure `conda-forge` is high priority in `environment.yml`.
