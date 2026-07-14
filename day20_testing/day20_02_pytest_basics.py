"""
Day 20 — Testing (Part 2: pytest Basics)
==========================================

WHAT THIS FILE COVERS:
    - Why most professional Python teams prefer pytest over unittest
    - Writing tests as plain functions (no class needed) with plain `assert`
    - Test discovery rules (`test_*.py`, `test_*` functions)
    - Parametrized tests with `@pytest.mark.parametrize`
    - Grouping related assertions and testing exceptions with pytest.raises
    - Running pytest from the command line

PREREQUISITES:
    - day20_01_unittest_basics.py (same day, previous file)

HOW TO RUN:
    pytest day20_02_pytest_basics.py -v
    (This file also runs standalone with `python day20_02_pytest_basics.py`,
     which uses pytest's programmatic API to execute itself.)

INSTALL:
    pip install pytest --break-system-packages
"""

import sys
import pytest


# ════════════════════════════════════════════════════════════
# SECTION 1: pytest vs unittest — Why Bother?
# ════════════════════════════════════════════════════════════
#
# unittest requires:
#   - A class inheriting from TestCase
#   - self.assertEqual(a, b) style methods
#
# pytest allows:
#   - A plain function
#   - A plain Python `assert` statement
#   - Much clearer failure messages out of the box
#   - Powerful "fixtures" for setup/teardown (see day20_03_fixtures.py)
#
# pytest can still RUN unittest-style tests too — it's a superset,
# which is why most teams migrate to it without rewriting old tests.


def calculate_gst(amount: float, gst_percent: float = 18.0) -> float:
    """Calculate the GST (Goods and Services Tax) amount for a purchase."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    return round(amount * gst_percent / 100, 2)


# ════════════════════════════════════════════════════════════
# SECTION 2: Your First pytest Test — Just a Function!
# ════════════════════════════════════════════════════════════
#
# pytest auto-discovers any function starting with `test_` inside a
# file starting with `test_` or `*_test.py`. (Our files are named
# `dayNN_...py`, so when running with pytest we pass the filename
# explicitly, as shown in the docstring above.)


def test_gst_at_default_rate():
    result = calculate_gst(1000)
    assert result == 180.0          # plain assert — no self.assertEqual needed!


def test_gst_at_custom_rate():
    result = calculate_gst(1000, gst_percent=5)
    assert result == 50.0


def test_gst_zero_amount():
    assert calculate_gst(0) == 0.0


def test_negative_amount_raises_value_error():
    # pytest.raises is the equivalent of unittest's assertRaises
    with pytest.raises(ValueError):
        calculate_gst(-500)


# ════════════════════════════════════════════════════════════
# SECTION 3: Multiple Assertions & Rich Failure Messages
# ════════════════════════════════════════════════════════════
#
# pytest inspects the assert expression itself to build a detailed
# failure report — you don't need special assertEqual/assertIn methods.


def get_swiggy_order_summary(items: list[dict]) -> dict:
    """Summarise a Swiggy order: total items, total cost, has_veg flag."""
    total_cost = sum(item["price"] * item["qty"] for item in items)
    total_items = sum(item["qty"] for item in items)
    has_veg = any(item.get("veg", False) for item in items)
    return {"total_cost": total_cost, "total_items": total_items, "has_veg": has_veg}


def test_order_summary_totals():
    order = [
        {"name": "Paneer Tikka", "price": 220, "qty": 1, "veg": True},
        {"name": "Butter Naan", "price": 45, "qty": 2, "veg": True},
    ]
    summary = get_swiggy_order_summary(order)
    assert summary["total_cost"] == 310
    assert summary["total_items"] == 3
    assert summary["has_veg"] is True


def test_order_summary_no_veg_items():
    order = [{"name": "Chicken Biryani", "price": 260, "qty": 1, "veg": False}]
    summary = get_swiggy_order_summary(order)
    assert summary["has_veg"] is False


# ════════════════════════════════════════════════════════════
# SECTION 4: Parametrized Tests — One Test, Many Inputs
# ════════════════════════════════════════════════════════════
#
# Instead of writing 5 near-identical test functions for 5 inputs,
# `@pytest.mark.parametrize` lets you supply a list of (input, expected)
# pairs and pytest generates one test case per pair automatically.


@pytest.mark.parametrize(
    "amount, gst_percent, expected",
    [
        (1000, 18, 180.0),
        (500, 5, 25.0),
        (0, 18, 0.0),
        (2500, 12, 300.0),
        (100, 28, 28.0),
    ],
)
def test_calculate_gst_parametrized(amount, gst_percent, expected):
    assert calculate_gst(amount, gst_percent) == expected


# You can also parametrize over multiple test IDs for readability:
@pytest.mark.parametrize(
    "city, pincode_prefix",
    [
        ("Mumbai", "40"),
        ("Delhi", "11"),
        ("Bengaluru", "56"),
        ("Pune", "41"),
    ],
)
def test_city_pincode_prefix(city, pincode_prefix):
    known_prefixes = {
        "Mumbai": "40",
        "Delhi": "11",
        "Bengaluru": "56",
        "Pune": "41",
    }
    assert known_prefixes[city] == pincode_prefix


# ════════════════════════════════════════════════════════════
# SECTION 5: Marking & Skipping Tests
# ════════════════════════════════════════════════════════════
#
#   @pytest.mark.skip(reason="...")       -> always skipped
#   @pytest.mark.skipif(condition, reason="...")  -> conditionally skipped
#   @pytest.mark.xfail(reason="...")      -> expected to fail (won't count as failure)


@pytest.mark.skip(reason="IRCTC sandbox API not available in this offline demo")
def test_irctc_live_booking():
    assert False  # would call a real API in production


@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires Python 3.10+ match statement")
def test_requires_modern_python():
    assert sys.version_info >= (3, 10)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE: Testing a BigBasket-style Inventory Checker
# ════════════════════════════════════════════════════════════

def check_stock(inventory: dict, item: str, quantity: int) -> bool:
    """Check if `quantity` units of `item` are available in `inventory`."""
    available = inventory.get(item, 0)
    return available >= quantity


@pytest.mark.parametrize(
    "item, quantity, expected",
    [
        ("Basmati Rice 5kg", 2, True),
        ("Basmati Rice 5kg", 20, False),
        ("Toor Dal 1kg", 1, True),
        ("Almonds 500g", 0, True),      # asking for 0 is always available
        ("Unknown Item", 1, False),     # item not in inventory at all
    ],
)
def test_check_stock(item, quantity, expected):
    inventory = {
        "Basmati Rice 5kg": 10,
        "Toor Dal 1kg": 5,
        "Almonds 500g": 0,
    }
    assert check_stock(inventory, item, quantity) == expected


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Sanjay Verma wants a function `is_strong_password(pw: str) -> bool`
# that returns True only if the password:
#   - is at least 8 characters long
#   - contains at least one digit
#   - contains at least one uppercase letter
#
# 1. Write the function.
# 2. Write a parametrized pytest test with at least 5 cases covering
#    strong passwords and each way a password can be weak.
#
# YOUR CODE HERE


# ---- SOLUTION ----
# def is_strong_password(pw: str) -> bool:
#     return (
#         len(pw) >= 8
#         and any(ch.isdigit() for ch in pw)
#         and any(ch.isupper() for ch in pw)
#     )
#
#
# @pytest.mark.parametrize(
#     "password, expected",
#     [
#         ("Mumbai2024", True),
#         ("short1A", False),        # too short
#         ("nouppercase1", False),   # no uppercase
#         ("NoDigitsHere", False),   # no digit
#         ("Delhi@2025Win", True),
#     ],
# )
# def test_is_strong_password(password, expected):
#     assert is_strong_password(password) == expected
# Expected: all 5 parametrized cases pass


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Plain-function tests with plain `assert` (no TestCase class needed)
#   - pytest.raises() for exception testing
#   - @pytest.mark.parametrize for data-driven tests
#   - skip / skipif / xfail markers
#
# NEXT FILE: day20_03_fixtures.py
#   -> pytest fixtures: reusable setup/teardown, fixture scopes,
#      and dependency injection into test functions.

if __name__ == "__main__":
    # Run this file's tests via pytest's programmatic API.
    sys.exit(pytest.main([__file__, "-v"]))
