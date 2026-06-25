# 30-Day Python Course — Project Context

---

## 📄 Documentation Generation Instructions

**Format:** PDF (using Python `reportlab` library — NOT Word/docx)

When the user asks to generate documentation for any day's session, always produce a **PDF file** using `reportlab`. Do not create `.docx` files unless explicitly asked.

### Standard PDF structure for each day's documentation:
1. **Title Page** — Day number, topic, session length, phase badge, stats card
2. **Session Overview** — Goal, outcome, timeline table (minute-by-minute), instructor note
3. **Prerequisites & Preparation** — Requirements table + instructor pre-session checklist
4. **Step-by-Step Instruction Guide** — Each step with: "What to Say" script, dark-themed code blocks, OS-specific commands (macOS / Windows / Linux), common errors table, green verification box
5. **Session Wrap-Up** — Student checklist, key concepts recap, next day preview, troubleshooting notes
6. **Quick Reference Card** — Daily workflow commands, VS Code shortcuts, tool summary

### PDF styling conventions:
- **Library:** `reportlab` — install with `pip install reportlab --break-system-packages`
- **Page size:** US Letter (`from reportlab.lib.pagesizes import letter`)
- **Margins:** 0.75 inch all sides
- **Colors:** Navy `#1E3A5F` headings, Blue `#2563EB` accents, dark code blocks `#1E293B`
- **Code blocks:** Dark background (`#1E293B`), yellow `#FDE68A` for commands, green `#4ADE80` for output, gray `#94A3B8` for comments
- **Info boxes:** Blue for tips, green for "Done When", amber for warnings
- **Section banners:** Navy background full-width bars between steps
- **Header/Footer:** Skip header on page 1; all pages get footer with page number

### Output path:
`/mnt/user-data/outputs/Day{N}_Python_Course_Documentation.pdf`

---

## Course Overview

| Detail | Value |
|--------|-------|
| Total Duration | 30 days |
| Daily Commitment | 2 hours/day |
| Total Hours | 60 hours |
| Format | Self-paced, structured phases |

---

## Phase Breakdown

| Phase | Days | Hours |
|-------|------|-------|
| Setup & Installation | Day 1 | 2 hrs |
| Beginner | Days 2–6 | 10 hrs |
| Intermediate | Days 7–16 | 20 hrs |
| Advanced | Days 17–25 | 18 hrs |
| Capstone Project | Days 26–30 | 10 hrs |

---

## Phase 1 — Setup & Installation
**Day 1 · 2 hours**

Get your full development environment ready before writing a single line of Python.

### Day 1 — Environment Setup
- Python 3.12 installation
- `uv` package manager (modern replacement for pip + virtualenv)
- VS Code installation
- Essential VS Code extensions (Python, Pylance, Ruff, GitLens)
- Creating and activating a virtual environment with `uv`
- Running your first Hello World script

---

## Phase 2 — Beginner
**Days 2–6 · 10 hours**

Cover all core Python fundamentals. By the end of this phase you can write functional scripts that take input, make decisions, repeat tasks, and store data.

### Day 2 — Variables & Data Types
- `int`, `float`, `str`, `bool`
- `type()` function
- `input()` and `print()`
- Type casting (`int()`, `str()`, `float()`)

### Day 3 — Control Flow
- `if` / `elif` / `else`
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators (`and`, `or`, `not`)
- Nested conditions
- `match` statement (Python 3.10+)

### Day 4 — Loops
- `for` loop
- `while` loop
- `range()`
- `break` / `continue` / `pass`
- `else` on loops

### Day 5 — Functions & Scope
- Defining functions with `def`
- Parameters and arguments
- Return values
- Default arguments
- `*args` and `**kwargs`
- Scope and the LEGB rule (Local, Enclosing, Global, Built-in)

### Day 6 — Data Structures
- Lists — creation, mutation, methods
- Tuples — immutability, packing/unpacking
- Dictionaries — key-value pairs, methods
- Sets — unique collections, set operations
- List/dict/set comprehensions
- Slicing syntax

---

## Phase 3 — Intermediate
**Days 7–16 · 20 hours**

Go deeper into Python. This phase covers the patterns and tools that separate beginner scripts from real programs — file handling, OOP, decorators, and more.

### Day 7 — Strings & String Methods
- String formatting
- f-strings
- `split()` / `join()`
- `strip()` / `replace()`
- `re` module basics (search, match, findall)

### Day 8 — File I/O
- `open()` / `close()`
- Reading, writing, and appending files
- `with` statement (context manager)
- `csv` module — reading and writing CSV
- `json` module — parsing and serializing JSON

### Day 9 — Error Handling
- `try` / `except` / `else` / `finally`
- `raise` — throwing exceptions manually
- Creating custom exception classes
- Logging basics with the `logging` module

### Day 10 — Object-Oriented Programming I
- Classes and objects
- `__init__` constructor
- `self` keyword
- Instance variables vs class variables
- Instance methods

### Day 11 — Object-Oriented Programming II
- Inheritance and `super()`
- Polymorphism
- Encapsulation (name mangling, properties)
- Dunder (magic) methods — `__str__`, `__repr__`, `__len__`, `__eq__`

### Day 12 — Modules & Packages
- `import` and `from ... import`
- Installing packages with `pip` / `uv add`
- `__main__` guard
- Standard library modules — `os`, `sys`, `math`, `datetime`, `pathlib`

### Day 13 — Iterators & Generators
- `__iter__` and `__next__` protocol
- `yield` keyword
- Generator expressions
- `itertools` module — `chain`, `islice`, `product`, `cycle`

### Day 14 — Decorators & Closures
- First-class functions
- Closures and free variables
- Writing a `@decorator` from scratch
- `functools.wraps`
- Built-in decorators — `@staticmethod`, `@classmethod`, `@property`

### Day 15 — Functional Programming
- `map()` / `filter()` / `reduce()`
- `lambda` expressions
- `zip()` / `enumerate()`
- `sorted()` with `key=`

### Day 16 — Concurrency Basics
- `threading` module
- `multiprocessing` module
- `async` / `await` syntax
- `asyncio.run()` — running coroutines

---

## Phase 4 — Advanced
**Days 17–25 · 18 hours**

Professional-level Python. This phase prepares you to write production-quality code — typed, tested, documented, and deployable.

### Day 17 — Advanced OOP
- Abstract base classes with `ABCMeta`
- Metaclasses
- `Protocol` classes (structural subtyping)
- `@dataclass` decorator

### Day 18 — Type Hints & Static Analysis
- Type hints for variables, functions, and return types
- `mypy` for static type checking
- `Optional` and `Union` types
- `TypeVar` and generics

### Day 19 — Context Managers
- The `with` protocol (`__enter__` / `__exit__`)
- `contextlib` module
- Writing custom context managers
- `@contextmanager` decorator

### Day 20 — Testing
- `unittest` — test cases and test suites
- `pytest` — test discovery, assertions, parametrize
- Fixtures
- Mocking with `unittest.mock`
- Coverage reports
- Test-driven development (TDD) intro

### Day 21 — Data & NumPy
- NumPy arrays vs Python lists
- Broadcasting rules
- Vectorized operations
- Array slicing and indexing
- `np.linalg` — linear algebra basics

### Day 22 — Data & Pandas
- `DataFrame` and `Series` objects
- `read_csv()` and `to_csv()`
- `groupby()` aggregations
- `merge()` and `join()`
- Basic plotting with `df.plot()`

### Day 23 — Web Requests & APIs
- `requests` library — GET, POST, headers, params
- REST API concepts
- JSON response parsing
- Authentication headers (Bearer, API key)
- `httpx` — async HTTP client

### Day 24 — Web Framework — FastAPI
- Defining routes and path parameters
- Query parameters and request bodies
- Pydantic models for validation
- Async endpoints
- Auto-generated Swagger UI (`/docs`)

### Day 25 — Databases & Packaging
- SQLite with the `sqlite3` module
- SQLAlchemy ORM — models, sessions, CRUD
- Database migrations basics
- `pyproject.toml` structure
- Building a package with `uv build`
- Docker basics — Dockerfile, image, container

---

## Phase 5 — Capstone Project
**Days 26–30 · 10 hours**

One complete project built end-to-end. All five days are dedicated to a single application that brings together everything from the course — OOP, FastAPI, databases, CLI, testing, and deployment.

---

### Capstone Project — Full-Stack Task Manager API

**Stack:** Python 3.12 · FastAPI · SQLAlchemy · SQLite · Typer CLI · Pandas · Pytest · Docker

**What you will build:** A command-line + REST API task management application. Users can create, read, update, and delete tasks via both a CLI and HTTP endpoints. The app includes a Pandas-powered analytics layer that reports task completion rates and exports summaries to CSV.

---

### Day 26 — Planning & Architecture
- Write the requirements specification
- Design the Entity Relationship Diagram (ERD)
- Scaffold the project folder structure
- Set up the `uv` environment and `pyproject.toml`
- Initialise Git repository with `.gitignore`

**Deliverable:** Clean project scaffold committed to Git.

---

### Day 27 — Core Backend
- Build the FastAPI application
- Define SQLAlchemy models (`Task`, `Category`)
- Implement all CRUD endpoints (Create, Read, Update, Delete)
- Write Pydantic schemas for request/response validation
- Add proper error handling (404, 422 responses)

**Deliverable:** Working REST API with full CRUD, testable via Swagger UI at `/docs`.

---

### Day 28 — CLI & Data Layer
- Build the CLI interface with `Typer`
- Commands — `add`, `list`, `complete`, `delete`, `export`
- Implement CSV export with the `csv` module
- Build Pandas analytics — completion rate, tasks by category, overdue report
- Rich terminal output using the `rich` library

**Deliverable:** Fully functional CLI that interacts with the same SQLite database as the API.

---

### Day 29 — Testing & Refinement
- Write a `pytest` test suite covering all endpoints
- Create fixtures for a test database (in-memory SQLite)
- Mock external dependencies
- Run coverage report — aim for 80%+ coverage
- Code review pass — refactor for clarity and consistency

**Deliverable:** Full test suite with coverage report, clean codebase.

---

### Day 30 — Deploy & Portfolio
- Write the `Dockerfile` and `.dockerignore`
- Build and run the Docker container locally
- Deploy to Render or Railway (free tier)
- Write a professional `README.md` — setup instructions, API docs, screenshots
- Push to GitHub portfolio
- Record a short demo video (optional)

**Deliverable:** Live deployed application + polished GitHub repository ready for your portfolio.

---

## Full 30-Day Schedule at a Glance

| Day | Phase | Topic |
|-----|-------|-------|
| 01 | Setup | Environment setup — Python, uv, VS Code |
| 02 | Beginner | Variables & data types |
| 03 | Beginner | Control flow |
| 04 | Beginner | Loops |
| 05 | Beginner | Functions & scope |
| 06 | Beginner | Data structures |
| 07 | Intermediate | Strings & string methods |
| 08 | Intermediate | File I/O |
| 09 | Intermediate | Error handling |
| 10 | Intermediate | OOP I — classes & objects |
| 11 | Intermediate | OOP II — inheritance & dunder methods |
| 12 | Intermediate | Modules & packages |
| 13 | Intermediate | Iterators & generators |
| 14 | Intermediate | Decorators & closures |
| 15 | Intermediate | Functional programming |
| 16 | Intermediate | Concurrency basics |
| 17 | Advanced | Advanced OOP |
| 18 | Advanced | Type hints & static analysis |
| 19 | Advanced | Context managers |
| 20 | Advanced | Testing |
| 21 | Advanced | Data & NumPy |
| 22 | Advanced | Data & Pandas |
| 23 | Advanced | Web requests & APIs |
| 24 | Advanced | Web framework — FastAPI |
| 25 | Advanced | Databases & packaging |
| 26 | Project | Planning & architecture |
| 27 | Project | Core backend |
| 28 | Project | CLI & data layer |
| 29 | Project | Testing & refinement |
| 30 | Project | Deploy & portfolio |
