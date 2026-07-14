"""
Day 20 — Practice Problems (Part 3 of 3)
===========================================
Topic: Testing — Mixed Challenges

CUMULATIVE SCOPE: Combines Day 20 (unittest, pytest, fixtures, mocking,
coverage, TDD) with prior days (OOP, error handling, dataclasses,
type hints, decorators, file I/O).

DIFFICULTY LEGEND:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines 2+ ideas, requires some thought
    🔴 Challenge — multi-step, real-world style problem

SECTION INDEX (this file):
    Section E — Mixed Challenges   (5 problems)

HOW TO RUN:
    pytest day20_practise_problems_03_mixed_challenges.py -v
"""

import pytest
from unittest.mock import Mock, patch


# ════════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ════════════════════════════════════════════════════════════

# ── Problem E1 ──
# 🟡 Core
# (Combines Day 11 OOP + Day 20 unittest)
# Create a class `Vehicle` with `__init__(self, make, model, fuel_level=100)`
# and a method `drive(km)` that reduces fuel_level by (km * 0.1), raising
# a ValueError if fuel_level would go below 0. Write a unittest.TestCase
# with tests for: driving reduces fuel correctly, and driving too far
# raises ValueError WITHOUT changing fuel_level (verify fuel_level is
# unchanged after the failed attempt).

# YOUR CODE HERE


# ---- SOLUTION ----
# class Vehicle:
#     def __init__(self, make, model, fuel_level=100):
#         self.make = make
#         self.model = model
#         self.fuel_level = fuel_level
#
#     def drive(self, km):
#         fuel_needed = km * 0.1
#         if fuel_needed > self.fuel_level:
#             raise ValueError("Not enough fuel for this trip")
#         self.fuel_level = round(self.fuel_level - fuel_needed, 2)
#
#
# import unittest
#
# class TestVehicle(unittest.TestCase):
#     def setUp(self):
#         self.car = Vehicle("Maruti", "Swift", fuel_level=50)
#
#     def test_drive_reduces_fuel(self):
#         self.car.drive(100)
#         self.assertEqual(self.car.fuel_level, 40.0)
#
#     def test_drive_too_far_raises_and_preserves_fuel(self):
#         with self.assertRaises(ValueError):
#             self.car.drive(1000)
#         self.assertEqual(self.car.fuel_level, 50)  # unchanged
# Expected: both tests pass
print("-" * 50)


# ── Problem E2 ──
# 🟡 Core
# (Combines Day 9 error handling + Day 20 pytest fixtures)
# Write a custom exception `InsufficientStockError(Exception)`. Write a
# class `Warehouse` with a dict `stock` (item -> quantity) and a method
# `ship(item, qty)` that reduces stock[item] by qty, raising
# InsufficientStockError if qty > available stock. Write a fixture
# `sample_warehouse` pre-loaded with {"Laptop": 5, "Mouse": 20}, and
# tests for a successful shipment and an insufficient-stock shipment.

# YOUR CODE HERE


# ---- SOLUTION ----
# class InsufficientStockError(Exception):
#     pass
#
# class Warehouse:
#     def __init__(self, stock):
#         self.stock = stock
#
#     def ship(self, item, qty):
#         available = self.stock.get(item, 0)
#         if qty > available:
#             raise InsufficientStockError(f"Only {available} units of {item} left")
#         self.stock[item] = available - qty
#
# @pytest.fixture
# def sample_warehouse():
#     return Warehouse(stock={"Laptop": 5, "Mouse": 20})
#
# def test_ship_success(sample_warehouse):
#     sample_warehouse.ship("Mouse", 5)
#     assert sample_warehouse.stock["Mouse"] == 15
#
# def test_ship_insufficient_stock_raises(sample_warehouse):
#     with pytest.raises(InsufficientStockError):
#         sample_warehouse.ship("Laptop", 10)
# Expected: both tests pass
print("-" * 50)


# ── Problem E3 ──
# 🔴 Challenge
# (Combines Day 14 decorators + Day 20 mocking)
# You are given a `retry_on_failure(max_attempts=3)` decorator (assume
# it already exists and retries the wrapped function up to max_attempts
# times if it raises an exception, re-raising the last exception if all
# attempts fail). Write a function `charge_card(gateway, amount)` that
# calls `gateway.charge(amount)` — decorate it with @retry_on_failure().
# Using a Mock whose `.charge` side_effect is
# `[ConnectionError, ConnectionError, {"status": "ok"}]` (fails twice,
# succeeds on 3rd try), write a test proving the function eventually
# returns {"status": "ok"} and that `.charge` was called exactly 3 times.

# YOUR CODE HERE


# ---- SOLUTION ----
# import functools
# import time
#
# def retry_on_failure(max_attempts=3):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             last_error = None
#             for attempt in range(max_attempts):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     last_error = e
#                     time.sleep(0)  # no real delay needed in tests
#             raise last_error
#         return wrapper
#     return decorator
#
# @retry_on_failure(max_attempts=3)
# def charge_card(gateway, amount):
#     return gateway.charge(amount)
#
# def test_charge_card_succeeds_after_retries():
#     mock_gateway = Mock()
#     mock_gateway.charge.side_effect = [
#         ConnectionError("timeout"),
#         ConnectionError("timeout"),
#         {"status": "ok"},
#     ]
#     result = charge_card(mock_gateway, 999)
#     assert result == {"status": "ok"}
#     assert mock_gateway.charge.call_count == 3
# Expected: test passes (2 failures then success, exactly 3 calls total)
print("-" * 50)


# ── Problem E4 ──
# 🔴 Challenge
# (Combines Day 8 file I/O + Day 20 patch/monkeypatch)
# Write a function `load_config(path: str) -> dict` that reads a JSON
# file at `path` and returns its parsed contents, raising a
# FileNotFoundError with a custom message "Config file missing: {path}"
# if the file doesn't exist (catch the real FileNotFoundError and
# re-raise with the custom message). Using `patch("builtins.open")`
# or pytest's `tmp_path` fixture, write:
#   1. A test that writes a temp JSON file and confirms load_config
#      reads it correctly.
#   2. A test that load_config on a non-existent path raises
#      FileNotFoundError with the expected message.

# YOUR CODE HERE


# ---- SOLUTION ----
# import json
#
# def load_config(path):
#     try:
#         with open(path, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Config file missing: {path}")
#
# def test_load_config_reads_json(tmp_path):
#     config_file = tmp_path / "config.json"
#     config_file.write_text(json.dumps({"env": "production", "debug": False}))
#     result = load_config(str(config_file))
#     assert result == {"env": "production", "debug": False}
#
# def test_load_config_missing_file_raises():
#     with pytest.raises(FileNotFoundError, match="Config file missing"):
#         load_config("/nonexistent/path/config.json")
# Expected: both tests pass (tmp_path is a built-in pytest fixture that
# gives each test its own temporary directory, auto-cleaned afterward)
print("-" * 50)


# ── Problem E5 ──
# 🔴 Challenge
# (Combines Day 17 dataclasses + Day 20 TDD)
# Practice TDD: build a `TaskManager` class (a lightweight preview of
# the course capstone!) with an `add_task(title, priority)` method and
# a `high_priority_count() -> int` method (counts tasks with
# priority == "high"). FOLLOW THE TDD CYCLE:
#   1. Write a test for an empty TaskManager having high_priority_count() == 0
#      (RED — TaskManager doesn't exist yet)
#   2. Write the minimal TaskManager to pass that one test (GREEN)
#   3. Write a test adding 2 high-priority + 1 low-priority task, expect
#      count == 2 (RED again against your minimal version)
#   4. Extend TaskManager to pass BOTH tests (GREEN)
# Show your final TaskManager class AND both tests.

# YOUR CODE HERE


# ---- SOLUTION ----
# from dataclasses import dataclass, field
#
# @dataclass
# class Task:
#     title: str
#     priority: str
#
# class TaskManager:
#     def __init__(self):
#         self.tasks: list[Task] = []
#
#     def add_task(self, title, priority):
#         self.tasks.append(Task(title=title, priority=priority))
#
#     def high_priority_count(self):
#         return sum(1 for task in self.tasks if task.priority == "high")
#
# def test_empty_task_manager_has_zero_high_priority():
#     manager = TaskManager()
#     assert manager.high_priority_count() == 0
#
# def test_high_priority_count_with_mixed_tasks():
#     manager = TaskManager()
#     manager.add_task("Fix login bug", priority="high")
#     manager.add_task("Update docs", priority="low")
#     manager.add_task("Review PR #42", priority="high")
#     assert manager.high_priority_count() == 2
# Expected: both tests pass
print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# SECTIONS IN THIS FILE:
#   E — Mixed Challenges   (5 problems)
#
# DIFFICULTY BREAKDOWN: 0x 🟢 Warm-up | 2x 🟡 Core | 3x 🔴 Challenge
#
# ════════════════════════════════════════════════════════════
# DAY 20 PROBLEM SET — FULL SUMMARY (ALL 3 FILES)
# ════════════════════════════════════════════════════════════
#   File 1 (Sections A-B): Review + unittest/pytest    — 8 problems
#   File 2 (Sections C-D): Fixtures + Mocking           — 10 problems
#   File 3 (Section E):    Mixed Challenges             — 5 problems
#   TOTAL: 23 problems
#   Difficulty spread: 6x 🟢 Warm-up | 9x 🟡 Core | 8x 🔴 Challenge
#
# NEXT: Day 21 — Data & NumPy (arrays, broadcasting, vectorized ops)

if __name__ == "__main__":
    print("All solutions are commented out above.")
    print("Uncomment a solution block and run with `pytest <this file> -v` to try it.")
