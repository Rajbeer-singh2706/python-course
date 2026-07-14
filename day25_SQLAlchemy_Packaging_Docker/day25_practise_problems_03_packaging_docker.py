"""
Day 25 — Databases & Packaging — Practice Problems (File 3 of 3)

Cumulative scope: Days 8-9 (files, exceptions), Day 10-11 (OOP), Day 25
(sqlite3, SQLAlchemy, packaging & Docker)

Difficulty legend:
    🟢 Warm-up  — direct application of one concept
    🟡 Core      — combines 2-3 concepts, requires some thought
    🔴 Challenge — multi-step, closer to a real-world task

Section index:
    Section D — Packaging & Docker
    Section E — Mixed Challenges (combines current + prior day concepts)

How to run:
    python day25_practise_problems_03_packaging_docker.py

All solutions are commented out below their starter code. Try each problem
yourself first, then uncomment the SOLUTION block to check your work.
"""

import os
import csv
import sqlite3
from sqlalchemy import create_engine, String, Integer, select, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

print("=" * 50)
print("SECTION D — Packaging & Docker")
print("=" * 50)

# ────────────────────────────────────────────────────────────────
# Problem D1 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Write a function `extract_dependencies(toml_text)` that parses the
# `dependencies = [...]` list out of a pyproject.toml-style string and
# returns it as a list of strings (stripping quotes and trailing commas).
#
# Expected output for the sample below:
# ['sqlalchemy>=2.0', 'typer>=0.9', 'rich>=13.0']

sample_toml = '''[project]
name = "expense-tracker"
dependencies = [
    "sqlalchemy>=2.0",
    "typer>=0.9",
    "rich>=13.0",
]
'''

# YOUR CODE HERE


# SOLUTION:
# def extract_dependencies(toml_text):
#     deps = []
#     in_deps = False
#     for line in toml_text.splitlines():
#         stripped = line.strip()
#         if stripped.startswith("dependencies"):
#             in_deps = True
#             continue
#         if in_deps:
#             if stripped.startswith("]"):
#                 break
#             dep = stripped.strip(',').strip('"')
#             if dep:
#                 deps.append(dep)
#     return deps
#
# print(extract_dependencies(sample_toml))
# Expected output:
# ['sqlalchemy>=2.0', 'typer>=0.9', 'rich>=13.0']

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem D2 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Write a function `has_build_system(toml_text)` that returns True if the
# string "[build-system]" appears in the text, False otherwise. Test it
# on `sample_toml` (should be False) and on `sample_toml + "\\n[build-system]"`
# (should be True).
#
# Expected output: False True

# YOUR CODE HERE


# SOLUTION:
# def has_build_system(toml_text):
#     return "[build-system]" in toml_text
#
# print(has_build_system(sample_toml), has_build_system(sample_toml + "\n[build-system]"))
# Expected output:
# False True

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem D3 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Write a function `generate_dockerfile(base_image, run_command)` that
# returns a Dockerfile as a multi-line string with these exact lines,
# in order: FROM <base_image>, WORKDIR /app, COPY . ., and
# CMD ["<run_command>"].
#
# Expected output when called with ("python:3.12-slim", "python app.py"):
# FROM python:3.12-slim
# WORKDIR /app
# COPY . .
# CMD ["python app.py"]

# YOUR CODE HERE


# SOLUTION:
# def generate_dockerfile(base_image, run_command):
#     return (
#         f"FROM {base_image}\n"
#         f"WORKDIR /app\n"
#         f"COPY . .\n"
#         f'CMD ["{run_command}"]\n'
#     )
#
# print(generate_dockerfile("python:3.12-slim", "python app.py"))
# Expected output:
# FROM python:3.12-slim
# WORKDIR /app
# COPY . .
# CMD ["python app.py"]

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem D4 — 🔴 Challenge
# ────────────────────────────────────────────────────────────────
# Write a function `categorize_dockerignore(text)` that scans a
# .dockerignore-style string (ignoring blank lines and "#" comments) and
# returns a dict counting how many entries are: a "dirs" entry (ends
# with "/"), a "wildcards" entry (contains "*"), or a plain "files" entry
# (neither of the above).
#
# Expected output for the sample below:
# {'dirs': 2, 'files': 2, 'wildcards': 2}

sample_ignore = ".git\n.venv/\n__pycache__/\n*.pyc\n.env\n*.db\n"

# YOUR CODE HERE


# SOLUTION:
# def categorize_dockerignore(text):
#     dirs, files, wildcards = 0, 0, 0
#     for line in text.splitlines():
#         stripped = line.strip()
#         if not stripped or stripped.startswith("#"):
#             continue
#         if stripped.endswith("/"):
#             dirs += 1
#         elif "*" in stripped:
#             wildcards += 1
#         else:
#             files += 1
#     return {"dirs": dirs, "files": files, "wildcards": wildcards}
#
# print(categorize_dockerignore(sample_ignore))
# Expected output:
# {'dirs': 2, 'files': 2, 'wildcards': 2}

print("-" * 50)


print("=" * 50)
print("SECTION E — Mixed Challenges")
print("=" * 50)

# ────────────────────────────────────────────────────────────────
# Problem E1 — 🟡 Core (sqlite3 + File I/O)
# ────────────────────────────────────────────────────────────────
# Create a SQLite table "tasks" (id, title, done) and insert these three
# rows: ("Buy groceries", 1), ("Pay electricity bill", 0),
# ("Call plumber", 1). Write a function `export_tasks_to_csv(conn,
# filename)` that queries all tasks, writes them to a CSV with a header
# row, then reads the file back and returns the number of DATA rows
# (excluding the header).
#
# Expected output: 3

# YOUR CODE HERE


# SOLUTION:
# DB = "tasks_practice.db"
# if os.path.exists(DB):
#     os.remove(DB)
# conn = sqlite3.connect(DB)
# conn.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")
# conn.executemany(
#     "INSERT INTO tasks (title, done) VALUES (?, ?)",
#     [("Buy groceries", 1), ("Pay electricity bill", 0), ("Call plumber", 1)]
# )
# conn.commit()
#
# def export_tasks_to_csv(conn, filename):
#     rows = conn.execute("SELECT title, done FROM tasks").fetchall()
#     with open(filename, "w", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["title", "done"])
#         writer.writerows(rows)
#     with open(filename) as f:
#         return sum(1 for _ in f) - 1
#
# count = export_tasks_to_csv(conn, "tasks_export.csv")
# print(count)
# conn.close()
# os.remove(DB)
# os.remove("tasks_export.csv")
# Expected output:
# 3

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem E2 — 🔴 Challenge (SQLAlchemy + OOP method)
# ────────────────────────────────────────────────────────────────
# Define a SQLAlchemy model `CartItem` (item_id, name, price, quantity)
# with an instance method `line_total()` that returns price * quantity.
# Insert three BigBasket-style cart items: ("Onions 1kg", 40.0, qty=2),
# ("Tomatoes 1kg", 35.0, qty=3), ("Toor Dal 1kg", 150.0, qty=1). Fetch all
# items and sum their line_total() values to get the cart total.
#
# Expected output: 335.0

# YOUR CODE HERE


# SOLUTION:
# class CartBase(DeclarativeBase):
#     pass
#
# class CartItem(CartBase):
#     __tablename__ = "cart_items"
#     item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     price: Mapped[float] = mapped_column()
#     quantity: Mapped[int] = mapped_column()
#
#     def line_total(self):
#         return self.price * self.quantity
#
# cart_engine = create_engine("sqlite:///cart_practice.db")
# CartBase.metadata.create_all(cart_engine)
# with Session(cart_engine) as session:
#     session.add_all([
#         CartItem(name="Onions 1kg", price=40.0, quantity=2),
#         CartItem(name="Tomatoes 1kg", price=35.0, quantity=3),
#         CartItem(name="Toor Dal 1kg", price=150.0, quantity=1),
#     ])
#     session.commit()
#
# with Session(cart_engine) as session:
#     items = session.scalars(select(CartItem)).all()
#     cart_total = sum(item.line_total() for item in items)
#     print(cart_total)
# os.remove("cart_practice.db")
# Expected output:
# 335.0

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem E3 — 🔴 Challenge (Database + Packaging, end-to-end)
# ────────────────────────────────────────────────────────────────
# Write a function `build_deployment_manifest(engine, app_name, version)`
# that inspects the database behind `engine` and returns a dict:
#   {
#     "app": app_name,
#     "version": version,
#     "tables": <sorted list of table names in the database>,
#     "image_tag": f"{app_name}:{version}"
#   }
# This mimics generating a small deployment summary before building a
# Docker image — combining what you know about a database's schema with
# packaging metadata.
#
# Using the CartItem model/table from E2, call it with
# ("grocery-tracker", "0.1.0").
#
# Expected output:
# {'app': 'grocery-tracker', 'version': '0.1.0', 'tables': ['cart_items'], 'image_tag': 'grocery-tracker:0.1.0'}

# YOUR CODE HERE


# SOLUTION:
# def build_deployment_manifest(engine, app_name, version):
#     inspector = inspect(engine)
#     return {
#         "app": app_name,
#         "version": version,
#         "tables": sorted(inspector.get_table_names()),
#         "image_tag": f"{app_name}:{version}",
#     }
#
# manifest_engine = create_engine("sqlite:///manifest_practice.db")
# CartBase.metadata.create_all(manifest_engine)
# manifest = build_deployment_manifest(manifest_engine, "grocery-tracker", "0.1.0")
# print(manifest)
# os.remove("manifest_practice.db")
# Expected output:
# {'app': 'grocery-tracker', 'version': '0.1.0', 'tables': ['cart_items'], 'image_tag': 'grocery-tracker:0.1.0'}

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# Sections in this file:
#   D — Packaging & Docker: 4 problems (dependency parsing, build-system
#       detection, Dockerfile generation, .dockerignore categorization)
#   E — Mixed Challenges: 3 problems (sqlite3 + CSV export, SQLAlchemy +
#       OOP method, database + packaging manifest)
#
# Difficulty breakdown: 2 🟢 warm-up, 2 🟡 core, 3 🔴 challenge (7 problems)
#
# ════════════════════════════════════════════════════════════════
# DAY 25 PRACTICE SET — FULL SUMMARY (all 3 files)
# ════════════════════════════════════════════════════════════════
#   File 1 (Sections A-B): 8 problems — review + SQLite basics
#   File 2 (Section C):     5 problems — SQLAlchemy ORM
#   File 3 (Sections D-E):  7 problems — packaging/Docker + mixed challenges
#   TOTAL: 20 problems (7 warm-up, 7 core, 6 challenge)
#
# Next up: Day 26 begins the Capstone Project — planning & architecture
# for the full-stack Task Manager (taskcli).

if __name__ == "__main__":
    print("Day 25 Practice Set — File 3 (Sections D-E) loaded. Try the problems above!")
    print("This completes the Day 25 practice problem set (20 problems total).")
