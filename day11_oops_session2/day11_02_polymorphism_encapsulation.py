"""
Day 11 — Object-Oriented Programming II
File 2 of 3: Polymorphism & Encapsulation

What this file covers:
    - Polymorphism: the same method name behaving differently per class
    - Duck typing in Python
    - Encapsulation: protecting internal state with naming conventions
    - The single-underscore "protected" convention
    - The double-underscore "name mangling" convention
    - The @property decorator for controlled attribute access

Prerequisites:
    - Day 10: Classes, objects, __init__, self
    - Day 11 File 1: Inheritance & super()

How to run:
    python day11_02_polymorphism_encapsulation.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: Polymorphism — One Interface, Many Forms
# ════════════════════════════════════════════════════════════
# "Polymorphism" means "many shapes". In OOP it means: different classes
# can define a method with the SAME NAME, and Python will call the right
# version automatically depending on which object you're using.

print("=" * 50)
print("SECTION 1: Polymorphism With Method Overriding")
print("=" * 50)


class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid Rs.{amount} via UPI"


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid Rs.{amount} via Credit Card"


class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid Rs.{amount} in Cash"


# ── Concept: Polymorphic Loop ──
# We can put different objects in one list and call the SAME method name
# on each. Python figures out which class's version to run.
payment_methods = [UPIPayment(), CardPayment(), CashPayment()]

for method in payment_methods:
    print(method.pay(500))
# Output:
# Paid Rs.500 via UPI
# Paid Rs.500 via Credit Card
# Paid Rs.500 in Cash


# ── Concept: Duck Typing ──
# Python doesn't require objects to share a parent class to be used
# polymorphically — "If it walks like a duck and quacks like a duck..."
# As long as an object HAS a .pay() method, it works in our loop above.

print("-" * 50)
print("SECTION 2: Duck Typing")
print("-" * 50)


class GiftVoucher:
    """Not related to PaymentMethod at all, but has a pay() method."""

    def pay(self, amount):
        return f"Redeemed gift voucher worth Rs.{amount}"


mixed_methods = payment_methods + [GiftVoucher()]
for method in mixed_methods:
    print(method.pay(200))
# Output includes the GiftVoucher line too — Python doesn't care about
# the class hierarchy, only that .pay() exists.


# ════════════════════════════════════════════════════════════
# SECTION 3: Encapsulation — Protecting Internal State
# ════════════════════════════════════════════════════════════
# Encapsulation means bundling data and the methods that operate on it,
# and restricting direct outside access to that data.

print("-" * 50)
print("SECTION 3: Public, Protected, and Private Attributes")
print("-" * 50)


class BankAccount:
    """Demonstrates Python's three attribute visibility conventions."""

    def __init__(self, owner, balance):
        self.owner = owner             # public: freely accessible
        self._account_notes = []       # protected (convention only): "internal use"
        self.__balance = balance       # private: name-mangled, harder to access directly

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self._account_notes.append(f"Deposited Rs.{amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        self._account_notes.append(f"Withdrew Rs.{amount}")
        return self.__balance

    def get_balance(self):
        return self.__balance


arjun_account = BankAccount("Arjun", 5000)
arjun_account.deposit(1500)
arjun_account.withdraw(800)
print(arjun_account.get_balance())
# Output: 5700

# `_account_notes` is "protected" by convention only — Python doesn't stop
# you from accessing it, but the underscore signals "don't touch this
# from outside the class unless you know what you're doing".
print(arjun_account._account_notes)
# Output: ['Deposited Rs.1500', 'Withdrew Rs.800']

# `__balance` is name-mangled: Python internally renames it to
# `_BankAccount__balance`, which makes accidental external access unlikely.
try:
    print(arjun_account.__balance)
except AttributeError as error:
    print(f"AttributeError: {error}")
# Output: AttributeError: 'BankAccount' object has no attribute '__balance'

# It's still technically reachable via the mangled name (Python has no
# TRUE private), but this is meant to discourage, not forbid, direct access.
print(arjun_account._BankAccount__balance)
# Output: 5700


# ════════════════════════════════════════════════════════════
# SECTION 4: The @property Decorator
# ════════════════════════════════════════════════════════════
# @property lets you expose a method as if it were a plain attribute,
# while still controlling reads (and optionally writes) behind the scenes.

print("-" * 50)
print("SECTION 4: @property for Controlled Access")
print("-" * 50)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # stored internally as protected

    @property
    def marks(self):
        """Getter: lets us read student.marks like a normal attribute."""
        return self._marks

    @marks.setter
    def marks(self, value):
        """Setter: validates before allowing student.marks = value."""
        if not (0 <= value <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self._marks = value

    @property
    def grade(self):
        """Read-only computed property — no setter defined."""
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        elif self._marks >= 35:
            return "C"
        return "Fail"


priya_student = Student("Priya", 82)
print(priya_student.marks)   # Output: 82 (looks like attribute access)
print(priya_student.grade)   # Output: B (computed on the fly)

priya_student.marks = 95     # Uses the setter, passes validation
print(priya_student.grade)   # Output: A

try:
    priya_student.marks = 150  # Fails validation inside the setter
except ValueError as error:
    print(f"ValueError: {error}")
# Output: ValueError: Marks must be between 0 and 100


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════

print("-" * 50)
print("GUIDED EXAMPLE 1: Polymorphic Shape Areas")
print("-" * 50)


class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(7), Triangle(10, 6)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")
# Output:
# Circle area: 153.94
# Triangle area: 30.0


print("-" * 50)
print("GUIDED EXAMPLE 2: Encapsulated Temperature Converter")
print("-" * 50)


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return round((self._celsius * 9 / 5) + 32, 1)


mumbai_temp = Temperature(34)
print(mumbai_temp.fahrenheit)  # Output: 93.2
mumbai_temp.celsius = 28
print(mumbai_temp.fahrenheit)  # Output: 82.4


print("-" * 50)
print("GUIDED EXAMPLE 3: Polymorphic Notification System")
print("-" * 50)


class Notification:
    def send(self, message):
        raise NotImplementedError


class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"


class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"


def notify_all(channels, message):
    for channel in channels:
        print(channel.send(message))


notify_all([SMSNotification(), EmailNotification()], "Order #4521 has shipped")
# Output:
# SMS sent: Order #4521 has shipped
# Email sent: Order #4521 has shipped


print("-" * 50)
print("GUIDED EXAMPLE 4: Private Counter With Controlled Access")
print("-" * 50)


class VisitCounter:
    def __init__(self):
        self.__count = 0

    def record_visit(self):
        self.__count += 1

    @property
    def total_visits(self):
        return self.__count


website_counter = VisitCounter()
for _ in range(3):
    website_counter.record_visit()
print(website_counter.total_visits)  # Output: 3
# website_counter.__count = 100  # would NOT change the real internal value
# because of name mangling — it would just create a new public attribute.


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Create a class `Wallet` with a private attribute `__balance` starting
# at 0. Add a method `add_money(amount)` that increases the balance
# (only if amount > 0), and a read-only @property called `balance` that
# returns the current balance.
#
# Expected behaviour:
#   w = Wallet()
#   w.add_money(500)
#   w.add_money(250)
#   w.balance  -> 750

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Polymorphism via method overriding (PaymentMethod subclasses)
#   - Duck typing (GiftVoucher worked without inheriting PaymentMethod)
#   - Public, protected (_x), and private (__x / name-mangled) attributes
#   - @property getters, setters, and read-only computed properties
#
# Next file (day11_03_dunder_methods.py) covers:
#   - Dunder (magic) methods: __str__, __repr__, __len__, __eq__

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11, File 2 complete: Polymorphism & Encapsulation")
