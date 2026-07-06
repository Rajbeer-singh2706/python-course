"""
Day 18 — Practice Problems
File 1 of 3: Type Hints Basics

Cumulative scope: Days 1-18 (Section A revisits prior days).
Difficulty legend: 🟢 Warm-up | 🟡 Core | 🔴 Challenge

Section index:
    A — Prior Days Review (2 problems)
    B — Type Hints Basics: variables & functions (5 problems)

How to run:
    python day18_practise_problems_01_type_hints_basics.py
"""

print("=" * 50)
print("SECTION A: Prior Days Review")
print("=" * 50)

# ──────────────────────────────────────────────────────────
# A1. 🟢 Warm-up (Day 17 review)
# Create a @dataclass named `Coupon` with fields `code: str` and
# `percent_off: int`. Print the auto-generated repr for
# Coupon("FEST18", 18).
# Expected output:
#   Coupon(code='FEST18', percent_off=18)
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# from dataclasses import dataclass
#
# @dataclass
# class Coupon:
#     code: str
#     percent_off: int
#
# print(Coupon("FEST18", 18))
# Output: Coupon(code='FEST18', percent_off=18)


# ──────────────────────────────────────────────────────────
# A2. 🟢 Warm-up (Day 13 review)
# Write a generator function `countdown(n)` that yields integers
# from n down to 1. Print the results of countdown(3) joined by
# commas using ", ".join(...).
# Expected output:
#   3, 2, 1
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def countdown(n):
#     current = n
#     while current >= 1:
#         yield current
#         current -= 1
#
# print(", ".join(str(x) for x in countdown(3)))
# Output: 3, 2, 1


print("\n" + "=" * 50)
print("SECTION B: Type Hints Basics")
print("=" * 50)

# ──────────────────────────────────────────────────────────
# B1. 🟢 Warm-up
# Write a fully type-hinted function `celsius_to_fahrenheit(celsius: float) -> float`
# that converts Celsius to Fahrenheit using: F = C * 9/5 + 32.
# Print the result for celsius = 30.0.
# Expected output:
#   86.0
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def celsius_to_fahrenheit(celsius: float) -> float:
#     return celsius * 9 / 5 + 32
#
# print(celsius_to_fahrenheit(30.0))
# Output: 86.0


# ──────────────────────────────────────────────────────────
# B2. 🟢 Warm-up
# Annotate three variables: city_name (str) = "Pune", pincode (int) = 411001,
# has_metro (bool) = True. Print all three separated by " | ".
# Expected output:
#   Pune | 411001 | True
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# city_name: str = "Pune"
# pincode: int = 411001
# has_metro: bool = True
# print(f"{city_name} | {pincode} | {has_metro}")
# Output: Pune | 411001 | True


# ──────────────────────────────────────────────────────────
# B3. 🟡 Core
# Write a type-hinted function `merge_names(first: list[str], last: list[str]) -> list[str]`
# that zips two equal-length lists of first and last names and returns
# a list of "First Last" strings.
# Test with first = ["Priya", "Arjun"], last = ["Sharma", "Mehta"].
# Expected output:
#   ['Priya Sharma', 'Arjun Mehta']
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def merge_names(first: list[str], last: list[str]) -> list[str]:
#     return [f"{f} {l}" for f, l in zip(first, last)]
#
# print(merge_names(["Priya", "Arjun"], ["Sharma", "Mehta"]))
# Output: ['Priya Sharma', 'Arjun Mehta']


# ──────────────────────────────────────────────────────────
# B4. 🟡 Core
# Write a type-hinted function `fare_breakdown(distances: dict[str, float]) -> dict[str, float]`
# that takes a dict mapping route name to distance in km, and returns a
# new dict mapping route name to fare, where fare = distance * 12.5 (Rs/km).
# Test with {"Mumbai-Pune": 150.0, "Pune-Nashik": 210.0}.
# Expected output:
#   {'Mumbai-Pune': 1875.0, 'Pune-Nashik': 2625.0}
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def fare_breakdown(distances: dict[str, float]) -> dict[str, float]:
#     return {route: dist * 12.5 for route, dist in distances.items()}
#
# print(fare_breakdown({"Mumbai-Pune": 150.0, "Pune-Nashik": 210.0}))
# Output: {'Mumbai-Pune': 1875.0, 'Pune-Nashik': 2625.0}


# ──────────────────────────────────────────────────────────
# B5. 🔴 Challenge
# Write a type-hinted class `WalletAccount` with:
#   - __init__(self, owner: str, balance: float = 0.0) -> None
#   - deposit(self, amount: float) -> None  (adds to balance)
#   - withdraw(self, amount: float) -> bool  (returns False and does
#     nothing if amount > balance, else subtracts and returns True)
# Create WalletAccount("Meera Iyer", 500.0), deposit 200.0, then
# attempt to withdraw 1000.0 (should fail) and withdraw 300.0
# (should succeed). Print the final balance and both withdraw results.
# Expected output:
#   False
#   True
#   400.0
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class WalletAccount:
#     def __init__(self, owner: str, balance: float = 0.0) -> None:
#         self.owner: str = owner
#         self.balance: float = balance
#
#     def deposit(self, amount: float) -> None:
#         self.balance += amount
#
#     def withdraw(self, amount: float) -> bool:
#         if amount > self.balance:
#             return False
#         self.balance -= amount
#         return True
#
# account = WalletAccount("Meera Iyer", 500.0)
# account.deposit(200.0)
# print(account.withdraw(1000.0))
# print(account.withdraw(300.0))
# print(account.balance)
# Output:
# False
# True
# 400.0


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Section A: 2 problems (Day 17 dataclasses, Day 13 generators)
# Section B: 5 problems (variable/function annotations, collection
#            hints, a fully typed class) — 3 difficulty tiers covered
# Total this file: 7 problems
#
# Continue to file 2 for Optional/Union practice, then file 3 for
# TypeVar/Generics practice plus the Mixed Challenges section.

if __name__ == "__main__":
    pass
