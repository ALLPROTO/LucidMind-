## 1. Environment Cleanup
- [x] 1.1 Remove `.venv` directory from workspace.
- [x] 1.2 Update `environment.yml`: remove `pip:` section and move `autograd` to dependencies.
- [x] 1.3 Update `setup.py` to match `environment.yml`.
- [x] 1.4 Remove `prototype/placeholder.md` (extra code/file).
- [x] 1.5 Verify environment can be recreated fresh without `pip` errors.

## 2. Code Deduplication
- [x] 2.1 Identify all instances of `complexity` and `entropy` math in `src/lucidmind/metrics/`.
- [x] 2.2 Refactor `src/lucidmind/metrics/complexity.py` to import `complexity` from `lucidmind.core.state`.
- [x] 2.3 Refactor `src/lucidmind/metrics/entropy.py` to import `entropy` from `lucidmind.core.state`.
- [x] 2.4 Unify `damping_ratio` calculation between `Kernel.get_stats` and `src/lucidmind/metrics/rules.py`.

## 3. Style and Polish
- [x] 3.1 Fix step numbering in `src/lucidmind/core/kernel.py` (add step 8, adjust sequence).
- [x] 3.2 Ensure all core and metrics functions have docstrings with links to `docs/math_core.md`.
- [x] 3.3 Ensure consistent type hinting across all modified files.

## 4. Documentation and Specs
- [x] 4.1 Update `openspec/specs/research-environment/spec.md` with new requirements.
- [x] 4.2 Create `openspec/specs/code-quality/spec.md` (will be archived later).
