# Change: Polish codebase and environment consistency

## Why
The project currently has minor duplicate logic (state math), inconsistent environment configurations (pip vs conda), and prohibited artifacts (.venv) that hinder stability and researcher workflow. Consolidating logic and enforcing a pure Conda environment ensures reproducibility.

## What Changes
- **MODIFIED** `research-environment`: Stricter conda enforcement, prohibit `.venv`.
- **ADDED** `code-quality`: Define standards for deduplication and docstrings.
- **Environment**: Update `environment.yml` to remove `pip`-contained dependencies; sync `setup.py`.
- **Cleanup**: Delete `.venv`.
- **Deduplication**: Move shared math (complexity, entropy) to a single location used by both core and metrics.
- **Polish**: Fix numbering and docstring links in `src/lucidmind/core/kernel.py`.

## Impact
- Affected specs: `specs/research-environment/spec.md`, `specs/code-quality/spec.md` (new).
- Affected code: `src/lucidmind/core/kernel.py`, `src/lucidmind/core/state.py`, `src/lucidmind/metrics/`, `environment.yml`, `setup.py`.
