"""
Day 11 — Object-Oriented Programming II
Practice Problems — File 2 of 3: Polymorphism & Encapsulation

Cumulative scope: Days 1-11 (Setup through OOP II)

Difficulty legend:
    🟢 Warm-up   — straightforward, single-concept
    🟡 Core      — typical exam/interview level
    🔴 Challenge — combines multiple ideas or edge cases

Section index in this file:
    Section C — Polymorphism & Encapsulation

How to run:
    python day11_practise_problems_02_encapsulation_polymorphism.py
"""

# ════════════════════════════════════════════════════════════
# SECTION C: Polymorphism & Encapsulation
# ════════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION C: Polymorphism & Encapsulation")
print("=" * 50)

# ── Problem C1 ──
# 🟢 Warm-up
# Create two classes, `Dog` and `Cat`, each with a method `sound()`
# returning "Woof" and "Meow" respectively. Loop over a list containing
# one of each and print the result of calling sound() on each.

# YOUR CODE HERE


class DogSolutionC1:
    def sound(self):
        return "Woof"


class CatSolutionC1:
    def sound(self):
        return "Meow"


# SOLUTION:
# for animal in [DogSolutionC1(), CatSolutionC1()]:
#     print(animal.sound())
# Expected output:
# Woof
# Meow

print("-" * 50)

# ── Problem C2 ──
# 🟢 Warm-up
# Create a class `Wallet` with a private attribute `__amount` initialised
# to 0 in `__init__`. Add a method `add(value)` that increases `__amount`,
# and a method `get_amount()` that returns it.

amount_to_add = 250  # simulating input()

# YOUR CODE HERE


class WalletSolutionC2:
    def __init__(self):
        self.__amount = 0

    def add(self, value):
        self.__amount += value

    def get_amount(self):
        return self.__amount


# SOLUTION:
# my_wallet = WalletSolutionC2()
# my_wallet.add(amount_to_add)
# print(my_wallet.get_amount())
# Expected output: 250

print("-" * 50)

# ── Problem C3 ──
# 🟡 Core
# Create a class `Discount` with a private attribute `__percent`. Use
# `@property` to create a getter `percent` and a setter that raises
# ValueError if the value is not between 0 and 100.

percent_value = 15  # simulating input()
invalid_percent_value = 120  # simulating input()

# YOUR CODE HERE


class DiscountSolutionC3:
    def __init__(self, percent):
        self.percent = percent  # uses the setter for validation

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Percent must be between 0 and 100")
        self.__percent = value


# SOLUTION:
# festival_discount = DiscountSolutionC3(percent_value)
# print(festival_discount.percent)
# Expected output: 15
# try:
#     festival_discount.percent = invalid_percent_value
# except ValueError as error:
#     print(error)
# Expected output: Percent must be between 0 and 100

print("-" * 50)

# ── Problem C4 ──
# 🟡 Core
# Create an abstract-style base class `Instrument` with a method `play()`
# that raises NotImplementedError. Create `Sitar` and `Tabla` subclasses
# that override `play()` with their own strings. Write a function
# `perform(instruments)` that loops through a list and prints each
# play() result. (Polymorphism via overriding)

# YOUR CODE HERE


class InstrumentSolutionC4:
    def play(self):
        raise NotImplementedError


class SitarSolutionC4(InstrumentSolutionC4):
    def play(self):
        return "Sitar: plucking strings, a melodic raga begins"


class TablaSolutionC4(InstrumentSolutionC4):
    def play(self):
        return "Tabla: rhythmic beats fill the room"


def perform_solution_c4(instruments):
    for instrument in instruments:
        print(instrument.play())


# SOLUTION:
# perform_solution_c4([SitarSolutionC4(), TablaSolutionC4()])
# Expected output:
# Sitar: plucking strings, a melodic raga begins
# Tabla: rhythmic beats fill the room

print("-" * 50)

# ── Problem C5 ──
# 🔴 Challenge
# Create a class `Account` with private `__pin` and `__balance`. Add a
# method `withdraw(pin, amount)` that only succeeds (deducts and returns
# new balance) if the pin matches AND amount <= balance; otherwise it
# should raise a ValueError with an appropriate message in each failing
# case ("Incorrect PIN" or "Insufficient funds").

correct_pin, wrong_pin = 4321, 1111  # simulating input()
starting_balance, withdraw_amount = 3000, 5000  # simulating input()

# YOUR CODE HERE


class AccountSolutionC5:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def withdraw(self, pin, amount):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance


# SOLUTION:
# test_account = AccountSolutionC5(correct_pin, starting_balance)
# try:
#     test_account.withdraw(wrong_pin, 500)
# except ValueError as error:
#     print(error)
# Expected output: Incorrect PIN
# try:
#     test_account.withdraw(correct_pin, withdraw_amount)
# except ValueError as error:
#     print(error)
# Expected output: Insufficient funds


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: C (Polymorphism & Encapsulation)
# Difficulty breakdown: 2 Warm-up, 2 Core, 1 Challenge = 5 problems
#
# Next file (day11_practise_problems_03_dunder_mixed.py) covers:
#   Section D — Dunder Methods
#   Section E — Mixed Challenges (combines Days 1-11)

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11 Practice Problems, File 2 complete")
