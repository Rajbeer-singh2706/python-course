"""
Day 18 — Practice Problems
File 2 of 3: Optional & Union Types

Cumulative scope: Days 1-18.
Difficulty legend: 🟢 Warm-up | 🟡 Core | 🔴 Challenge

Section index:
    C — Optional & Union Types (5 problems)

How to run:
    python day18_practise_problems_02_optional_union.py
"""

from typing import Optional, Union

print("=" * 50)
print("SECTION C: Optional & Union Types")
print("=" * 50)

# ──────────────────────────────────────────────────────────
# C1. 🟢 Warm-up
# Write a type-hinted function `first_or_none(items: list[str]) -> Optional[str]`
# that returns the first element of the list, or None if the list is empty.
# Test with ["Chennai", "Delhi"] and with [].
# Expected output:
#   Chennai
#   None
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def first_or_none(items: list[str]) -> Optional[str]:
#     return items[0] if items else None
#
# print(first_or_none(["Chennai", "Delhi"]))
# print(first_or_none([]))
# Output:
# Chennai
# None


# ──────────────────────────────────────────────────────────
# C2. 🟢 Warm-up
# Write a type-hinted function `greet(name: Optional[str]) -> str` that
# returns f"Hello, {name}!" if name is not None, otherwise returns
# "Hello, stranger!". Test with "Riya Deshmukh" and with None.
# Expected output:
#   Hello, Riya Deshmukh!
#   Hello, stranger!
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def greet(name: Optional[str]) -> str:
#     if name is None:
#         return "Hello, stranger!"
#     return f"Hello, {name}!"
#
# print(greet("Riya Deshmukh"))
# print(greet(None))
# Output:
# Hello, Riya Deshmukh!
# Hello, stranger!


# ──────────────────────────────────────────────────────────
# C3. 🟡 Core
# Write a type-hinted function `to_rupees(amount: Union[int, str]) -> str`
# that formats an amount (which may arrive as int paise-free rupees, or
# as a numeric string) into "Rs. <amount>.00". Test with 500 and "1250".
# Expected output:
#   Rs. 500.00
#   Rs. 1250.00
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def to_rupees(amount: Union[int, str]) -> str:
#     return f"Rs. {int(amount)}.00"
#
# print(to_rupees(500))
# print(to_rupees("1250"))
# Output:
# Rs. 500.00
# Rs. 1250.00


# ──────────────────────────────────────────────────────────
# C4. 🟡 Core
# Write a type-hinted function `lookup_student(roll_no: int, records: dict[int, str]) -> str | None`
# using the modern `|` syntax. Return the student's name if found, else None.
# Test with records = {101: "Sanjay Verma", 102: "Meera Iyer"},
# looking up roll_no 101 and roll_no 999.
# Expected output:
#   Sanjay Verma
#   None
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def lookup_student(roll_no: int, records: dict[int, str]) -> str | None:
#     return records.get(roll_no)
#
# records = {101: "Sanjay Verma", 102: "Meera Iyer"}
# print(lookup_student(101, records))
# print(lookup_student(999, records))
# Output:
# Sanjay Verma
# None


# ──────────────────────────────────────────────────────────
# C5. 🔴 Challenge
# Write a type-hinted function `combine_contacts(primary: Optional[str], backup: Optional[str]) -> Optional[str]`
# that returns primary if it is not None, else returns backup if that is
# not None, else returns None. Test all three combinations:
#   combine_contacts("9876543210", "9123456780")
#   combine_contacts(None, "9123456780")
#   combine_contacts(None, None)
# Expected output:
#   9876543210
#   9123456780
#   None
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def combine_contacts(primary: Optional[str], backup: Optional[str]) -> Optional[str]:
#     if primary is not None:
#         return primary
#     if backup is not None:
#         return backup
#     return None
#
# print(combine_contacts("9876543210", "9123456780"))
# print(combine_contacts(None, "9123456780"))
# print(combine_contacts(None, None))
# Output:
# 9876543210
# 9123456780
# None


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Section C: 5 problems covering Optional[X], Union[X, Y], the modern
# X | Y / X | None syntax, and chained None-fallback logic.
#
# Continue to file 3 for TypeVar/Generics practice, which also contains
# the Mixed Challenges section (Section E) combining all of Day 18.

if __name__ == "__main__":
    pass
