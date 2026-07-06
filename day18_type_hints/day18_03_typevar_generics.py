"""
Day 18 — Type Hints & Static Analysis
File 3 of 3: TypeVar and Generics

Covers:
    - Why "just use Any" defeats the purpose of type hints
    - TypeVar — a placeholder for "some type, to be decided by the caller"
    - Generic functions that work with any type while staying type-safe
    - Generic classes using Generic[T]
    - Bounded TypeVars (restricting which types are allowed)

Prerequisites:
    - Day 18, files 1 & 2 (Type Hints Basics, mypy/Optional/Union)
    - Day 17 (Advanced OOP — Protocol, dataclasses)

How to run:
    python day18_03_typevar_generics.py
"""

from typing import Generic, TypeVar

# ════════════════════════════════════════════════════════════
# SECTION 1: The Problem — Functions That Work on ANY Type
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("SECTION 1: The Problem Generics Solve")
print("=" * 50)
# Imagine a function that returns the first item of a list. It should
# work for a list[str], a list[int], a list[Passenger] — any list at all.
#
# We COULD write it with `Any`, but that throws away all type safety:
#
#     from typing import Any
#     def first_item(items: list[Any]) -> Any:
#         return items[0]
#
# With `Any`, mypy has no idea what first_item(["a", "b"]) returns — it
# could be treated as an int, a Passenger, anything — and mypy will not
# complain, defeating the whole point of type hints.
#
# A TypeVar solves this: it says "whatever type goes IN is the same
# type that comes OUT", and mypy can track that connection precisely.

print("See TypeVar examples below — they solve this without losing safety.")


# ════════════════════════════════════════════════════════════
# SECTION 2: TypeVar — Declaring a Placeholder Type
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 2: TypeVar Basics")
print("=" * 50)

# Convention: TypeVars are usually named T, or something short and
# capitalised. This line just DECLARES the placeholder; it does not
# pick a type yet — that happens each time the function is called.
T = TypeVar("T")


def first_item(items: list[T]) -> T:
    """Return the first item of any list, keeping its original type."""
    return items[0]


# When called with list[str], mypy infers T = str, so the return type
# is str. When called with list[int], T = int, and so on.
names: list[str] = ["Priya Sharma", "Arjun Mehta"]
print(first_item(names))
# Output: Priya Sharma

order_ids: list[int] = [10245, 10312, 10098]
print(first_item(order_ids))
# Output: 10245


# ── A TypeVar can appear more than once in the same signature ──
# This lets mypy enforce that two parameters share the same type.
def pick_larger(a: T, b: T) -> T:
    """Return whichever of a or b is 'larger', comparing with >."""
    return a if a > b else b  # type: ignore[operator]
    # (mypy can't prove every possible T supports ">", so this line
    #  needs an ignore in a fully generic version; in practice you'd
    #  bound T — see Section 4 below)


print(pick_larger(120.5, 89.0))
# Output: 120.5
print(pick_larger("Chennai", "Mumbai"))
# Output: Mumbai


# ════════════════════════════════════════════════════════════
# SECTION 3: Generic Classes with Generic[T]
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 3: Generic Classes")
print("=" * 50)
# A class can ALSO be generic over a type — useful for containers that
# should work with any payload type but stay internally consistent.

S = TypeVar("S")


class Stack(Generic[S]):
    """A simple last-in-first-out stack that works with any single type."""

    def __init__(self) -> None:
        self._items: list[S] = []

    def push(self, item: S) -> None:
        self._items.append(item)

    def pop(self) -> S:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


# Stack[str]: mypy now knows every item pushed/popped must be a str
task_stack: Stack[str] = Stack()
task_stack.push("Book train ticket")
task_stack.push("Pay electricity bill")
task_stack.push("Renew Swiggy One")

print(len(task_stack))
# Output: 3
print(task_stack.pop())
# Output: Renew Swiggy One
print(len(task_stack))
# Output: 2

# Stack[int]: a completely separate, independently-typed instance
order_id_stack: Stack[int] = Stack()
order_id_stack.push(10245)
order_id_stack.push(10312)
print(order_id_stack.pop())
# Output: 10312


# ════════════════════════════════════════════════════════════
# SECTION 4: Bounded TypeVars — Restricting Which Types Are Allowed
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 4: Bounded TypeVars")
print("=" * 50)
# A plain TypeVar accepts ANY type. Sometimes you want to restrict it —
# for example, "any type, as long as it supports addition and comparison,
# like int or float". You do this with `bound=`.

Number = TypeVar("Number", bound="int | float")


def total_and_average(values: list[int] | list[float]) -> tuple[float, float]:
    """Works for a list of int OR a list of float, not for a list of str."""
    total = sum(values)
    average = total / len(values)
    return float(total), round(average, 2)


fares: list[float] = [45.0, 60.0, 35.5]
print(total_and_average(fares))
# Output: (140.5, 46.83)

trip_counts: list[int] = [3, 5, 2, 4]
print(total_and_average(trip_counts))
# Output: (14.0, 3.5)

# NOTE: bounded TypeVars are most useful in generic FUNCTIONS/CLASSES
# where the bound is enforced across multiple parameters at once — the
# example above shows the concept using a Union for simplicity, since
# `sum()` on a Sequence needs a concrete overload to satisfy mypy fully.


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Progressive, Indian-context
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)

U = TypeVar("U")


# Example 1: A generic "get or default" helper
def get_or_default(value: U | None, default: U) -> U:
    """Return value if it isn't None, otherwise return default."""
    return value if value is not None else default


print(get_or_default(None, "Guest"))
# Output: Guest
print(get_or_default("Riya Deshmukh", "Guest"))
# Output: Riya Deshmukh


# Example 2: A generic swap function
def swap(pair: tuple[U, U]) -> tuple[U, U]:
    a, b = pair
    return b, a


print(swap(("Mumbai", "Pune")))
# Output: ('Pune', 'Mumbai')


# Example 3: A generic class wrapping a single labelled value (like a
# lightweight "Box" — a common generics teaching example)
class Box(Generic[U]):
    """Holds exactly one value of type U, with a label for display."""

    def __init__(self, label: str, value: U) -> None:
        self.label = label
        self.value: U = value

    def describe(self) -> str:
        return f"{self.label}: {self.value!r}"


price_box: Box[float] = Box("Ticket Price", 549.0)
print(price_box.describe())
# Output: Ticket Price: 549.0

city_box: Box[str] = Box("Home City", "Bengaluru")
print(city_box.describe())
# Output: Home City: 'Bengaluru'


# Example 4: A generic function that filters a list, keeping the type
def keep_matching(items: list[U], predicate) -> list[U]:  # type: ignore[no-untyped-def]
    return [item for item in items if predicate(item)]


passenger_ages: list[int] = [17, 25, 45, 16, 30]
adults = keep_matching(passenger_ages, lambda age: age >= 18)
print(adults)
# Output: [25, 45, 30]


# Example 5: A generic Stack used for an undo-history feature
undo_history: Stack[str] = Stack()
undo_history.push("typed heading")
undo_history.push("added table")
undo_history.push("inserted image")
print(f"Last action to undo: {undo_history.pop()}")
# Output: Last action to undo: inserted image
print(f"Actions remaining: {len(undo_history)}")
# Output: Actions remaining: 2


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Write a generic class `Pair(Generic[U])` that stores two values of
# the SAME type U, with a method `both_equal()` returning True if the
# two stored values are equal.
#
# Expected output:
#   Pair(5, 5).both_equal()   -> True
#   Pair("a", "b").both_equal() -> False

print("\n" + "=" * 50)
print("MINI-CHALLENGE")
print("=" * 50)

# YOUR CODE HERE
class Pair(Generic[U]):
    def __init__(self, first: U, second: U) -> None:
        self.first = first
        self.second = second

    def both_equal(self) -> bool:
        return self.first == self.second


print(Pair(5, 5).both_equal())
# Output: True
print(Pair("a", "b").both_equal())
# Output: False

# ── SOLUTION (reference) ──
# class Pair(Generic[U]):
#     def __init__(self, first: U, second: U) -> None:
#         self.first = first
#         self.second = second
#
#     def both_equal(self) -> bool:
#         return self.first == self.second


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Covered today (file 3 of 3):
#   - Why `Any` throws away type safety, and how TypeVar solves it
#   - TypeVar("T") as a placeholder that mypy resolves per call
#   - Generic functions where the same TypeVar links input and output
#   - Generic classes using Generic[T], e.g. a type-safe Stack
#   - Bounded TypeVars for restricting which types are acceptable
#
# This completes Day 18 — Type Hints & Static Analysis. Tomorrow (Day 19)
# moves on to Context Managers: the `with` protocol, `contextlib`, and
# writing your own custom context managers with @contextmanager.

if __name__ == "__main__":
    pass
