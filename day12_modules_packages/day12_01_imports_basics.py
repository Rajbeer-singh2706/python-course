"""
Day 12 — Modules & Packages (Part 1 of 3)
==========================================

Topic   : Import statements, from...import, and installing packages
Covers  : import module, from module import name, import as alias,
          installing third-party packages with pip / uv add
Prereqs : Day 1 (environment setup), Day 9 (error handling), Day 11 (OOP II)
Run with: python day12_01_imports_basics.py

WHAT IS A MODULE?
A module is simply a .py file containing Python code (functions, classes,
variables) that you can reuse in other files. A PACKAGE is a folder of
modules (with an __init__.py file, historically required, optional since
Python 3.3) that lets you organise related modules together.

Today, Priya and Arjun are organising a small Mumbai grocery delivery
script, and they need to start pulling in code from Python's standard
library instead of reinventing everything from scratch.
"""

# ════════════════════════════════════════════════════════════════
# SECTION 1: THE BASIC `import` STATEMENT
# ════════════════════════════════════════════════════════════════

# ── Concept: import module ──
# `import module_name` loads the ENTIRE module. To use anything inside it,
# you must prefix it with the module name, e.g. math.sqrt(), os.getcwd().
import math

print("── Basic import ──")
radius = 7
area = math.pi * radius ** 2
print(f"Area of a circle with radius {radius} cm: {area:.2f} sq cm")
# Output: Area of a circle with radius 7 cm: 153.94 sq cm

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: `from ... import ...`
# ════════════════════════════════════════════════════════════════

# ── Concept: from module import name ──
# This pulls a SPECIFIC name out of a module, so you can use it directly
# without the module prefix. Useful when you only need one or two things.
from math import sqrt, floor, ceil

print("── from...import ──")
bill_amount = 487.30
print(f"Square root of 487.30: {sqrt(bill_amount):.2f}")
print(f"Rounded down (floor): {floor(bill_amount)}")
print(f"Rounded up (ceil): {ceil(bill_amount)}")
# Output:
# Square root of 487.30: 22.07
# Rounded down (floor): 487
# Rounded up (ceil): 488

print("-" * 50)

# ── Concept: from module import * (AVOID in real code) ──
# This imports EVERYTHING from a module into your current namespace.
# It is convenient but DANGEROUS — it can silently overwrite your own
# variables/functions and makes it unclear where a name came from.
# Shown here only so you recognise it; do not use it in production code.
#
#   from math import *      # avoid this style
#   print(pi)                # works, but where did `pi` come from?

print("── Why `import *` is risky (demo, not used) ──")
print("Use explicit imports like 'from math import pi' instead of 'import *'")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: ALIASING WITH `as`
# ════════════════════════════════════════════════════════════════

# ── Concept: import module as alias ──
# Gives a module (or a specific import) a shorter or conventional nickname.
# This is extremely common with popular libraries, e.g. `import pandas as pd`.
import datetime as dt

print("── Import aliasing ──")
delivery_date = dt.date(2025, 6, 30)
print(f"Delivery scheduled for: {delivery_date}")
# Output: Delivery scheduled for: 2025-06-30

from math import factorial as fact

orders_to_arrange = 5
print(f"Ways to arrange {orders_to_arrange} delivery orders: {fact(orders_to_arrange)}")
# Output: Ways to arrange 5 delivery orders: 120

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 4: INSTALLING THIRD-PARTY PACKAGES
# ════════════════════════════════════════════════════════════════

# ── Concept: pip vs uv add ──
# `math`, `os`, `datetime` etc. ship with Python — no installation needed.
# To use code OTHER people have published (like `requests` or `rich`),
# you must install it first into your virtual environment.
#
# Using pip (classic):
#     pip install requests
#
# Using uv (the modern tool we set up on Day 1 — faster, manages
# pyproject.toml dependencies automatically):
#     uv add requests
#
# Once installed, you import it exactly like a standard library module:
#     import requests
#
# NOTE: This file does not install anything automatically — installing
# packages is something YOU run once in your terminal, not inside a script.

print("── Installing packages (reference only, not executed) ──")
print("Terminal command (pip):  pip install requests")
print("Terminal command (uv):   uv add requests")
print("Then in code:            import requests")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Mumbai Grocery Delivery Script
# ════════════════════════════════════════════════════════════════

print("── Guided Example 1: Mixing import styles ──")
import os                      # full module import
from datetime import datetime  # specific import
import random as rnd           # aliased import

customer_name = "Riya Deshmukh"
order_id = rnd.randint(1000, 9999)
order_time = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"Order #{order_id} placed by {customer_name} at {order_time}")

print("-" * 50)

print("── Guided Example 2: Using math for delivery cost calculation ──")
distance_km = 8.4
base_fare = 25
per_km_rate = 6.5
total_fare = base_fare + math.ceil(distance_km) * per_km_rate
print(f"Distance: {distance_km} km -> Total delivery fare: Rs.{total_fare:.2f}")
# Output: Distance: 8.4 km -> Total delivery fare: Rs.83.50

print("-" * 50)

print("── Guided Example 3: Current working directory with os ──")
current_dir = os.getcwd()
print(f"Script is running from: {current_dir}")

print("-" * 50)

print("── Guided Example 4: Aliased random for order assignment ──")
delivery_partners = ["Arjun", "Kabir", "Sanjay", "Vikram"]
assigned_partner = rnd.choice(delivery_partners)
print(f"Order #{order_id} assigned to delivery partner: {assigned_partner}")

print("-" * 50)

print("── Guided Example 5: Combining everything ──")
orders = [
    {"id": rnd.randint(1000, 9999), "amount": 320.50},
    {"id": rnd.randint(1000, 9999), "amount": 145.00},
    {"id": rnd.randint(1000, 9999), "amount": 980.75},
]
total_revenue = sum(order["amount"] for order in orders)
average_order = total_revenue / len(orders)
print(f"Total orders today: {len(orders)}")
print(f"Total revenue: Rs.{total_revenue:.2f}")
print(f"Average order value: Rs.{average_order:.2f}")
print(f"Square root of total revenue (just for fun): {sqrt(total_revenue):.2f}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Using ONLY the imports already available in this file (math, os,
# datetime as dt, datetime.datetime, random as rnd):
#
# 1. Create a variable `pickup_time` set to the current datetime.
# 2. Generate a random "estimated delivery minutes" between 20 and 60.
# 3. Calculate the estimated delivery time by adding those minutes to
#    pickup_time (hint: use dt.timedelta(minutes=...)).
# 4. Print a sentence like:
#    "Picked up at 14:05, estimated delivery by 14:42 (37 mins)"
#
# Expected output (your numbers will vary since they are random):
#    Picked up at <time>, estimated delivery by <time> (<N> mins)

# YOUR CODE HERE
pickup_time = datetime.now()
estimated_minutes = rnd.randint(20, 60)
delivery_time = pickup_time + dt.timedelta(minutes=estimated_minutes)
print(
    f"Picked up at {pickup_time.strftime('%H:%M')}, "
    f"estimated delivery by {delivery_time.strftime('%H:%M')} "
    f"({estimated_minutes} mins)"
)

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Covered in this file:
#   - `import module` for full-module access (math.sqrt)
#   - `from module import name` for direct access (sqrt directly)
#   - Why `from module import *` should be avoided
#   - Aliasing with `as` (import datetime as dt)
#   - Installing third-party packages with pip / uv add
#
# Next up in Part 2: the `if __name__ == "__main__":` guard — why every
# well-written Python file uses it and what problems it prevents.

if __name__ == "__main__":
    print("\nDay 12, Part 1 (Imports & Packages) complete!")
