"""
Day 20 — Testing (Part 1: unittest Basics)
============================================

WHAT THIS FILE COVERS:
    - Why we test code at all
    - The `unittest` module — TestCase classes
    - Writing test methods (must start with `test_`)
    - Common assertion methods (assertEqual, assertTrue, assertRaises, etc.)
    - Grouping tests into a TestSuite
    - Running tests from the command line

PREREQUISITES:
    - Day 9  — Error Handling (try/except, custom exceptions)
    - Day 10/11 — OOP (classes, methods, inheritance)
    - Day 17 — Advanced OOP (dataclasses)
    - Day 18 — Type Hints

HOW TO RUN:
    python day20_01_unittest_basics.py
    (or, once you know pytest: pytest day20_01_unittest_basics.py -v)
"""

import unittest


# ════════════════════════════════════════════════════════════
# SECTION 1: Why Do We Test?
# ════════════════════════════════════════════════════════════
#
# Imagine Priya Sharma is building a billing module for a Swiggy-style
# food delivery app. Every time she changes the discount logic, she
# needs to be SURE she hasn't broken anything else. Manually re-checking
# every scenario by hand is slow and error-prone.
#
# A "test" is simply a small piece of code that:
#   1. Calls your function/class with known inputs
#   2. Checks that the output matches what you EXPECT
#   3. Reports pass/fail automatically
#
# Once you have a suite of tests, you can run all of them in seconds
# every time you make a change — this is called a "regression test suite."


def apply_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a percentage discount."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")
    final_price = price - (price * discount_percent / 100)
    return round(final_price, 2)


# Quick manual check (this is what we DON'T want to keep doing by hand):
print("Manual check:", apply_discount(500, 10))
# Output: Manual check: 450.0


# ════════════════════════════════════════════════════════════
# SECTION 2: Writing Your First unittest.TestCase
# ════════════════════════════════════════════════════════════
#
# `unittest` is Python's built-in testing framework (no install needed).
# The core building block is a class that inherits from `unittest.TestCase`.
# Every method whose name starts with `test_` is treated as a separate test.


class TestApplyDiscount(unittest.TestCase):
    """Tests for the apply_discount() function."""

    def test_ten_percent_discount(self):
        # assertEqual(actual, expected) — the most common assertion
        result = apply_discount(500, 10)
        self.assertEqual(result, 450.0)

    def test_zero_percent_discount(self):
        result = apply_discount(1000, 0)
        self.assertEqual(result, 1000.0)

    def test_full_discount(self):
        result = apply_discount(750, 100)
        self.assertEqual(result, 0.0)

    def test_negative_discount_raises_error(self):
        # assertRaises checks that a specific exception is thrown
        with self.assertRaises(ValueError):
            apply_discount(500, -5)

    def test_over_hundred_percent_raises_error(self):
        with self.assertRaises(ValueError):
            apply_discount(500, 150)


# ════════════════════════════════════════════════════════════
# SECTION 3: Common Assertion Methods Reference
# ════════════════════════════════════════════════════════════
#
#   assertEqual(a, b)        -> a == b
#   assertNotEqual(a, b)     -> a != b
#   assertTrue(x)            -> bool(x) is True
#   assertFalse(x)           -> bool(x) is False
#   assertIsNone(x)          -> x is None
#   assertIsNotNone(x)       -> x is not None
#   assertIn(a, b)           -> a in b
#   assertNotIn(a, b)        -> a not in b
#   assertRaises(Error)      -> code inside `with` block raises Error
#   assertAlmostEqual(a, b)  -> useful for floating point comparisons
#   assertListEqual(a, b)    -> a == b, with a nicer diff for lists
#   assertDictEqual(a, b)    -> a == b, with a nicer diff for dicts


class Cart:
    """A simple shopping cart used across our examples (Flipkart-style)."""

    def __init__(self):
        self.items: list[dict] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total(self) -> float:
        return round(sum(item["price"] * item["quantity"] for item in self.items), 2)

    def is_empty(self) -> bool:
        return len(self.items) == 0


class TestCart(unittest.TestCase):
    """Tests demonstrating a variety of assertion methods."""

    def setUp(self):
        # setUp() runs BEFORE every single test method in this class.
        # It's the perfect place to build a "fresh" object so tests
        # don't interfere with each other.
        self.cart = Cart()

    def test_new_cart_is_empty(self):
        self.assertTrue(self.cart.is_empty())

    def test_adding_item_makes_cart_not_empty(self):
        self.cart.add_item("Wireless Mouse", 799.0)
        self.assertFalse(self.cart.is_empty())

    def test_total_with_single_item(self):
        self.cart.add_item("Bluetooth Speaker", 1499.0, quantity=2)
        self.assertEqual(self.cart.total(), 2998.0)

    def test_total_with_multiple_items(self):
        self.cart.add_item("Notebook", 60.0, quantity=3)
        self.cart.add_item("Pen Set", 120.0)
        self.assertAlmostEqual(self.cart.total(), 300.0)

    def test_item_name_in_cart(self):
        self.cart.add_item("USB Cable", 199.0)
        item_names = [item["name"] for item in self.cart.items]
        self.assertIn("USB Cable", item_names)

    def tearDown(self):
        # tearDown() runs AFTER every test method — good for cleanup
        # (closing files, disconnecting from a test database, etc.)
        self.cart = None


# ════════════════════════════════════════════════════════════
# SECTION 4: setUpClass / tearDownClass (Run Once Per Class)
# ════════════════════════════════════════════════════════════
#
# Unlike setUp/tearDown (which run before/after EVERY test),
# setUpClass/tearDownClass run ONCE for the whole class — useful
# for expensive setup like opening a database connection.


class TestExpensiveResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[setUpClass] Connecting to mock Razorpay sandbox... (runs once)")
        cls.shared_connection = {"status": "connected", "gateway": "razorpay-sandbox"}

    @classmethod
    def tearDownClass(cls):
        print("[tearDownClass] Closing mock Razorpay sandbox connection... (runs once)")

    def test_connection_status(self):
        self.assertEqual(self.shared_connection["status"], "connected")

    def test_connection_gateway(self):
        self.assertEqual(self.shared_connection["gateway"], "razorpay-sandbox")


# ════════════════════════════════════════════════════════════
# SECTION 5: Building a TestSuite Manually
# ════════════════════════════════════════════════════════════
#
# Usually `unittest.main()` auto-discovers tests for you. But you can
# also build a suite explicitly — handy when you only want to run a
# subset of tests.


def build_custom_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTest(TestApplyDiscount("test_ten_percent_discount"))
    suite.addTest(TestApplyDiscount("test_full_discount"))
    return suite


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE: Testing a Student Grading Function
# ════════════════════════════════════════════════════════════

def grade_for_marks(marks: int) -> str:
    """Return a letter grade for Arjun Mehta's exam marks (out of 100)."""
    if not 0 <= marks <= 100:
        raise ValueError("marks must be between 0 and 100")
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


class TestGradeForMarks(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(grade_for_marks(95), "A")

    def test_grade_b(self):
        self.assertEqual(grade_for_marks(80), "B")

    def test_grade_c(self):
        self.assertEqual(grade_for_marks(65), "C")

    def test_grade_d(self):
        self.assertEqual(grade_for_marks(40), "D")

    def test_boundary_ninety_is_a(self):
        # Boundary testing — always check the EDGE of a condition
        self.assertEqual(grade_for_marks(90), "A")

    def test_invalid_marks_raises(self):
        with self.assertRaises(ValueError):
            grade_for_marks(150)


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Riya Deshmukh wants a function `is_valid_pincode(pincode: str) -> bool`
# that returns True only if the pincode is exactly 6 digits, all numeric,
# and does not start with "0".
#
# 1. Write the function.
# 2. Write a TestCase class with at least 4 tests covering:
#    - a valid pincode (e.g. "411045" — Pune)
#    - a pincode that is too short
#    - a pincode starting with "0"
#    - a pincode containing letters
#
# YOUR CODE HERE


# ---- SOLUTION ----
# def is_valid_pincode(pincode: str) -> bool:
#     return (
#         len(pincode) == 6
#         and pincode.isdigit()
#         and pincode[0] != "0"
#     )
#
#
# class TestIsValidPincode(unittest.TestCase):
#     def test_valid_pincode(self):
#         self.assertTrue(is_valid_pincode("411045"))
#
#     def test_too_short(self):
#         self.assertFalse(is_valid_pincode("4110"))
#
#     def test_starts_with_zero(self):
#         self.assertFalse(is_valid_pincode("041104"))
#
#     def test_contains_letters(self):
#         self.assertFalse(is_valid_pincode("41A045"))
# Expected: all 4 tests pass (OK)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Why automated tests beat manual checking
#   - unittest.TestCase, test_ methods, and core assertions
#   - setUp/tearDown (per-test) vs setUpClass/tearDownClass (per-class)
#   - Building a TestSuite manually
#
# NEXT FILE: day20_02_pytest_basics.py
#   -> The pytest framework: simpler syntax, auto-discovery,
#      plain `assert` statements, and parametrize.

if __name__ == "__main__":
    unittest.main(verbosity=2)
