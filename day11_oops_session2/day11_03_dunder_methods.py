"""
Day 11 — Object-Oriented Programming II
File 3 of 3: Dunder (Magic) Methods

What this file covers:
    - What "dunder" methods are (double-underscore methods)
    - __str__ vs __repr__
    - __len__ for custom length support
    - __eq__ for custom equality comparison
    - A few bonus dunders: __add__, __lt__

Prerequisites:
    - Day 10: Classes, objects, __init__, self
    - Day 11 File 1: Inheritance & super()
    - Day 11 File 2: Polymorphism & Encapsulation

How to run:
    python day11_03_dunder_methods.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: What Are Dunder Methods?
# ════════════════════════════════════════════════════════════
# "Dunder" = Double UNDERscore. Methods like __init__, __str__, __len__
# are special hooks that Python calls automatically in certain situations
# (printing, using len(), comparing with ==, etc.). They let your custom
# classes behave like Python's built-in types.

print("=" * 50)
print("SECTION 1: The Problem Without __str__")
print("=" * 50)


class TaskWithoutStr:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority


plain_task = TaskWithoutStr("Submit report", "High")
print(plain_task)
# Output: <__main__.TaskWithoutStr object at 0x...>
# Not useful! We see a memory address instead of meaningful info.


# ── Concept: __str__ ──
# __str__ defines what print(obj) and str(obj) show. It should be a
# friendly, human-readable description.

print("-" * 50)
print("SECTION 2: __str__ for Human-Readable Output")
print("-" * 50)


class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"Task('{self.title}', priority={self.priority})"


report_task = Task("Submit report", "High")
print(report_task)
# Output: Task('Submit report', priority=High)
print(str(report_task))
# Output: Task('Submit report', priority=High)


# ── Concept: __repr__ ──
# __repr__ is meant for DEVELOPERS — it should ideally be unambiguous
# enough that eval(repr(obj)) could recreate the object. It's what you
# see when you inspect an object directly (e.g. in a list, or the
# interactive shell) if __str__ isn't defined for that context.

print("-" * 50)
print("SECTION 3: __repr__ for Developer-Facing Output")
print("-" * 50)


class TaskWithRepr:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"Task: {self.title} ({self.priority} priority)"

    def __repr__(self):
        return f"TaskWithRepr(title={self.title!r}, priority={self.priority!r})"


review_task = TaskWithRepr("Review PR", "Medium")
print(review_task)        # Output: Task: Review PR (Medium priority)  -- uses __str__
print(repr(review_task))  # Output: TaskWithRepr(title='Review PR', priority='Medium')

# Lists/containers always use __repr__ for their elements, even if __str__ exists:
task_list = [review_task]
print(task_list)
# Output: [TaskWithRepr(title='Review PR', priority='Medium')]


# ════════════════════════════════════════════════════════════
# SECTION 4: __len__ — Custom Length Support
# ════════════════════════════════════════════════════════════
# __len__ lets your object work with the built-in len() function.

print("-" * 50)
print("SECTION 4: __len__")
print("-" * 50)


class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)


todays_tasks = TaskList(["Buy groceries", "Call Riya", "Finish assignment"])
print(len(todays_tasks))
# Output: 3


# ════════════════════════════════════════════════════════════
# SECTION 5: __eq__ — Custom Equality
# ════════════════════════════════════════════════════════════
# By default, two objects are only "equal" (==) if they are literally the
# SAME object in memory. __eq__ lets us define equality based on VALUES.

print("-" * 50)
print("SECTION 5: __eq__")
print("-" * 50)


class StudentWithoutEq:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name


student_a = StudentWithoutEq(101, "Arjun")
student_b = StudentWithoutEq(101, "Arjun")
print(student_a == student_b)
# Output: False (different objects in memory, even with identical data!)


class StudentWithEq:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, StudentWithEq):
            return NotImplemented
        return self.roll_number == other.roll_number and self.name == other.name

    def __str__(self):
        return f"Student({self.roll_number}, {self.name})"


student_c = StudentWithEq(101, "Arjun")
student_d = StudentWithEq(101, "Arjun")
print(student_c == student_d)
# Output: True (compares VALUES now, not memory identity)


# ════════════════════════════════════════════════════════════
# SECTION 6: Bonus Dunders — __add__ and __lt__
# ════════════════════════════════════════════════════════════
# Python lets you overload operators like + and < by defining their
# dunder counterparts.

print("-" * 50)
print("SECTION 6: __add__ and __lt__")
print("-" * 50)


class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __add__(self, other):
        return Money(self.rupees + other.rupees)

    def __lt__(self, other):
        return self.rupees < other.rupees

    def __str__(self):
        return f"Rs.{self.rupees}"


wallet1 = Money(500)
wallet2 = Money(300)
combined = wallet1 + wallet2  # calls wallet1.__add__(wallet2)
print(combined)
# Output: Rs.800
print(wallet2 < wallet1)  # calls wallet2.__lt__(wallet1)
# Output: True


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════

print("-" * 50)
print("GUIDED EXAMPLE 1: Book With __str__ and __repr__")
print("-" * 50)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __len__(self):
        return self.pages


gita_book = Book("The Bhagavad Gita Explained", "R. Sharma", 320)
print(gita_book)        # Output: "The Bhagavad Gita Explained" by R. Sharma
print(len(gita_book))   # Output: 320


print("-" * 50)
print("GUIDED EXAMPLE 2: Comparable Cricket Scores")
print("-" * 50)


class CricketScore:
    def __init__(self, team, runs):
        self.team = team
        self.runs = runs

    def __eq__(self, other):
        return self.runs == other.runs

    def __lt__(self, other):
        return self.runs < other.runs

    def __str__(self):
        return f"{self.team}: {self.runs} runs"


mumbai_score = CricketScore("Mumbai", 187)
delhi_score = CricketScore("Delhi", 165)
print(mumbai_score == delhi_score)  # Output: False
print(delhi_score < mumbai_score)   # Output: True
print(max(mumbai_score, delhi_score, key=lambda score: score.runs))
# Output: Mumbai: 187 runs (print() calls __str__ automatically)


print("-" * 50)
print("GUIDED EXAMPLE 3: Vector Addition With __add__")
print("-" * 50)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


vector_a = Vector2D(2, 3)
vector_b = Vector2D(4, -1)
print(vector_a + vector_b)
# Output: (6, 2)


print("-" * 50)
print("GUIDED EXAMPLE 4: Inventory Item With __eq__ and __len__")
print("-" * 50)


class InventoryItem:
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity

    def __eq__(self, other):
        return self.sku == other.sku

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"Item {self.sku} (qty: {self.quantity})"


item_x = InventoryItem("SKU-001", 40)
item_y = InventoryItem("SKU-001", 15)  # same SKU, different stock batch
print(item_x == item_y)  # Output: True (equality defined by SKU only)
print(len(item_x))       # Output: 40


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Create a class `Playlist` that takes a list of song titles in __init__.
# Implement:
#   - __len__ -> number of songs
#   - __str__ -> "Playlist with N songs" (N = number of songs)
#   - __eq__  -> two playlists are equal if they contain the same songs
#                in the same order
#
# Expected behaviour:
#   p1 = Playlist(["Kesariya", "Tum Hi Ho"])
#   p2 = Playlist(["Kesariya", "Tum Hi Ho"])
#   len(p1) -> 2
#   str(p1) -> "Playlist with 2 songs"
#   p1 == p2 -> True

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - __str__ for friendly, user-facing string output
#   - __repr__ for unambiguous, developer-facing output
#   - __len__ to support len(obj)
#   - __eq__ to support value-based == comparison
#   - Bonus: __add__ and __lt__ for operator overloading
#
# This completes Day 11 — Object-Oriented Programming II.
# Next session (Day 12) covers: Modules & Packages — import, pip/uv,
# the __main__ guard, and key standard library modules (os, sys, math,
# datetime, pathlib).

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11, File 3 complete: Dunder (Magic) Methods")
