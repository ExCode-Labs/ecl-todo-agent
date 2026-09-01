# Todo Agent

Agentic AI backend service for the Todo application.

This service provides the foundation for natural-language and voice-driven Todo operations. It is responsible for interpreting user commands, orchestrating Agentic AI workflows, and interacting with the Todo backend through controlled APIs.

> **Status:** Initial project setup. Agent workflows and Todo tools are under development.

---

## Tech Stack

### Runtime & API

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic v2
- Pydantic Settings
- AsyncIO

### Agentic AI

- LangChain
- LangGraph
- LLM provider integration

### Development & Quality

- uv — Python package and environment management
- Ruff — Linting and formatting
- mypy — Static type checking
- pytest — Testing
- pytest-asyncio — Async test support
- pytest-cov — Test coverage
- pip-audit — Dependency security auditing
- pre-commit — Git hooks
- Commitizen — Conventional Commit validation
- Poe the Poet — Development task runner

---

## Project Architecture

The service follows a `src` package layout:

```text
todo-agent/
│
├── src/
│   └── todo_agent/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── commitlint.config.js
├── Makefile
├── pyproject.toml
├── README.md
└── uv.lock
```

The application code is located under:

```text
src/todo_agent/
```

Tests are located under:

```text
tests/
```

---

## Prerequisites

Install the following before setting up the project:

- Python 3.13+
- Git
- uv

Verify Python:

```bash
python --version
```

Verify Git:

```bash
git --version
```

Verify uv:

```bash
uv --version
```

---

## Project Setup

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
```

Navigate to the project:

```bash
cd todo-agent
```

---

### 2. Install the Python environment

The project uses `uv` for dependency and virtual-environment management.

Run:

```bash
uv sync
```

This will:

- Create the virtual environment if required
- Install project dependencies
- Install development dependencies
- Use `uv.lock` for reproducible dependency versions

---

### 3. Activate the virtual environment

#### Git Bash

```bash
source .venv/Scripts/activate
```

#### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Activation is optional when using `uv run`, because `uv` automatically executes commands inside the project environment.

---

## Environment Configuration

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Never commit `.env` to Git.

Secrets and environment-specific configuration should be supplied through environment variables or the deployment platform's secret manager.

---

## Start the Application

### Development

Start FastAPI with Uvicorn and automatic reload:

```bash
uv run poe dev
```

The API will be available at:

```text
http://localhost:8000
```

### API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

### Production-style start

```bash
uv run poe start
```

---

## Development Commands

The project uses **Poe the Poet** as the task runner.

### Start development server

```bash
uv run poe dev
```

### Start application

```bash
uv run poe start
```

### Run tests

```bash
uv run poe test
```

### Format code

```bash
uv run poe format
```

### Check formatting

```bash
uv run poe format-check
```

### Run linting

```bash
uv run poe lint
```

### Automatically fix lint issues

```bash
uv run poe lint-fix
```

### Run type checking

```bash
uv run poe typecheck
```

### Run dependency security audit

```bash
uv run poe audit
```

### Run all quality checks

```bash
uv run poe check
```

The `check` command runs:

```text
Ruff lint
    ↓
Ruff format check
    ↓
mypy
    ↓
pytest
    ↓
pip-audit
```

All checks should pass before creating a pull request.

---

## Pre-commit Hooks

Install the Git hooks after cloning the repository:

```bash
uv run pre-commit install --hook-type pre-commit --hook-type commit-msg
```

Run all configured hooks manually:

```bash
uv run pre-commit run --all-files
```

Pre-commit is responsible for fast local checks such as:

- Ruff linting
- Ruff formatting
- mypy
- Conventional Commit validation

---

## Commit Convention

This project follows the **Conventional Commits** specification.

Valid examples:

```text
feat: add todo agent
fix: handle invalid agent command
docs: update project setup
test: add welcome endpoint tests
refactor: simplify agent service
chore: update dependencies
ci: add quality pipeline
build: configure application container
perf: optimize agent execution
```

Invalid:

```text
feat add todo agent
```

Valid:

```text
feat: add todo agent
```

Commitizen can be used to create commits interactively:

```bash
uv run cz commit
```

---

## Testing

Tests are written using pytest.

Run the test suite:

```bash
uv run poe test
```

Run tests with coverage:

```bash
uv run pytest --cov
```

Test files should be placed under:

```text
tests/
```

Example:

```text
tests/
├── test_main.py
├── unit/
├── integration/
└── e2e/
```

---

## Code Quality

Before pushing changes, run:

```bash
uv run poe check
```

The command validates:

1. Ruff linting
2. Ruff formatting
3. mypy type checking
4. pytest
5. pip-audit

Do not bypass failing quality checks unless there is a documented reason.

---

## Dependency Management

Add a production dependency:

```bash
uv add <package>
```

Example:

```bash
uv add httpx
```

Add a development dependency:

```bash
uv add --dev <package>
```

Example:

```bash
uv add --dev pytest
```

Synchronize the environment:

```bash
uv sync
```

Update dependencies when required:

```bash
uv lock --upgrade
```

The `uv.lock` file must be committed to the repository to maintain reproducible environments.

---

## CI/CD

GitHub Actions runs automated quality checks for pushes and pull requests targeting the primary development branches.

The CI pipeline validates:

```text
Checkout
   ↓
Install uv
   ↓
Install Python
   ↓
uv sync --locked
   ↓
Ruff
   ↓
Formatting
   ↓
mypy
   ↓
pytest
   ↓
pip-audit
```

A pull request should not be merged while required CI checks are failing.

---

## Security

Do not commit sensitive values such as:

- API keys
- Database credentials
- LLM provider credentials
- Service-to-service authentication keys
- Access tokens
- Private certificates

Use:

```text
.env
```

for local development and your deployment platform's secret-management mechanism for production.

Dependency vulnerabilities can be checked with:

```bash
uv run poe audit
```

---

## Current API

The initial application exposes a welcome endpoint:

```http
GET /
```

Example response:

```json
{
  "message": "Welcome to Todo Agent API"
}
```

---

## Future Agent Architecture

The Agentic AI service will eventually follow this flow:

```text
                    User Command
                         │
                         ▼
                  FastAPI Endpoint
                         │
                         ▼
                   Agent Workflow
                    (LangGraph)
                         │
                         ▼
                  LLM / Reasoning
                         │
                         ▼
                    Tool Selection
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Todo Backend            User Input
              │                / Confirmation
              ▼
        Todo Operations
```

The Agent service will **not directly access PostgreSQL**.

The expected service boundary is:

```text
todo-agent
     │
     │ HTTP
     ▼
todo-backend
     │
     ▼
Prisma
     │
     ▼
PostgreSQL
```

This keeps Todo business logic and database access centralized in the Todo backend.

---

## Branching Strategy

Recommended branches:

```text
main
  └── Production

develop
  └── Integration / UAT

feature/*
  └── Feature development

bugfix/*
  └── Bug fixes

release/*
  └── Release preparation
```

Feature branches should be created from `develop` and merged through pull requests.

---

## Development Workflow

Typical developer workflow:

```bash
# Get latest changes
git pull

# Install/synchronize dependencies
uv sync

# Create a feature branch
git checkout -b <jira-ticket-id>

# Implement changes

# Format
uv run poe format

# Lint
uv run poe lint-fix

# Type check
uv run poe typecheck

# Run tests
uv run poe test

# Run complete validation
uv run poe check

# Commit
uv run cz commit

# Push
git push
```

---

## License

This project is currently maintained as an internal application/service.

Add the appropriate license information when the project is intended for external distribution.