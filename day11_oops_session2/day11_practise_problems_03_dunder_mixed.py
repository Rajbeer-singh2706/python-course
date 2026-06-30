"""
Day 11 — Object-Oriented Programming II
Practice Problems — File 3 of 3: Dunder Methods + Mixed Challenges

Cumulative scope: Days 1-11 (Setup through OOP II)

Difficulty legend:
    🟢 Warm-up   — straightforward, single-concept
    🟡 Core      — typical exam/interview level
    🔴 Challenge — combines multiple ideas or edge cases

Section index in this file:
    Section D — Dunder Methods
    Section E — Mixed Challenges (combines Days 1-11)

How to run:
    python day11_practise_problems_03_dunder_mixed.py
"""

# ════════════════════════════════════════════════════════════
# SECTION D: Dunder Methods
# ════════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION D: Dunder Methods")
print("=" * 50)

# ── Problem D1 ──
# 🟢 Warm-up
# Create a class `Coupon` with attribute `code`. Add a `__str__` method
# returning f"Coupon: {self.code}".

coupon_code = "DIWALI50"  # simulating input()

# YOUR CODE HERE


class CouponSolutionD1:
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return f"Coupon: {self.code}"


# SOLUTION:
# diwali_coupon = CouponSolutionD1(coupon_code)
# print(diwali_coupon)
# Expected output: Coupon: DIWALI50

print("-" * 50)

# ── Problem D2 ──
# 🟢 Warm-up
# Create a class `Cart` that stores a list of items. Implement `__len__`
# to return the number of items in the cart.

cart_items = ["Rice", "Dal", "Atta", "Sugar"]  # simulating input()

# YOUR CODE HERE


class CartSolutionD2:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


# SOLUTION:
# grocery_cart = CartSolutionD2(cart_items)
# print(len(grocery_cart))
# Expected output: 4

print("-" * 50)

# ── Problem D3 ──
# 🟡 Core
# Create a class `Point` with `x` and `y`. Implement `__eq__` so two
# Points are equal if both x and y match, and `__str__` returning
# f"({x}, {y})".

x1, y1, x2, y2 = 3, 4, 3, 4  # simulating input()

# YOUR CODE HERE


class PointSolutionD3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


# SOLUTION:
# point_a = PointSolutionD3(x1, y1)
# point_b = PointSolutionD3(x2, y2)
# print(point_a == point_b)
# Expected output: True

print("-" * 50)

# ── Problem D4 ──
# 🟡 Core
# Create a class `Distance` (kilometres) with `__add__` that returns a
# new Distance whose value is the sum, and `__lt__` for comparison.
# Implement `__str__` returning f"{value} km".

distance_one, distance_two = 12.5, 7.3  # simulating input()

# YOUR CODE HERE


class DistanceSolutionD4:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        return DistanceSolutionD4(self.km + other.km)

    def __lt__(self, other):
        return self.km < other.km

    def __str__(self):
        return f"{self.km} km"


# SOLUTION:
# trip_one = DistanceSolutionD4(distance_one)
# trip_two = DistanceSolutionD4(distance_two)
# print(trip_one + trip_two)
# Expected output: 19.8 km
# print(trip_two < trip_one)
# Expected output: True

print("-" * 50)

# ── Problem D5 ──
# 🔴 Challenge
# Create a class `Matrix2x2` storing four numbers (a, b, c, d) arranged
# as [[a, b], [c, d]]. Implement `__add__` (element-wise addition
# returning a new Matrix2x2), `__eq__` (all four elements match), and
# `__str__` returning f"[[a, b], [c, d]]" with actual values.

matrix_one = (1, 2, 3, 4)  # simulating input()
matrix_two = (5, 6, 7, 8)  # simulating input()

# YOUR CODE HERE


class Matrix2x2SolutionD5:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def __add__(self, other):
        return Matrix2x2SolutionD5(
            self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d
        )

    def __eq__(self, other):
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)

    def __str__(self):
        return f"[[{self.a}, {self.b}], [{self.c}, {self.d}]]"


# SOLUTION:
# matrix_a = Matrix2x2SolutionD5(*matrix_one)
# matrix_b = Matrix2x2SolutionD5(*matrix_two)
# print(matrix_a + matrix_b)
# Expected output: [[6, 8], [10, 12]]


# ════════════════════════════════════════════════════════════
# SECTION E: Mixed Challenges (Days 1-11)
# ════════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION E: Mixed Challenges")
print("=" * 50)

# ── Problem E1 ──
# 🔴 Challenge
# Build a small class hierarchy for a library system:
#   - `LibraryItem` (base): __init__(title, item_id), __str__ returns
#     f"[{item_id}] {title}"
#   - `Book(LibraryItem)`: adds `author`, overrides __str__ to append
#     f" by {author}"
#   - `DVD(LibraryItem)`: adds `duration_minutes`, overrides __str__ to
#     append f" ({duration_minutes} min)"
# Store a list of mixed Book and DVD objects and print each using a
# polymorphic loop (Day 11 inheritance + polymorphism + Day 6 lists).

# YOUR CODE HERE


class LibraryItemSolutionE1:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def __str__(self):
        return f"[{self.item_id}] {self.title}"


class BookSolutionE1(LibraryItemSolutionE1):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def __str__(self):
        return f"{super().__str__()} by {self.author}"


class DVDSolutionE1(LibraryItemSolutionE1):
    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"{super().__str__()} ({self.duration_minutes} min)"


# SOLUTION:
# library_catalog = [
#     BookSolutionE1("Sapiens", "LIB001", "Yuval Noah Harari"),
#     DVDSolutionE1("3 Idiots", "LIB002", 170),
# ]
# for item in library_catalog:
#     print(item)
# Expected output:
# [LIB001] Sapiens by Yuval Noah Harari
# [LIB002] 3 Idiots (170 min)

print("-" * 50)

# ── Problem E2 ──
# 🔴 Challenge
# Build a `Product` class with private `__price` (validated to be >= 0
# via @property setter), and a `__str__` returning
# f"{name}: Rs.{price}". Build a `Cart` class (Day 6 lists + Day 11 OOP)
# that holds a list of Products, with `__len__` returning item count and
# a method `total()` summing all product prices using a for loop AND
# error handling (Day 9) to skip any product whose price attribute
# access raises an exception (simulate by including a plain object with
# no `price` attribute in the list).

# YOUR CODE HERE


class ProductSolutionE2:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # uses setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    def __str__(self):
        return f"{self.name}: Rs.{self.price}"


class CartSolutionE2:
    def __init__(self, products):
        self.products = products

    def __len__(self):
        return len(self.products)

    def total(self):
        running_total = 0
        for product in self.products:
            try:
                running_total += product.price
            except AttributeError:
                continue  # skip invalid items instead of crashing
        return running_total


# SOLUTION:
# class NotAProduct:
#     pass
#
# shopping_cart = CartSolutionE2([
#     ProductSolutionE2("Notebook", 60),
#     ProductSolutionE2("Pen", 10),
#     NotAProduct(),  # deliberately broken entry
# ])
# print(len(shopping_cart))
# Expected output: 3
# print(shopping_cart.total())
# Expected output: 70

print("-" * 50)

# ── Problem E3 ──
# 🔴 Challenge
# Combine inheritance, encapsulation, and dunder methods: build a
# `Currency` base class storing a private `__amount` and a `code`
# (e.g. "INR"). Implement `@property amount`, `__str__` returning
# f"{amount} {code}", `__add__` that only allows adding two Currency
# objects with the SAME code (raise ValueError otherwise), and `__eq__`
# comparing both amount and code. Create a child class `Rupee(Currency)`
# whose __init__ always sets code="INR".

amount_one, amount_two = 500, 250  # simulating input()

# YOUR CODE HERE


class CurrencySolutionE3:
    def __init__(self, amount, code):
        self.__amount = amount
        self.code = code

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"{self.amount} {self.code}"

    def __add__(self, other):
        if self.code != other.code:
            raise ValueError("Cannot add different currencies")
        return CurrencySolutionE3(self.amount + other.amount, self.code)

    def __eq__(self, other):
        return self.amount == other.amount and self.code == other.code


class RupeeSolutionE3(CurrencySolutionE3):
    def __init__(self, amount):
        super().__init__(amount, code="INR")


# SOLUTION:
# rupee_one = RupeeSolutionE3(amount_one)
# rupee_two = RupeeSolutionE3(amount_two)
# print(rupee_one + rupee_two)
# Expected output: 750 INR


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: D (Dunder Methods), E (Mixed Challenges)
# Difficulty breakdown: 2 Warm-up, 2 Core, 4 Challenge = 8 problems
#
# Combined across all 3 practice files for Day 11:
#   File 1 (Section A + B): 9 problems
#   File 2 (Section C):      5 problems
#   File 3 (Section D + E):  8 problems
#   TOTAL: 22 problems (within the 16-20+ target range for a content-dense day)
#
# Next session preview (Day 12 — Modules & Packages):
#   import / from...import, pip & uv add, __main__ guard,
#   os, sys, math, datetime, pathlib

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11 Practice Problems, File 3 complete — Day 11 problem set finished")
