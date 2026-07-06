"""
Day 17 — Advanced OOP
File 2 of 4: Metaclasses

What this file covers:
    - "Classes are objects too" — everything in Python is an object
    - `type()` as the default metaclass
    - Writing a custom metaclass with `type(name, bases, dct)`
    - Overriding `__new__` and `__init__` inside a metaclass
    - Two practical uses: a Singleton metaclass and an
      auto-registering "plugin" metaclass

Prerequisites:
    - Day 10-11 (OOP I & II)
    - day17_01_abstract_base_classes.py (same day, file 1)

How to run:
    python day17_02_metaclasses.py
"""


# ════════════════════════════════════════════════════════
# SECTION 1: Classes Are Objects Too
# ════════════════════════════════════════════════════════
#
# In Python, everything is an object — including classes themselves.
# When you write `class Foo: ...`, Python actually calls a special
# callable behind the scenes to CREATE the class object `Foo`.
# That callable is called a METACLASS. By default, it's `type`.

# ── Concept: type() is the metaclass of every ordinary class ──
class Student:
    def __init__(self, name):
        self.name = name


priya = Student("Priya Sharma")

print(f"type(priya)   -> {type(priya)}")
print(f"type(Student) -> {type(Student)}")
print(f"type(type)    -> {type(type)}")
# Output:
# type(priya)   -> <class '__main__.Student'>
# type(Student) -> <class 'type'>
# type(type)    -> <class 'type'>

print("-" * 50)


# ── Concept: type() can create a class dynamically, without `class` ──
# type(name, bases, namespace_dict) builds a brand-new class object
DynamicStudent = type(
    "DynamicStudent",
    (object,),
    {"college": "IIT Bombay", "greet": lambda self: f"Hi, I study at {self.college}"}
)

arjun = DynamicStudent()
print(f"DynamicStudent created via type(): {arjun.greet()}")
# Output:
# DynamicStudent created via type(): Hi, I study at IIT Bombay

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: Writing a Custom Metaclass
# ════════════════════════════════════════════════════════
#
# A metaclass is simply a class that INHERITS from `type`.
# When a class uses `metaclass=MyMeta`, Python calls MyMeta(...)
# instead of the default type(...) to build that class.

# ── Concept: A metaclass that logs every class creation ──
class LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"[LoggingMeta] Creating class '{name}'")
        return super().__new__(mcs, name, bases, namespace)


class Employee(metaclass=LoggingMeta):
    def __init__(self, name, city):
        self.name = name
        self.city = city
# Output (printed at class-definition time, not instantiation time):
# [LoggingMeta] Creating class 'Employee'

meera = Employee("Meera Iyer", "Chennai")
print(f"Employee created: {meera.name} from {meera.city}")
# Output:
# Employee created: Meera Iyer from Chennai

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: Practical Use #1 — Singleton via Metaclass
# ════════════════════════════════════════════════════════
#
# A common real use of metaclasses is enforcing a Singleton —
# a class that can only ever have ONE instance. Useful for
# things like a shared database connection or app configuration.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {"currency": "INR", "region": "Mumbai"}


config1 = AppConfig()
config2 = AppConfig()

config1.settings["currency"] = "USD"

print(f"config1 is config2 -> {config1 is config2}")
print(f"config2.settings   -> {config2.settings}")
# Output:
# config1 is config2 -> True
# config2.settings   -> {'currency': 'USD', 'region': 'Mumbai'}

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 4: Practical Use #2 — Auto-Registering Plugins
# ════════════════════════════════════════════════════════
#
# Imagine a food-delivery app (like Swiggy) that supports many
# restaurant "cuisine handlers". A registry metaclass can
# automatically track every subclass as soon as it's defined —
# no manual registration list needed.

class CuisineRegistryMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        new_class = super().__new__(mcs, name, bases, namespace)
        if bases:  # skip registering the base class itself
            mcs.registry[name] = new_class
        return new_class


class CuisineHandler(metaclass=CuisineRegistryMeta):
    def prepare(self):
        raise NotImplementedError


class NorthIndianHandler(CuisineHandler):
    def prepare(self):
        return "Preparing butter chicken and naan"


class SouthIndianHandler(CuisineHandler):
    def prepare(self):
        return "Preparing dosa and sambar"


print(f"Registered cuisines: {list(CuisineRegistryMeta.registry.keys())}")
for cuisine_name, cuisine_class in CuisineRegistryMeta.registry.items():
    handler = cuisine_class()
    print(f"{cuisine_name}: {handler.prepare()}")
# Output:
# Registered cuisines: ['NorthIndianHandler', 'SouthIndianHandler']
# NorthIndianHandler: Preparing butter chicken and naan
# SouthIndianHandler: Preparing dosa and sambar

print("-" * 50)


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════

# ── Example 1: A metaclass that enforces naming conventions ──
class UpperCaseMeta(type):
    def __new__(mcs, name, bases, namespace):
        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' must start with a capital letter")
        return super().__new__(mcs, name, bases, namespace)


class TrainBooking(metaclass=UpperCaseMeta):
    pass


print("TrainBooking class created successfully under UpperCaseMeta")
# Output:
# TrainBooking class created successfully under UpperCaseMeta

print("-" * 50)


# ── Example 2: Metaclass that injects a method into every subclass ──
class AuditMeta(type):
    def __new__(mcs, name, bases, namespace):
        namespace["audit_log"] = lambda self: f"{self.__class__.__name__} was accessed"
        return super().__new__(mcs, name, bases, namespace)


class BankAccount(metaclass=AuditMeta):
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


account = BankAccount("Sanjay Verma", 50000)
print(account.audit_log())
# Output:
# BankAccount was accessed

print("-" * 50)


# ── Example 3: Comparing isinstance() checks across the metaclass chain ──
print(f"isinstance(account, BankAccount) -> {isinstance(account, BankAccount)}")
print(f"isinstance(BankAccount, type)    -> {isinstance(BankAccount, type)}")
print(f"isinstance(BankAccount, AuditMeta) -> {isinstance(BankAccount, AuditMeta)}")
# Output:
# isinstance(account, BankAccount) -> True
# isinstance(BankAccount, type)    -> True
# isinstance(BankAccount, AuditMeta) -> True

print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Write a metaclass `PositiveOnlyMeta` that, when a class using it
# is defined, wraps every method starting with "set_" so that it
# raises a ValueError if called with a negative number.
#
# (This is a stretch challenge — feel free to first attempt a
# simpler version: a metaclass `CountingMeta` that keeps a class
# attribute `instance_count` on ANY class using it, incremented
# every time an instance is created.)
#
# Expected output for the simpler CountingMeta version:
# Wallet instances created: 2

# YOUR CODE HERE


# SOLUTION (simpler CountingMeta version):
# class CountingMeta(type):
#     def __call__(cls, *args, **kwargs):
#         instance = super().__call__(*args, **kwargs)
#         cls.instance_count = getattr(cls, "instance_count", 0) + 1
#         return instance
#
#
# class Wallet(metaclass=CountingMeta):
#     def __init__(self, owner):
#         self.owner = owner
#
#
# w1 = Wallet("Priya")
# w2 = Wallet("Arjun")
# print(f"Wallet instances created: {Wallet.instance_count}")


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Classes are objects, and `type` is their default metaclass
#   - `type(name, bases, dict)` builds classes dynamically
#   - Custom metaclasses inherit from `type` and override
#     `__new__` / `__call__` to customize class or instance creation
#   - Real-world patterns: Singleton enforcement, plugin auto-registration
#
# Next up: day17_03_protocol_classes.py — structural subtyping
# with typing.Protocol (an alternative to ABC inheritance)!
