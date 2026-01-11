# Project Context

## Purpose
LucidMind is a non-statistical artificial intelligence framework based on deterministic state evolution within a structured state space. Unlike modern neural networks, it does not rely on training, datasets, or optimization. Instead, it generates reasoning through the geometric properties of a task-induced functional. The project aims to provide a mathematically interpretable and inherently safe alternative to statistical AI.

## Tech Stack
- **Language:** Python 3.10+ (preferred for numerical modeling and simulation).
- **Core Libraries:**
  - `NumPy`/`SciPy`: High-performance numerical computation and matrix operations.
  - `Autograd` or `JAX`: For automatic differentiation of task functionals $h(x)$.
  - `Matplotlib`/`Plotly`: For visualizing state trajectories and topological manifolds.
- **Documentation:** Markdown with KaTeX/MathJax for formal mathematical notation.

## Project Conventions

### Code Style
- **Naming:** Follow mathematical conventions from the theory (e.g., `x` for state, `h` for functional, `g` for gradient, `F` for operator).
- **Typing:** Use Python type hints (e.g., `numpy.ndarray`) for clarity in numerical code.
- **Docstrings:** Every function implementing a mathematical concept MUST link to the corresponding section in `docs/math_core.md`.

### Architecture Patterns
- **Functional Core:** Implement the transition operator $F(x)$ as a pure function where possible.
- **State Isolation:** Maintain strict separation between the system state $x_t$ and the task definition $h(x)$.
- **Safety Wrappers:** All state updates MUST pass through a validation layer that checks Zero-Divergence Core (ZDC) constraints.

### Testing Strategy
- **Numerical Validation:** Use property-based testing to verify Lipschitz continuity and boundedness of $F(x)$.
- **Convergence Tests:** Verify that state trajectories in Low-Gradient Stability Fields (LSF) converge to fixed points.
- **Inertia Tests:** Ensure states in the Non-Actionable Domain (NAD) remains static.

### Git Workflow
- **Branching:** Use `main` for stable theory/documentation and `feature/` branches for prototype implementations.
- **Commits:** Convention: `feat:`, `fix:`, `docs:`, `math:`, `refactor:`.

## Domain Context
- **State Space ($\mathcal{X}$):** A finite-dimensional manifold where reasoning occurs as motion.
- **Task Functional ($h$):** A scalar field defining the "geometry" of the problem.
- **Non-Statistical:** Explicitly avoid any probabilistic sampling or parameter optimization (learning).

## Important Constraints
- **ZDC Constraint:** $\nabla \cdot F(x) = 0$ is a non-negotiable safety requirement.
- **Determinism:** The transition $x_{t+1} = x_t + F(x_t)$ must be perfectly reproducible.
- **Resource Efficiency:** The architecture should run on standard CPU hardware without requiring GPUs for core reasoning.

## External Dependencies
- None at this stage; prioritizing a self-contained numerical engine.
