"""
Day 17 — Advanced OOP
File 1 of 4: Abstract Base Classes (ABCMeta)

What this file covers:
    - Why we need abstract base classes (ABCs)
    - The `abc` module — `ABC` and `@abstractmethod`
    - Enforcing a contract that subclasses MUST implement
    - Abstract methods vs regular (concrete) methods in an ABC
    - Why you cannot instantiate an abstract class directly

Prerequisites:
    - Day 10 (OOP I — classes, __init__, self)
    - Day 11 (OOP II — inheritance, super(), dunder methods)

How to run:
    python day17_01_abstract_base_classes.py
"""

from abc import ABC, abstractmethod


# ════════════════════════════════════════════════════════
# SECTION 1: Why Abstract Base Classes?
# ════════════════════════════════════════════════════════
#
# Imagine you are building the payment system for an e-commerce app
# used across Mumbai, Delhi, and Bengaluru. Customers can pay using
# Paytm, Razorpay, or PhonePe. Every payment gateway MUST be able to
# process a payment and check a transaction status — but the concept
# of a generic "PaymentGateway" should never be created on its own.
#
# A normal (concrete) base class does not stop anyone from creating
# a useless, generic instance of it. An Abstract Base Class (ABC)
# solves this: it defines a contract, and Python REFUSES to let you
# create an object of a class that hasn't fulfilled that contract.


# ── Concept: Creating an ABC ──
class PaymentGateway(ABC):
    """
    Abstract base class for all payment gateways.
    Any subclass MUST implement process_payment() and check_status(),
    or Python will raise a TypeError when you try to instantiate it.
    """

    def __init__(self, merchant_name):
        self.merchant_name = merchant_name

    @abstractmethod
    def process_payment(self, amount):
        """Every gateway must define how it processes a payment."""
        pass

    @abstractmethod
    def check_status(self, transaction_id):
        """Every gateway must define how it checks transaction status."""
        pass

    # A concrete (non-abstract) method IS allowed in an ABC.
    # Subclasses inherit this for free — no need to override it.
    def print_receipt(self, amount):
        print(f"Receipt: Rs. {amount} paid to {self.merchant_name}")


# ── Concept: Trying to instantiate an ABC directly fails ──
try:
    gateway = PaymentGateway("Flipkart Store")
except TypeError as error:
    print(f"Cannot create PaymentGateway directly -> {error}")
# Output:
# Cannot create PaymentGateway directly -> Can't instantiate abstract class
# PaymentGateway without an implementation for abstract methods
# 'check_status', 'process_payment'

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: Implementing Concrete Subclasses
# ════════════════════════════════════════════════════════

# ── Concept: A subclass MUST override every abstract method ──
class PaytmGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"[Paytm] Processing Rs. {amount} for {self.merchant_name}")
        return f"PAYTM-TXN-{amount}"

    def check_status(self, transaction_id):
        return f"{transaction_id} -> SUCCESS"


class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"[Razorpay] Processing Rs. {amount} for {self.merchant_name}")
        return f"RZP-TXN-{amount}"

    def check_status(self, transaction_id):
        return f"{transaction_id} -> SUCCESS"


# Now both gateways can be instantiated because the contract is fulfilled
paytm = PaytmGateway("Flipkart Store")
razorpay = RazorpayGateway("Swiggy Instamart")

txn1 = paytm.process_payment(1499)
txn2 = razorpay.process_payment(899)

print(paytm.check_status(txn1))
print(razorpay.check_status(txn2))

# The concrete method print_receipt() was never redefined,
# yet both subclasses can use it — inherited straight from the ABC.
paytm.print_receipt(1499)
razorpay.print_receipt(899)
# Output:
# [Paytm] Processing Rs. 1499 for Flipkart Store
# [Razorpay] Processing Rs. 899 for Swiggy Instamart
# PAYTM-TXN-1499 -> SUCCESS
# RZP-TXN-899 -> SUCCESS
# Receipt: Rs. 1499 paid to Flipkart Store
# Receipt: Rs. 899 paid to Swiggy Instamart

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: What happens if a subclass forgets a method?
# ════════════════════════════════════════════════════════

class BrokenGateway(PaymentGateway):
    def process_payment(self, amount):
        return "processed"
    # check_status() is missing on purpose!

try:
    broken = BrokenGateway("Test Merchant")
except TypeError as error:
    print(f"BrokenGateway failed to instantiate -> {error}")
# Output:
# BrokenGateway failed to instantiate -> Can't instantiate abstract class
# BrokenGateway without an implementation for abstract method 'check_status'

print("-" * 50)


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian e-commerce & delivery contexts
# ════════════════════════════════════════════════════════

# ── Example 1: Abstract "Notification" sender ──
class NotificationSender(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


class SMSSender(NotificationSender):
    def send(self, recipient, message):
        print(f"SMS to {recipient}: {message}")


class EmailSender(NotificationSender):
    def send(self, recipient, message):
        print(f"Email to {recipient}: {message}")


senders = [SMSSender(), EmailSender()]
for sender in senders:
    sender.send("Arjun Mehta", "Your IRCTC ticket is confirmed!")
# Output:
# SMS to Arjun Mehta: Your IRCTC ticket is confirmed!
# Email to Arjun Mehta: Your IRCTC ticket is confirmed!

print("-" * 50)


# ── Example 2: Abstract "DeliveryPartner" for Swiggy-style app ──
class DeliveryPartner(ABC):
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @abstractmethod
    def estimate_time(self, distance_km):
        pass

    def profile(self):
        return f"{self.name} ({self.city})"


class BikePartner(DeliveryPartner):
    def estimate_time(self, distance_km):
        return round(distance_km / 30 * 60, 1)  # avg 30 km/h -> minutes


class CyclePartner(DeliveryPartner):
    def estimate_time(self, distance_km):
        return round(distance_km / 15 * 60, 1)  # avg 15 km/h -> minutes


riya = BikePartner("Riya Deshmukh", "Pune")
sanjay = CyclePartner("Sanjay Verma", "Bengaluru")

print(f"{riya.profile()} ETA: {riya.estimate_time(6)} minutes")
print(f"{sanjay.profile()} ETA: {sanjay.estimate_time(6)} minutes")
# Output:
# Riya Deshmukh (Pune) ETA: 12.0 minutes
# Sanjay Verma (Bengaluru) ETA: 24.0 minutes

print("-" * 50)


# ── Example 3: Using isinstance() with ABCs ──
partners = [riya, sanjay]
for partner in partners:
    print(f"{partner.name} is a DeliveryPartner? {isinstance(partner, DeliveryPartner)}")
# Output:
# Riya Deshmukh is a DeliveryPartner? True
# Sanjay Verma is a DeliveryPartner? True

print("-" * 50)


# ── Example 4: Abstract property (a variation using @property + @abstractmethod) ──
class Vehicle(ABC):
    @property
    @abstractmethod
    def fuel_type(self):
        pass


class ElectricScooter(Vehicle):
    @property
    def fuel_type(self):
        return "Electric"


class PetrolBike(Vehicle):
    @property
    def fuel_type(self):
        return "Petrol"


scooter = ElectricScooter()
bike = PetrolBike()
print(f"Scooter runs on: {scooter.fuel_type}")
print(f"Bike runs on: {bike.fuel_type}")
# Output:
# Scooter runs on: Electric
# Bike runs on: Petrol

print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Create an abstract base class `Report` with:
#   - An abstract method `generate(self)` that returns a string
#   - A concrete method `header(self, title)` that returns
#     f"===== {title} ====="
#
# Then create two subclasses:
#   - `SalesReport` — generate() returns "Sales: Rs. 45000"
#   - `InventoryReport` — generate() returns "Items in stock: 320"
#
# Create one instance of each and print header("Monthly Report")
# followed by generate() for both.
#
# Expected output:
# ===== Monthly Report =====
# Sales: Rs. 45000
# ===== Monthly Report =====
# Items in stock: 320

# YOUR CODE HERE


# SOLUTION:
# class Report(ABC):
#     @abstractmethod
#     def generate(self):
#         pass
#
#     def header(self, title):
#         return f"===== {title} ====="
#
#
# class SalesReport(Report):
#     def generate(self):
#         return "Sales: Rs. 45000"
#
#
# class InventoryReport(Report):
#     def generate(self):
#         return "Items in stock: 320"
#
#
# sales = SalesReport()
# inventory = InventoryReport()
# print(sales.header("Monthly Report"))
# print(sales.generate())
# print(inventory.header("Monthly Report"))
# print(inventory.generate())


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file you learned:
#   - ABCs define a contract subclasses MUST fulfill
#   - `@abstractmethod` marks methods that MUST be overridden
#   - You cannot instantiate a class with unimplemented abstract methods
#   - ABCs can still hold concrete (shared) methods
#   - Abstract properties combine @property with @abstractmethod
#
# Next up: day17_02_metaclasses.py — where classes themselves
# become objects created by other classes (metaclasses)!
