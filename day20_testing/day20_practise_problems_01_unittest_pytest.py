"""
Day 20 — Practice Problems (Part 1 of 3)
===========================================
Topic: Testing — unittest & pytest fundamentals

CUMULATIVE SCOPE: This problem set assumes everything from Days 1-20,
with special focus on Day 9 (error handling), Day 17-18 (dataclasses,
type hints), and Day 20 (unittest, pytest).

DIFFICULTY LEGEND:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines 2+ ideas, requires some thought
    🔴 Challenge — multi-step, real-world style problem

SECTION INDEX (this file):
    Section A — Prior Days Review           (3 problems)
    Section B — unittest & pytest Basics    (5 problems)

HOW TO RUN:
    python day20_practise_problems_01_unittest_pytest.py
"""

import unittest
import pytest
import sys


# ════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════

# ── Problem A1 ──
# 🟢 Warm-up
# (Day 17 review) Create a @dataclass called `Employee` with fields
# `name: str`, `department: str`, `salary: float`. Then write a function
# `apply_raise(emp: Employee, percent: float) -> Employee` that returns
# a NEW Employee with the salary increased by `percent`%.

# YOUR CODE HERE


# ---- SOLUTION ----
# from dataclasses import dataclass, replace
#
# @dataclass
# class Employee:
#     name: str
#     department: str
#     salary: float
#
# def apply_raise(emp: Employee, percent: float) -> Employee:
#     new_salary = round(emp.salary * (1 + percent / 100), 2)
#     return replace(emp, salary=new_salary)
#
# arjun = Employee("Arjun Mehta", "Engineering", 80000.0)
# raised = apply_raise(arjun, 10)
# print(raised)
# Expected Output: Employee(name='Arjun Mehta', department='Engineering', salary=88000.0)
print("-" * 50)


# ── Problem A2 ──
# 🟢 Warm-up
# (Day 9 review) Write a function `safe_divide(a, b)` that returns
# a / b, but returns None (instead of crashing) if b is 0. Use
# try/except, not an if-check.

# YOUR CODE HERE


# ---- SOLUTION ----
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None
#
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# Expected Output:
# 5.0
# None
print("-" * 50)


# ── Problem A3 ──
# 🟡 Core
# (Day 18 review) Write a type-hinted function
# `find_max(numbers: list[int]) -> int | None` that returns the largest
# number in the list, or None if the list is empty.

# YOUR CODE HERE


# ---- SOLUTION ----
# def find_max(numbers: list[int]) -> int | None:
#     if not numbers:
#         return None
#     return max(numbers)
#
# print(find_max([4, 9, 2, 7]))
# print(find_max([]))
# Expected Output:
# 9
# None
print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — unittest & pytest Basics
# ════════════════════════════════════════════════════════════

# ── Problem B1 ──
# 🟢 Warm-up
# Write a function `celsius_to_fahrenheit(c: float) -> float` that
# converts Celsius to Fahrenheit: F = C * 9/5 + 32.
# Then write a unittest.TestCase with 2 tests: freezing point (0C -> 32F)
# and boiling point (100C -> 212F).

# YOUR CODE HERE


# ---- SOLUTION ----
# def celsius_to_fahrenheit(c: float) -> float:
#     return round(c * 9 / 5 + 32, 2)
#
# class TestCelsiusToFahrenheit(unittest.TestCase):
#     def test_freezing_point(self):
#         self.assertEqual(celsius_to_fahrenheit(0), 32.0)
#
#     def test_boiling_point(self):
#         self.assertEqual(celsius_to_fahrenheit(100), 212.0)
# Expected: both tests pass (run via unittest.main())
print("-" * 50)


# ── Problem B2 ──
# 🟢 Warm-up
# Write a function `is_palindrome(text: str) -> bool` that checks if
# a string reads the same forwards and backwards (ignore case).
# Then write pytest-style test FUNCTIONS (not a class) for:
#   "Malayalam" (palindrome when lowercased), "Mumbai" (not a palindrome)

# YOUR CODE HERE


# ---- SOLUTION ----
# def is_palindrome(text: str) -> bool:
#     cleaned = text.lower()
#     return cleaned == cleaned[::-1]
#
# def test_is_palindrome_true():
#     assert is_palindrome("Malayalam") is True
#
# def test_is_palindrome_false():
#     assert is_palindrome("Mumbai") is False
# Expected: both tests pass (run via pytest)
print("-" * 50)


# ── Problem B3 ──
# 🟡 Core
# Write a function `validate_age(age: int) -> int` that returns `age`
# if it's between 0 and 120 inclusive, otherwise raises a ValueError.
# Write a unittest.TestCase with:
#   - a test for a valid age
#   - a test that a negative age raises ValueError
#   - a test that age > 120 raises ValueError
# Use self.assertRaises for the error cases.

# YOUR CODE HERE


# ---- SOLUTION ----
# def validate_age(age: int) -> int:
#     if not 0 <= age <= 120:
#         raise ValueError("age must be between 0 and 120")
#     return age
#
# class TestValidateAge(unittest.TestCase):
#     def test_valid_age(self):
#         self.assertEqual(validate_age(30), 30)
#
#     def test_negative_age_raises(self):
#         with self.assertRaises(ValueError):
#             validate_age(-5)
#
#     def test_too_old_raises(self):
#         with self.assertRaises(ValueError):
#             validate_age(150)
# Expected: all 3 tests pass
print("-" * 50)


# ── Problem B4 ──
# 🟡 Core
# Write a function `word_frequency(text: str) -> dict[str, int]` that
# counts how many times each word appears (case-insensitive, split on
# whitespace). Then write a parametrized pytest test with at least
# 3 cases checking different input strings and expected dicts.

# YOUR CODE HERE


# ---- SOLUTION ----
# def word_frequency(text: str) -> dict[str, int]:
#     words = text.lower().split()
#     freq: dict[str, int] = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq
#
# @pytest.mark.parametrize(
#     "text, expected",
#     [
#         ("Pune Pune Mumbai", {"pune": 2, "mumbai": 1}),
#         ("Delhi", {"delhi": 1}),
#         ("cat dog cat cat dog", {"cat": 3, "dog": 2}),
#     ],
# )
# def test_word_frequency(text, expected):
#     assert word_frequency(text) == expected
# Expected: all 3 parametrized cases pass
print("-" * 50)


# ── Problem B5 ──
# 🔴 Challenge
# Write a function `merge_intervals(intervals: list[tuple[int, int]])
# -> list[tuple[int, int]]` that merges overlapping (start, end)
# intervals into the minimum number of non-overlapping intervals,
# sorted by start. Example: [(1,3), (2,6), (8,10)] -> [(1,6), (8,10)].
# Write at least 4 test cases (unittest OR pytest style) covering:
#   no overlaps, full overlap, partial overlap, and a single interval.

# YOUR CODE HERE


# ---- SOLUTION ----
# def merge_intervals(intervals):
#     if not intervals:
#         return []
#     sorted_intervals = sorted(intervals, key=lambda pair: pair[0])
#     merged = [sorted_intervals[0]]
#     for current_start, current_end in sorted_intervals[1:]:
#         last_start, last_end = merged[-1]
#         if current_start <= last_end:
#             merged[-1] = (last_start, max(last_end, current_end))
#         else:
#             merged.append((current_start, current_end))
#     return merged
#
# @pytest.mark.parametrize(
#     "intervals, expected",
#     [
#         ([(1, 2), (3, 4)], [(1, 2), (3, 4)]),               # no overlap
#         ([(1, 5), (2, 4)], [(1, 5)]),                         # full overlap
#         ([(1, 3), (2, 6), (8, 10)], [(1, 6), (8, 10)]),       # partial overlap
#         ([(5, 9)], [(5, 9)]),                                  # single interval
#     ],
# )
# def test_merge_intervals(intervals, expected):
#     assert merge_intervals(intervals) == expected
# Expected: all 4 parametrized cases pass
print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# SECTIONS IN THIS FILE:
#   A — Prior Days Review           (3 problems)
#   B — unittest & pytest Basics    (5 problems)
#
# DIFFICULTY BREAKDOWN: 4x 🟢 Warm-up | 3x 🟡 Core | 1x 🔴 Challenge
#
# NEXT FILE: day20_practise_problems_02_fixtures_mocking.py
#   -> Section C (fixtures) and Section D (mocking)

if __name__ == "__main__":
    print("All solutions are commented out above.")
    print("Uncomment a solution block and its matching print/test calls to try it.")
