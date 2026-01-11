## MODIFIED Requirements
### Requirement: Conda Mandate
All development and execution MUST use the conda environment. Direct `pip install` outside conda or the use of local virtual environments (e.g., `.venv`) is strictly prohibited to ensure environment consistency.

#### Scenario: Environment check
- **WHEN** a script is executed outside the conda environment
- **THEN** a warning or error is raised indicating conda activation is required

#### Scenario: Prohibited artifacts
- **WHEN** a developer audits the workspace
- **THEN** no `.venv` or similar non-conda folders are found in the root
