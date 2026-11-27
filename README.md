# Python in 60 Days (Beginner to Advanced)

A project-based Python course for complete beginners (Indian context). You build **one project, PaisaTracker**, a command-line expense tracker, and it grows a little every day.

> Formerly *Python in 30 Days*. The same 30 topics, now taught **one lesson per day over 60 days**. Each day is about 1 hour, so no day feels heavy.

## The story
Priya, 21, works in Mumbai and earns ₹25,000 a month. At month end she asks: *where did all my money go?* PaisaTracker is her digital *khata* (ledger).

## How each day works
Every day has a YouTube video and these files:

| File | What it is |
|------|------------|
| `1_story_syntax` notebook | A short story, the syntax, simple examples, 2 exercises |
| `2_concepts` notebook | One concept at a time, each with a small exercise |
| `3_paisatracker` notebook | The day's step added to PaisaTracker |
| `.py` file | All concepts as one runnable script |
| Practice problems | `.py` and `.ipynb`, with solutions |

## PaisaTracker versions

| Version | Days | What you have by the end |
|---------|------|--------------------------|
| v0 Calculator | 2 to 6 | In-memory tracker with a menu loop |
| v1 Saves data | 7 to 13 | Neat output, saves/loads CSV and JSON, validates input, logs errors |
| v2 Organised code | 14 to 31 | Classes, modules, generators, decorators, functional helpers, concurrency |
| v3 Professional | 32 to 55 | Dataclasses, type hints, pytest, NumPy/Pandas, APIs, FastAPI, SQLite, packaging |
| Final | 56 to 60 | Typer CLI, tests, deployment, GitHub portfolio |

## Full 60-day plan


### Phase 1: Setup

| Day | Topic | What you learn | PaisaTracker step |
|-----|-------|----------------|-------------------|
| 1 | Environment setup | Python 3.12, uv, VS Code, venv, Hello World | Create `paisatracker/` and first `Hello, PaisaTracker` script |

### Phase 2: Beginner (v0)

| Day | Topic | What you learn | PaisaTracker step |
|-----|-------|----------------|-------------------|
| 2 | Variables & data types | Variables and data types | Store one expense (name, amount, category) |
| 3 | Control flow | if / elif / else | Warn when an expense is above a limit |
| 4 | Data structures | list, tuple, dict, set, slicing | Expenses as a list of dicts; category totals |
| 5 | Loops | for, while, break/continue/pass, loop else | Expense report with `for`; menu loop with `while` |
| 6 | Functions & scope | def, return, defaults, scope | Menu actions turned into functions (v0 complete) |

### Phase 3: Intermediate (v1, v2)

| Day | Topic | What you learn | PaisaTracker step |
|-----|-------|----------------|-------------------|
| 7 | Strings & string methods (Part 1 of 2) | Formatting, f-strings, split/join/strip/replace | Neat table output |
| 8 | Strings & string methods (Part 2 of 2) | `re` basics | Parse "250 chai" quick-entry text |
| 9 | File I/O (Part 1 of 3) | open/read/write/append and `with` | Save and load expenses as text |
| 10 | File I/O (Part 2 of 3) | `csv` | Save and load expenses (CSV) |
| 11 | File I/O (Part 3 of 3) | `json` | Save settings (JSON) |
| 12 | Error handling (Part 1 of 2) | try/except/else/finally, `raise` | Validate amounts and dates |
| 13 | Error handling (Part 2 of 2) | Custom exceptions, `logging` | `InvalidAmountError`; error log file |
| 14 | OOP I (Part 1 of 3) | Classes/objects, `__init__`, `self` | `Expense` class |
| 15 | OOP I (Part 2 of 3) | Instance vs class variables | Class-level settings for `Expense` |
| 16 | OOP I (Part 3 of 3) | Instance methods | `ExpenseBook` class |
| 17 | OOP II (Part 1 of 3) | Inheritance, `super()` | `Category` hierarchy |
| 18 | OOP II (Part 2 of 3) | Polymorphism, encapsulation, properties | `Budget` with protected balance |
| 19 | OOP II (Part 3 of 3) | Dunder methods | `__str__`/`__repr__`/`__len__`/`__eq__` |
| 20 | Modules & packages (Part 1 of 2) | import, `__main__` guard, structure | Split into `models.py`, `storage.py`, `cli.py` |
| 21 | Modules & packages (Part 2 of 2) | Installing packages, stdlib (`os`, `sys`, `math`, `datetime`, `pathlib`) | Date-based monthly filtering |
| 22 | Iterators & generators (Part 1 of 2) | Iterator protocol | Stream large expense files lazily |
| 23 | Iterators & generators (Part 2 of 2) | `yield`, generator expressions, `itertools` | Group by month with `itertools` |
| 24 | Decorators & closures (Part 1 of 3) | First-class functions, closures | Closure-based helpers |
| 25 | Decorators & closures (Part 2 of 3) | Writing decorators, `functools.wraps` | `@timer` and `@log_call` |
| 26 | Decorators & closures (Part 3 of 3) | `@staticmethod`/`@classmethod`/`@property` | `from_csv_row` class method |
| 27 | Functional programming (Part 1 of 2) | `map`/`filter`/`reduce`, `lambda` | Top-N expenses, totals via `reduce` |
| 28 | Functional programming (Part 2 of 2) | `zip`/`enumerate`, `sorted(key=)` | Sorted reports |
| 29 | Concurrency basics (Part 1 of 3) | `threading` | Export reports with threads |
| 30 | Concurrency basics (Part 2 of 3) | `multiprocessing` | Export reports in parallel |
| 31 | Concurrency basics (Part 3 of 3) | `async`/`await`, `asyncio.run()` | Async "fetch exchange rate" simulation |

### Phase 4: Advanced (v3)

| Day | Topic | What you learn | PaisaTracker step |
|-----|-------|----------------|-------------------|
| 32 | Advanced OOP (Part 1 of 3) | Abstract base classes | `BaseExporter` ABC (CSV/JSON) |
| 33 | Advanced OOP (Part 2 of 3) | `Protocol` and metaclasses | Protocol-based exporters |
| 34 | Advanced OOP (Part 3 of 3) | `@dataclass` | `Expense` as a dataclass |
| 35 | Type hints & static analysis (Part 1 of 2) | Hints, `Optional`/`Union` | Add hints to the codebase |
| 36 | Type hints & static analysis (Part 2 of 2) | `mypy`, `TypeVar`, generics | Codebase that passes mypy |
| 37 | Context managers (Part 1 of 2) | `__enter__`/`__exit__` | Safe file/DB handling |
| 38 | Context managers (Part 2 of 2) | `contextlib`, `@contextmanager` | `with Timer():` for reports |
| 39 | Testing (Part 1 of 3) | `unittest` basics, TDD intro | First tests for `Expense` |
| 40 | Testing (Part 2 of 3) | `pytest` (assertions, parametrize, fixtures) | Test suite for `Expense` and `Budget` |
| 41 | Testing (Part 3 of 3) | Mocking and coverage | Mocks and coverage report |
| 42 | Data & NumPy (Part 1 of 3) | Arrays vs lists, indexing | Expenses as arrays |
| 43 | Data & NumPy (Part 2 of 3) | Broadcasting, vectorised ops | Fast monthly statistics (mean, std) |
| 44 | Data & NumPy (Part 3 of 3) | `np.linalg` basics | Trend calculation |
| 45 | Data & Pandas (Part 1 of 3) | DataFrame/Series, `read_csv`/`to_csv` | Load expenses into a DataFrame |
| 46 | Data & Pandas (Part 2 of 3) | `groupby`, aggregations | Category and monthly analytics |
| 47 | Data & Pandas (Part 3 of 3) | `merge`/`join`, `df.plot()` | Chart export |
| 48 | Web requests & APIs (Part 1 of 2) | `requests` (GET/POST, headers, params, JSON) | Fetch live USD→INR rate |
| 49 | Web requests & APIs (Part 2 of 2) | Auth headers, `httpx` async | Multi-currency expenses |
| 50 | Web framework: FastAPI (Part 1 of 3) | Routes, path/query params | Read endpoints for expenses |
| 51 | Web framework: FastAPI (Part 2 of 3) | Pydantic models and request bodies | Create/update endpoints |
| 52 | Web framework: FastAPI (Part 3 of 3) | Async endpoints, Swagger `/docs` | Reports API |
| 53 | Databases & packaging (Part 1 of 3) | `sqlite3` | Move storage to SQLite |
| 54 | Databases & packaging (Part 2 of 3) | SQLAlchemy ORM and migrations basics | ORM models |
| 55 | Databases & packaging (Part 3 of 3) | `pyproject.toml`, `uv build`, Docker basics | Package and containerise |

### Phase 5: Capstone (Final)

| Day | Topic | What you learn | PaisaTracker step |
|-----|-------|----------------|-------------------|
| 56 | Review & architecture | Requirements, ERD, folder structure, Git | Git initialised, architecture reviewed |
| 57 | Core backend polish | Models, storage layer, API wired to SQLite | Clean backend |
| 58 | CLI & data layer | Typer CLI (`add`,`list`,`budget`,`report`,`export`) with `rich` | CLI |
| 59 | Testing & refinement | 80%+ coverage, refactor pass | Tested codebase |
| 60 | Deploy & portfolio | Dockerfile, deployment, README, GitHub repo | Live project |

## Quick lookup: old topic number to new day

| Old topic | Topic | New days |
|-----------|-------|----------|
| 1 | Environment setup | 1 |
| 2 | Variables & data types | 2 |
| 3 | Control flow | 3 |
| 4 | Data structures | 4 |
| 5 | Loops | 5 |
| 6 | Functions & scope | 6 |
| 7 | Strings & string methods | 7 to 8 |
| 8 | File I/O | 9 to 11 |
| 9 | Error handling | 12 to 13 |
| 10 | OOP I | 14 to 16 |
| 11 | OOP II | 17 to 19 |
| 12 | Modules & packages | 20 to 21 |
| 13 | Iterators & generators | 22 to 23 |
| 14 | Decorators & closures | 24 to 26 |
| 15 | Functional programming | 27 to 28 |
| 16 | Concurrency basics | 29 to 31 |
| 17 | Advanced OOP | 32 to 34 |
| 18 | Type hints & static analysis | 35 to 36 |
| 19 | Context managers | 37 to 38 |
| 20 | Testing | 39 to 41 |
| 21 | Data & NumPy | 42 to 44 |
| 22 | Data & Pandas | 45 to 47 |
| 23 | Web requests & APIs | 48 to 49 |
| 24 | Web framework: FastAPI | 50 to 52 |
| 25 | Databases & packaging | 53 to 55 |
| 26 | Review & architecture | 56 |
| 27 | Core backend polish | 57 |
| 28 | CLI & data layer | 58 |
| 29 | Testing & refinement | 59 |
| 30 | Deploy & portfolio | 60 |

## Before you start
- A laptop (Windows, macOS or Linux)
- No programming experience needed
- Python 3.12, `uv` and VS Code are set up on Day 1

## Learning path
Setup (1) → Beginner (2 to 6) → Intermediate (7 to 31) → Advanced (32 to 55) → Capstone (56 to 60)

## Links
- YouTube playlist: [add link]
- GitHub repo: [add link]
