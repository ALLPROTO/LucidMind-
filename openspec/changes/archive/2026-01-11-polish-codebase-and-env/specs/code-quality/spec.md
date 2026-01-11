## ADDED Requirements
### Requirement: Logic Deduplication
All mathematical operations and state metrics MUST be defined in a single location to prevent divergence between internal kernel state and analysis.

#### Scenario: Shared complexity metric
- **WHEN** the kernel calculates state complexity
- **AND** the stability analysis tool calculates state complexity
- **THEN** they both use the exact same implementation from `lucidmind.core.state`

### Requirement: Documentation Traceability
Every function implementing a mathematical concept or metric MUST include a link to the corresponding section in `docs/math_core.md`.

#### Scenario: Docstring audit
- **WHEN** a developer reads the docstring for a core function
- **THEN** it contains a string like `See: docs/math_core.md#[section]`
