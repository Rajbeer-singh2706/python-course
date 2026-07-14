"""
Day 25 — Databases & Packaging
File 3 of 3: Packaging Your Project & Docker Basics

What this file covers:
    - Why packaging matters (turning a folder of scripts into an installable tool)
    - pyproject.toml structure — the modern standard for Python project metadata
    - Building a distributable package with `uv build`
    - Docker basics — image vs container, the Dockerfile, build & run commands
    - Writing a minimal Dockerfile for a Python app
    - .dockerignore — keeping images small and clean

Prerequisites:
    - Day 12 (Modules & Packages) — import system, __main__ guard
    - day25_01_sqlite_basics.py and day25_02_sqlalchemy_orm.py — the database
      layer this packaging example wraps

How to run:
    python day25_03_packaging_docker.py

NOTE: This file is documentation-driven rather than execution-heavy — most
of what it teaches (running `uv build`, `docker build`, `docker run`) happens
in your TERMINAL, not inside a running Python script. The code below writes
real example files (pyproject.toml, Dockerfile, .dockerignore) to a
"packaging_demo" folder so you can see exactly what they look like and try
the terminal commands yourself.
"""

import os

DEMO_DIR = "packaging_demo"
os.makedirs(DEMO_DIR, exist_ok=True)

# ════════════════════════════════════════════════════════════════
# SECTION 1: Why Package Your Project?
# ════════════════════════════════════════════════════════════════
#
# Right now, running your code means "cd into the folder and run
# python somefile.py". That's fine for learning, but it breaks down when:
#   - You want someone else to `pip install your-tool` and just use it
#   - You want a single command like `taskcli` to work from anywhere
#   - Your project depends on specific versions of specific libraries and
#     you need that documented and reproducible
#
# Packaging solves all three: it bundles your code, its dependencies, and
# its metadata (name, version, entry points) into a distributable unit.

print("A package turns a folder of scripts into an installable, distributable tool.")
# Output:
# A package turns a folder of scripts into an installable, distributable tool.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2: pyproject.toml — The Modern Standard
# ════════════════════════════════════════════════════════════════
#
# pyproject.toml replaced the older setup.py/setup.cfg approach. It's a
# single, declarative file (TOML format — like a stricter, cleaner version
# of INI files) that every modern Python tool (pip, uv, poetry, build)
# understands. Key sections:
#
#   [project]           -> name, version, description, dependencies
#   [project.scripts]   -> defines command-line entry points
#   [build-system]       -> which tool builds your package (uv, hatchling, etc.)

pyproject_toml_content = '''\
[project]
name = "grocery-tracker"
version = "0.1.0"
description = "A simple CLI to track BigBasket grocery orders and spending"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "sqlalchemy>=2.0",
    "typer>=0.9",
]

[project.scripts]
grocery-tracker = "grocery_tracker.cli:app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
'''

pyproject_path = os.path.join(DEMO_DIR, "pyproject.toml")
with open(pyproject_path, "w") as f:
    f.write(pyproject_toml_content)

print(f"Wrote example pyproject.toml to: {pyproject_path}")
# Output:
# Wrote example pyproject.toml to: packaging_demo/pyproject.toml

# ── Reading it back to show the key sections ──
with open(pyproject_path) as f:
    lines = f.readlines()
print(f"pyproject.toml has {len(lines)} lines across [project], [project.scripts], [build-system]")
# Output:
# pyproject.toml has 17 lines across [project], [project.scripts], [build-system]

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3: The `src/` Layout
# ════════════════════════════════════════════════════════════════
#
# Real Python packages typically use a "src layout":
#
#   grocery-tracker/
#   ├── pyproject.toml
#   ├── README.md
#   └── src/
#       └── grocery_tracker/
#           ├── __init__.py
#           ├── cli.py
#           └── models.py
#
# Why src/ instead of putting grocery_tracker/ at the top level? It forces
# you to actually install the package (uv pip install -e .) before you can
# import it — which catches "it works on my machine because of accidental
# path magic" bugs before your users ever hit them.

src_package_dir = os.path.join(DEMO_DIR, "src", "grocery_tracker")
os.makedirs(src_package_dir, exist_ok=True)

with open(os.path.join(src_package_dir, "__init__.py"), "w") as f:
    f.write('"""grocery_tracker package."""\n__version__ = "0.1.0"\n')

with open(os.path.join(src_package_dir, "cli.py"), "w") as f:
    f.write(
        '"""Command-line entry point for grocery_tracker."""\n\n'
        'def app():\n'
        '    print("grocery-tracker CLI running!")\n'
    )

print("Created src/ layout: src/grocery_tracker/{__init__.py, cli.py}")
# Output:
# Created src/ layout: src/grocery_tracker/{__init__.py, cli.py}

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 4: Building with `uv build`
# ════════════════════════════════════════════════════════════════
#
# Once pyproject.toml and the src/ layout are in place, building a
# distributable package is one terminal command:
#
#     cd packaging_demo
#     uv build
#
# This produces a dist/ folder containing:
#   - grocery_tracker-0.1.0.tar.gz   (source distribution, "sdist")
#   - grocery_tracker-0.1.0-py3-none-any.whl   (built distribution, "wheel")
#
# The .whl file is what gets installed with `pip install` or `uv add` — it's
# a pre-built, ready-to-use format. You could then publish it to PyPI with
# `uv publish`, or share the file directly, or install it locally with:
#
#     uv pip install dist/grocery_tracker-0.1.0-py3-none-any.whl

print("Terminal reference: 'uv build' -> creates dist/*.tar.gz and dist/*.whl")
# Output:
# Terminal reference: 'uv build' -> creates dist/*.tar.gz and dist/*.whl

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 5: Docker Basics — Image vs Container
# ════════════════════════════════════════════════════════════════
#
# Packaging (Section 2-4) solves "install my Python code." Docker solves a
# bigger problem: "run my code with the EXACT same OS, Python version, and
# system libraries, on any machine, every time."
#
# Two key terms:
#   - IMAGE: a read-only template/blueprint — like a class in OOP terms.
#     Built once from a Dockerfile's instructions.
#   - CONTAINER: a running instance of an image — like an object created
#     from that class. You can run many containers from one image.

print("Docker analogy: Image is the class, Container is the object created from it.")
# Output:
# Docker analogy: Image is the class, Container is the object created from it.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 6: Writing a Dockerfile
# ════════════════════════════════════════════════════════════════
#
# A Dockerfile is a plain-text list of instructions Docker executes in
# order to build an image, layer by layer.

dockerfile_content = '''\
# Start from an official, slim Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency files first (better build caching -- if only your code
# changes, Docker can reuse the cached "install dependencies" layer)
COPY pyproject.toml .

# Install dependencies
RUN pip install --no-cache-dir .

# Copy the rest of the application code
COPY src/ ./src/

# Document which port the app listens on (informational only)
EXPOSE 8000

# The command that runs when a container starts from this image
CMD ["python", "-m", "grocery_tracker.cli"]
'''

dockerfile_path = os.path.join(DEMO_DIR, "Dockerfile")
with open(dockerfile_path, "w") as f:
    f.write(dockerfile_content)

print(f"Wrote example Dockerfile to: {dockerfile_path}")
# Output:
# Wrote example Dockerfile to: packaging_demo/Dockerfile

num_instructions = sum(
    1 for line in dockerfile_content.splitlines()
    if line.strip() and not line.strip().startswith("#")
)
print(f"Dockerfile contains {num_instructions} instruction lines (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD)")
# Output:
# Dockerfile contains 7 instruction lines (FROM, WORKDIR, COPY, RUN, COPY, EXPOSE, CMD)

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 7: .dockerignore — Keeping Images Lean
# ════════════════════════════════════════════════════════════════
#
# Just like .gitignore, a .dockerignore file tells Docker which files to
# skip when building the image. Without it, Docker may copy your entire
# .git history, virtual environments, and __pycache__ folders into the
# image — bloating it and slowing every build.

dockerignore_content = '''\
.git
.venv
__pycache__/
*.pyc
.pytest_cache/
dist/
*.db
.env
README.md
'''

dockerignore_path = os.path.join(DEMO_DIR, ".dockerignore")
with open(dockerignore_path, "w") as f:
    f.write(dockerignore_content)

print(f"Wrote example .dockerignore to: {dockerignore_path}")
# Output:
# Wrote example .dockerignore to: packaging_demo/.dockerignore

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 8: Building & Running a Container (Terminal Reference)
# ════════════════════════════════════════════════════════════════
#
# With a Dockerfile in place, these are the core terminal commands:
#
#   docker build -t grocery-tracker:0.1.0 .
#       -> Builds an image named "grocery-tracker", tagged "0.1.0",
#          using the Dockerfile in the current directory (.)
#
#   docker run grocery-tracker:0.1.0
#       -> Starts a new container from that image
#
#   docker run -p 8000:8000 grocery-tracker:0.1.0
#       -> Maps port 8000 on your machine to port 8000 inside the
#          container -- needed for web apps like FastAPI services
#
#   docker ps
#       -> Lists currently running containers
#
#   docker images
#       -> Lists all images you've built or pulled locally

terminal_commands = [
    "docker build -t grocery-tracker:0.1.0 .",
    "docker run grocery-tracker:0.1.0",
    "docker run -p 8000:8000 grocery-tracker:0.1.0",
    "docker ps",
    "docker images",
]
print("Key Docker terminal commands:")
for cmd in terminal_commands:
    print(f"  $ {cmd}")
# Output:
# Key Docker terminal commands:
#   $ docker build -t grocery-tracker:0.1.0 .
#   $ docker run grocery-tracker:0.1.0
#   $ docker run -p 8000:8000 grocery-tracker:0.1.0
#   $ docker ps
#   $ docker images

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

# ── Example 1: Validating a pyproject.toml has the required sections ──
def has_required_sections(toml_text):
    required = ["[project]", "[project.scripts]", "[build-system]"]
    return all(section in toml_text for section in required)

is_valid = has_required_sections(pyproject_toml_content)
print(f"Example 1: pyproject.toml has all required sections: {is_valid}")
# Output:
# Example 1: pyproject.toml has all required sections: True

# ── Example 2: Extracting the package name from pyproject.toml ──
def extract_package_name(toml_text):
    for line in toml_text.splitlines():
        if line.strip().startswith("name ="):
            return line.split("=")[1].strip().strip('"')
    return None

pkg_name = extract_package_name(pyproject_toml_content)
print(f"Example 2: Package name extracted: {pkg_name}")
# Output:
# Example 2: Package name extracted: grocery-tracker

# ── Example 3: Counting how many patterns .dockerignore excludes ──
ignore_patterns = [line for line in dockerignore_content.splitlines() if line.strip()]
print(f"Example 3: .dockerignore excludes {len(ignore_patterns)} patterns")
# Output:
# Example 3: .dockerignore excludes 9 patterns

# ── Example 4: Simulating an image tag naming convention ──
def build_image_tag(app_name, version, registry="docker.io/rajlearns"):
    """Mimics how you'd tag an image before pushing to a registry
    (e.g. for deploying to Railway or another cloud host)."""
    return f"{registry}/{app_name}:{version}"

tag = build_image_tag("grocery-tracker", "0.1.0")
print(f"Example 4: Full image tag for pushing to a registry: {tag}")
# Output:
# Example 4: Full image tag for pushing to a registry: docker.io/rajlearns/grocery-tracker:0.1.0

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Write a function `count_dockerfile_layers(dockerfile_text)` that returns
# how many distinct instruction TYPES (FROM, WORKDIR, COPY, RUN, EXPOSE,
# CMD, etc.) appear at least once in a Dockerfile, ignoring comments and
# blank lines, and ignoring repeats of the same instruction type.
#
# Expected output when called on the Dockerfile from Section 6:
#   6   (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD -- COPY appears twice but counts once)

# YOUR CODE HERE


# ── Solution (uncomment to check your work) ──
# def count_dockerfile_layers(dockerfile_text):
#     instruction_types = set()
#     for line in dockerfile_text.splitlines():
#         stripped = line.strip()
#         if not stripped or stripped.startswith("#"):
#             continue
#         instruction = stripped.split()[0]
#         instruction_types.add(instruction)
#     return len(instruction_types)
#
# result = count_dockerfile_layers(dockerfile_content)
# print(result)
# Expected output:
# 6


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Why packaging matters: installable, distributable, reproducible code
#   - pyproject.toml structure: [project], [project.scripts], [build-system]
#   - The src/ layout and why it prevents accidental-import bugs
#   - `uv build` -> produces dist/*.tar.gz and dist/*.whl
#   - Docker's image-vs-container distinction (class vs object analogy)
#   - Writing a Dockerfile: FROM, WORKDIR, COPY, RUN, EXPOSE, CMD
#   - .dockerignore for lean, fast image builds
#   - Core terminal commands: docker build, docker run, docker ps, docker images
#
# This wraps up Day 25! Next up: Day 26 begins the Capstone Project --
# planning and architecting the full-stack Task Manager (taskcli) that
# will use everything from sqlite3/SQLAlchemy through to Docker deployment.

if __name__ == "__main__":
    print("Day 25, File 3 complete: Packaging & Docker fundamentals covered.")
    print(f"Example files written under: {os.path.abspath(DEMO_DIR)}/")
