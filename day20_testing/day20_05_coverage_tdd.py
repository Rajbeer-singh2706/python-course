"""
Day 20 — Testing (Part 5: Coverage Reports & TDD Intro)
==========================================================

WHAT THIS FILE COVERS:
    - What "code coverage" means and why 100% coverage isn't the goal
    - Running pytest with pytest-cov to generate a coverage report
    - Reading a coverage report (statements, missing lines, percentage)
    - Test-Driven Development (TDD): Red -> Green -> Refactor
    - A worked TDD walkthrough building a function step by step

PREREQUISITES:
    - day20_04_mocking.py (same day, previous file)

HOW TO RUN:
    pytest day20_05_coverage_tdd.py -v
    pytest day20_05_coverage_tdd.py --cov=day20_05_coverage_tdd --cov-report=term-missing

INSTALL:
    pip install pytest-cov --break-system-packages
"""

import sys
import pytest


# ════════════════════════════════════════════════════════════
# SECTION 1: What Is Code Coverage?
# ════════════════════════════════════════════════════════════
#
# "Coverage" measures WHICH LINES of your source code were actually
# executed while your test suite ran. It's reported as a percentage:
#
#     Coverage % = (lines executed by tests / total lines) * 100
#
# High coverage does NOT guarantee bug-free code — it only tells you
# which lines were never even RUN by any test. A common professional
# target is 80%+ coverage (see Day 29 of the capstone, which revisits
# this exact idea for the Task Manager project).


def classify_bmi(weight_kg: float, height_m: float) -> str:
    """Classify BMI into a category — used to demonstrate coverage gaps."""
    if height_m <= 0:
        raise ValueError("height_m must be positive")
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Suppose we ONLY write this one test:
def test_classify_bmi_normal_only():
    assert classify_bmi(65, 1.7) == "Normal"


# If this were the ONLY test in the file, a coverage report would show
# that the "Underweight", "Overweight", "Obese", and ValueError branches
# were NEVER executed — a coverage report would flag those exact line
# numbers as "missing". Let's add tests for every branch below so our
# coverage of `classify_bmi` reaches 100%.


def test_classify_bmi_underweight():
    assert classify_bmi(45, 1.7) == "Underweight"


def test_classify_bmi_overweight():
    assert classify_bmi(80, 1.7) == "Overweight"


def test_classify_bmi_obese():
    assert classify_bmi(100, 1.7) == "Obese"


def test_classify_bmi_invalid_height_raises():
    with pytest.raises(ValueError):
        classify_bmi(70, 0)


# ════════════════════════════════════════════════════════════
# SECTION 2: Running Coverage From the Command Line
# ════════════════════════════════════════════════════════════
#
# From the terminal, in the folder containing this file, run:
#
#     pytest day20_05_coverage_tdd.py \
#         --cov=day20_05_coverage_tdd \
#         --cov-report=term-missing
#
# You'll see a table like:
#
#     Name                          Stmts   Miss  Cover   Missing
#     -----------------------------------------------------------
#     day20_05_coverage_tdd.py        42      0   100%
#     -----------------------------------------------------------
#
# The "Missing" column lists EXACT line numbers that were never
# executed — a direct pointer to which tests you still need to write.


# ════════════════════════════════════════════════════════════
# SECTION 3: Test-Driven Development (TDD) — The Big Idea
# ════════════════════════════════════════════════════════════
#
# TDD flips the usual order: instead of writing code THEN tests,
# you write a FAILING test FIRST, then just enough code to make it
# pass, then clean up. The cycle has three steps, repeated:
#
#   1. RED      — Write a test for behaviour that doesn't exist yet.
#                 Run it. It FAILS (often because the function doesn't
#                 even exist yet).
#   2. GREEN    — Write the SIMPLEST possible code that makes the test
#                 pass. Don't worry about elegance yet.
#   3. REFACTOR — Clean up the code (and/or the test) while keeping
#                 all tests green. Re-run tests after every change.
#
# Benefits: you always have a safety net, you never over-engineer
# (you only write code your tests actually demand), and your test
# suite grows naturally alongside your features.


# ════════════════════════════════════════════════════════════
# SECTION 4: A Worked TDD Walkthrough
# ════════════════════════════════════════════════════════════
#
# GOAL: Build a `calculate_late_fee(days_late: int) -> float` function
# for a Bengaluru public library system.
#
# Business rule (given by the librarian, Riya Deshmukh):
#   - No fee for 0 days late
#   - ₹5 per day for days 1-7
#   - ₹10 per day for any day beyond 7
#
# --- ROUND 1: RED ---
# We write this test BEFORE the function exists:
#
#     def test_no_late_fee_when_on_time():
#         assert calculate_late_fee(0) == 0.0
#
# Running it fails with NameError: calculate_late_fee is not defined.
# That failure is EXPECTED — this is the "RED" step.
#
# --- ROUND 1: GREEN ---
# We write the simplest code that passes JUST this one test:
#
#     def calculate_late_fee(days_late: int) -> float:
#         return 0.0
#
# Test passes! (Silly, but valid — TDD builds up gradually.)
#
# --- ROUND 2: RED ---
# Add a new test for the next behaviour:
#
#     def test_late_fee_for_three_days():
#         assert calculate_late_fee(3) == 15.0
#
# This FAILS with our current "always return 0.0" implementation.
#
# --- ROUND 2: GREEN ---
# Update the implementation to make BOTH tests pass:
#
#     def calculate_late_fee(days_late: int) -> float:
#         if days_late <= 0:
#             return 0.0
#         return days_late * 5.0
#
# --- ROUND 3: RED ---
# Add a test for the "beyond 7 days" tier:
#
#     def test_late_fee_for_ten_days():
#         assert calculate_late_fee(10) == (7 * 5.0) + (3 * 10.0)  # 65.0
#
# This fails with our current implementation (it would return 50.0).
#
# --- ROUND 3: GREEN + REFACTOR ---
# Final implementation that satisfies ALL tests:

def calculate_late_fee(days_late: int) -> float:
    if days_late <= 0:
        return 0.0
    if days_late <= 7:
        return days_late * 5.0
    standard_days = 7
    extra_days = days_late - standard_days
    return (standard_days * 5.0) + (extra_days * 10.0)


# The final test suite, all written BEFORE (or alongside) the final
# implementation, in true TDD spirit:

def test_no_late_fee_when_on_time():
    assert calculate_late_fee(0) == 0.0


def test_late_fee_for_three_days():
    assert calculate_late_fee(3) == 15.0


def test_late_fee_for_exactly_seven_days():
    assert calculate_late_fee(7) == 35.0


def test_late_fee_for_ten_days():
    assert calculate_late_fee(10) == 65.0


def test_negative_days_treated_as_zero():
    # Defensive case discovered DURING refactor — TDD encourages
    # thinking about edge cases as you go.
    assert calculate_late_fee(-2) == 0.0


# ════════════════════════════════════════════════════════════
# SECTION 5: TDD Isn't All-or-Nothing
# ════════════════════════════════════════════════════════════
#
# In real teams, strict Red-Green-Refactor for every single line is
# rare. What DOES carry over broadly:
#   - Writing tests for tricky logic BEFORE fixing a bug (this proves
#     you've reproduced the bug, and proves your fix actually works)
#   - Never marking a feature "done" without a test proving it works
#   - Treating a failing test as a TODO list, not a nuisance


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE: TDD for a Discount Coupon Validator
# ════════════════════════════════════════════════════════════
#
# Requirement from Meera Iyer (marketing team): a coupon code is valid
# only if it starts with "SALE", is followed by exactly 4 digits, and
# the digits form a number less than or equal to 2026 (this year).

def is_valid_coupon(code: str) -> bool:
    if not code.startswith("SALE"):
        return False
    digits_part = code[4:]
    if len(digits_part) != 4 or not digits_part.isdigit():
        return False
    return int(digits_part) <= 2026


def test_valid_coupon_code():
    assert is_valid_coupon("SALE2025") is True


def test_coupon_wrong_prefix():
    assert is_valid_coupon("DEAL2025") is False


def test_coupon_wrong_digit_count():
    assert is_valid_coupon("SALE25") is False


def test_coupon_number_too_high():
    assert is_valid_coupon("SALE9999") is False


def test_coupon_non_numeric_suffix():
    assert is_valid_coupon("SALEABCD") is False


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Practise TDD yourself. The requirement: `seat_class(price: float) -> str`
# for an IRCTC-style train booking, where:
#   - price < 500        -> "Sleeper"
#   - 500 <= price < 1500 -> "AC 3-Tier"
#   - 1500 <= price < 2500 -> "AC 2-Tier"
#   - price >= 2500       -> "AC First Class"
#
# 1. Write the tests FIRST (they will fail — that's RED).
# 2. Then write `seat_class()` to make them pass (GREEN).
# 3. Re-read your solution and simplify if possible (REFACTOR).
#
# YOUR CODE HERE (tests first, then implementation)


# ---- SOLUTION ----
# def test_seat_class_sleeper():
#     assert seat_class(300) == "Sleeper"
#
# def test_seat_class_ac_3_tier():
#     assert seat_class(800) == "AC 3-Tier"
#
# def test_seat_class_ac_2_tier():
#     assert seat_class(2000) == "AC 2-Tier"
#
# def test_seat_class_ac_first():
#     assert seat_class(3000) == "AC First Class"
#
# def seat_class(price: float) -> str:
#     if price < 500:
#         return "Sleeper"
#     elif price < 1500:
#         return "AC 3-Tier"
#     elif price < 2500:
#         return "AC 2-Tier"
#     else:
#         return "AC First Class"
# Expected: all 4 tests pass


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - What code coverage measures (and its limits)
#   - Running pytest-cov and reading a coverage report
#   - The Red -> Green -> Refactor TDD cycle
#   - A full worked TDD example (late fee calculator)
#   - TDD applied pragmatically, not dogmatically
#
# THIS COMPLETES DAY 20's CONCEPT FILES.
# NEXT: day20_practise_problems_*.py for hands-on practice,
# then Day 21 — Data & NumPy.

if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
