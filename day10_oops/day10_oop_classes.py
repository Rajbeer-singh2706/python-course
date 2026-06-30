"""
════════════════════════════════════════════════════════════════════════════════
Day 10 — Object-Oriented Programming I: Classes & Objects
30-Day Python Course | Intermediate Phase (Days 7–16)
════════════════════════════════════════════════════════════════════════════════

What this file covers:
  • What OOP is and why it matters
  • Defining classes with `class`
  • The __init__ constructor
  • The `self` keyword
  • Instance variables vs class variables
  • Instance methods
  • A real-world mini-project: Library Book System

Prerequisites: Days 1–9 (variables, control flow, loops, functions,
               data structures, strings, file I/O, error handling)

Next up: Day 11 — OOP II (Inheritance, Polymorphism, Dunder Methods)

How to run:
  python day10_oop_classes.py
════════════════════════════════════════════════════════════════════════════════
"""

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 1 — Why OOP? Thinking in Objects
# ════════════════════════════════════════════════════════════════════════════════

# ── What is Object-Oriented Programming? ──
#
# Until now you wrote *procedural* code — a list of instructions that
# run top-to-bottom. OOP is a different way of organising code around
# "objects" that bundle together:
#
#   • DATA        (called attributes or instance variables)
#   • BEHAVIOUR   (called methods — functions that live inside a class)
#
# Real-world analogy:
#   A "BankAccount" is a CLASS — a blueprint.
#   Priya's account and Arjun's account are two separate OBJECTS (instances)
#   built from that same blueprint. Each has its own balance, but they share
#   the same deposit() and withdraw() behaviour.
#
# Why learn OOP?
#   → Code is easier to read, reuse, and extend
#   → Groups related data + logic together — no more passing 10 arguments
#   → Essential for working with libraries (FastAPI, SQLAlchemy all use OOP)
#   → Required for Day 11 onwards and the capstone Task Manager project

print("=" * 60)
print("DAY 10 — Object-Oriented Programming I: Classes & Objects")
print("=" * 60)


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 2 — Defining a Class
# ════════════════════════════════════════════════════════════════════════════════

# ── Syntax ──
#
#   class ClassName:              ← PascalCase (UpperCamelCase) by convention
#       """Docstring."""
#
#       def __init__(self, p1):   ← constructor — runs on object creation
#           self.attribute = p1   ← instance variable
#
#       def some_method(self):    ← instance method
#           ...

print("\n" + "-" * 50)
print("SECTION 2 — Defining a Class")
print("-" * 50)


# Simplest possible class — no data, no methods yet
class Dog:
    """A simple Dog class."""
    pass   # 'pass' means nothing here yet


my_dog = Dog()    # create an instance (object) from the Dog blueprint
print(f"Type of my_dog  : {type(my_dog)}")
print(f"Is Dog instance : {isinstance(my_dog, Dog)}")


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 3 — The __init__ Constructor and self
# ════════════════════════════════════════════════════════════════════════════════

# ── __init__ ──
#   A special method Python calls automatically when you create an object.
#   Sets up the object's initial state.
#
# ── self ──
#   Refers to the specific instance being created or used.
#   Must always be the FIRST parameter of every instance method.
#   Python passes it automatically — you never supply it yourself.
#
#   obj = MyClass(arg1, arg2)
#   Python internally calls: MyClass.__init__(obj, arg1, arg2)

print("\n" + "-" * 50)
print("SECTION 3 — __init__ and self")
print("-" * 50)


class Student:
    """Represents a student enrolled in a course."""

    def __init__(self, name, age, city):
        """
        Constructor — called when Student(...) is invoked.

        Parameters:
            name (str): Student's full name
            age  (int): Student's age
            city (str): City where the student lives
        """
        self.name = name    # instance variable — belongs to THIS student object
        self.age  = age
        self.city = city

    def greet(self):
        """Print a personalised greeting."""
        print(f"  Hello! I am {self.name}, {self.age} years old, from {self.city}.")


# Creating two separate Student objects from the same blueprint
student1 = Student("Priya Sharma", 20, "Mumbai")
student2 = Student("Arjun Mehta",  22, "Delhi")

student1.greet()   # Hello! I am Priya Sharma, 20 years old, from Mumbai.
student2.greet()   # Hello! I am Arjun Mehta, 22 years old, from Delhi.

# Accessing attributes directly
print(f"\n  student1.name = {student1.name}")
print(f"  student2.city = {student2.city}")

# Each object is independent — changing one does NOT affect the other
student1.age = 21
print(f"\n  Priya's updated age  : {student1.age}")    # 21
print(f"  Arjun's age unchanged: {student2.age}")     # 22


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 4 — Instance Variables vs Class Variables
# ════════════════════════════════════════════════════════════════════════════════

# ── Instance Variables ──
#   Defined inside __init__ with self.xxx
#   Each object gets its OWN separate copy
#   Different objects can hold different values
#
# ── Class Variables ──
#   Defined directly inside the class body (NOT inside any method)
#   SHARED across ALL instances of the class
#   Useful for constants or counters that apply to every object

print("\n" + "-" * 50)
print("SECTION 4 — Instance vs Class Variables")
print("-" * 50)


class BankAccount:
    """
    A simple bank account.

    Class variables:
        bank_name      — same for every account (constant)
        total_accounts — counts all accounts created (shared counter)

    Instance variables:
        owner, balance — unique per account object
    """

    # ── Class variables (shared across all instances) ──
    bank_name      = "Dhan Bank of India"
    total_accounts = 0

    def __init__(self, owner, initial_deposit=0):
        # ── Instance variables (unique per object) ──
        self.owner   = owner
        self.balance = initial_deposit
        BankAccount.total_accounts += 1    # update the shared counter

    def deposit(self, amount):
        """Add funds to the account."""
        self.balance += amount
        print(f"  ₹{amount:,} deposited  →  {self.owner}'s balance: ₹{self.balance:,}")

    def withdraw(self, amount):
        """Withdraw funds; warn if insufficient."""
        if amount > self.balance:
            print(f"  Insufficient funds! {self.owner} has only ₹{self.balance:,}")
        else:
            self.balance -= amount
            print(f"  ₹{amount:,} withdrawn  →  {self.owner}'s balance: ₹{self.balance:,}")

    def show_info(self):
        """Display account summary."""
        print(f"  [{BankAccount.bank_name}]  {self.owner}  |  ₹{self.balance:,}")


acc1 = BankAccount("Priya Sharma", 10_000)
acc2 = BankAccount("Riya Patel",    5_000)

acc1.show_info()
acc2.show_info()
print(f"\n  Total accounts created: {BankAccount.total_accounts}")   # 2

acc1.deposit(2_500)
acc1.withdraw(800)
acc2.withdraw(9_000)   # insufficient funds

# Class variable accessible via instance OR via class name
print(f"\n  Via instance : {acc1.bank_name}")
print(f"  Via class    : {BankAccount.bank_name}")


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 5 — Instance Methods in Depth
# ════════════════════════════════════════════════════════════════════════════════

# ── Rules for instance methods ──
#   1. Always defined inside the class body (indented under class)
#   2. First parameter is always `self`
#   3. Called on an object: obj.method_name(args)
#   4. Can read AND modify instance variables
#   5. Can call other methods on the same object using self.other_method()

print("\n" + "-" * 50)
print("SECTION 5 — Instance Methods")
print("-" * 50)


class Rectangle:
    """A rectangle — demonstrates multiple methods calling each other."""

    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Return True if width == height."""
        return self.width == self.height

    def scale(self, factor):
        """Scale dimensions in place."""
        self.width  *= factor
        self.height *= factor

    def describe(self):
        """Print full description — calls other methods via self."""
        shape = "Square" if self.is_square() else "Rectangle"
        print(f"  {shape}: {self.width} x {self.height}")
        print(f"    Area      = {self.area()} sq units")
        print(f"    Perimeter = {self.perimeter()} units")


r1 = Rectangle(6, 4)
r1.describe()

r2 = Rectangle(5, 5)
r2.describe()

r1.scale(2)
print(f"\n  After scaling r1 by 2:")
r1.describe()


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 6 — Guided Examples with Indian Context
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "-" * 50)
print("SECTION 6 — Guided Examples")
print("-" * 50)

# ── Example 1: Movie Ticket ──────────────────────────────────────────────────

class MovieTicket:
    """A cinema ticket with dynamic pricing."""

    base_price = 180   # Rs 180 base — class variable (shared)

    def __init__(self, customer_name, movie_title, seat_class):
        self.customer_name = customer_name
        self.movie_title   = movie_title
        self.seat_class    = seat_class.lower()

    def _price(self):
        """Internal helper — compute ticket price by seat class."""
        multipliers = {"economy": 1.0, "premium": 1.5, "vip": 2.5}
        return int(MovieTicket.base_price * multipliers.get(self.seat_class, 1.0))

    def print_ticket(self):
        """Print a formatted ticket."""
        p = self._price()
        print(f"\n  Ticket | {self.movie_title}")
        print(f"  Customer : {self.customer_name}")
        print(f"  Class    : {self.seat_class.title()}")
        print(f"  Price    : Rs {p}")


t1 = MovieTicket("Priya Sharma", "Pushpa 2", "premium")
t2 = MovieTicket("Arjun Mehta",  "Pushpa 2", "vip")
t1.print_ticket()
t2.print_ticket()

# ── Example 2: Cricket Player ────────────────────────────────────────────────

print()

class CricketPlayer:
    """Tracks a player's batting stats across matches."""

    def __init__(self, name, team):
        self.name    = name
        self.team    = team
        self.runs    = 0
        self.matches = 0
        self.wickets = 0

    def play_match(self, runs_scored, wickets_taken=0):
        """Record one match."""
        self.runs    += runs_scored
        self.matches += 1
        self.wickets += wickets_taken

    def batting_average(self):
        """Average runs per match."""
        return round(self.runs / self.matches, 2) if self.matches else 0.0

    def show_stats(self):
        print(f"  {self.name} ({self.team})")
        print(f"  Matches: {self.matches}  |  Runs: {self.runs}  |"
              f"  Avg: {self.batting_average()}  |  Wickets: {self.wickets}")


rohit = CricketPlayer("Rohit Sharma", "India")
rohit.play_match(83)
rohit.play_match(131)
rohit.play_match(56)
rohit.show_stats()

# ── Example 3: Grocery Cart ──────────────────────────────────────────────────

print()

class GroceryCart:
    """A shopping cart with itemised billing."""

    def __init__(self, customer_name):
        self.customer = customer_name
        self.items    = {}   # {item_name: (price, quantity)}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            old_p, old_q = self.items[name]
            self.items[name] = (old_p, old_q + quantity)
        else:
            self.items[name] = (price, quantity)
        print(f"  Added: {quantity}x {name} @ Rs {price}")

    def total(self):
        return sum(p * q for p, q in self.items.values())

    def print_receipt(self):
        print(f"\n  -- Receipt for {self.customer} --")
        for name, (price, qty) in self.items.items():
            print(f"  {name:<22} {qty} x Rs {price:<6} = Rs {price * qty}")
        print(f"  {'TOTAL':<34} Rs {self.total()}")


cart = GroceryCart("Riya Patel")
cart.add_item("Basmati Rice (5 kg)", 350)
cart.add_item("Toor Dal (1 kg)",     120)
cart.add_item("Amul Butter",          58, quantity=2)
cart.add_item("Milk (1 L)",           68, quantity=3)
cart.print_receipt()


# ════════════════════════════════════════════════════════════════════════════════
# SECTION 7 — Common Mistakes & How to Avoid Them
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "-" * 50)
print("SECTION 7 — Common Mistakes")
print("-" * 50)

# Mistake 1: Forgetting `self` in method definition
#   def greet():          # WRONG — TypeError when called
#   def greet(self):      # CORRECT

# Mistake 2: Forgetting `self.` when setting attributes inside __init__
#   def __init__(self, name):
#       name = name       # WRONG — local variable, lost immediately
#       self.name = name  # CORRECT — stored on the object

# Mistake 3: Mutable default class variable shared across all instances

class BadTeam:
    members = []     # DANGER: shared list across ALL instances!
    def __init__(self, name):
        self.name = name
    def add(self, person):
        self.members.append(person)   # modifies the SHARED list

class GoodTeam:
    def __init__(self, name):
        self.name    = name
        self.members = []   # SAFE: each instance owns its own list
    def add(self, person):
        self.members.append(person)


team_a = GoodTeam("Alpha")
team_b = GoodTeam("Beta")
team_a.add("Priya")
team_b.add("Arjun")
print(f"  team_a members: {team_a.members}")   # ['Priya']
print(f"  team_b members: {team_b.members}")   # ['Arjun']  — not mixed up
print("  Tip: Use self.list = [] in __init__ for mutable data, not class-level lists.")


# ════════════════════════════════════════════════════════════════════════════════
# MINI-CHALLENGE — Library Book System
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("MINI-CHALLENGE — Library Book System")
print("=" * 60)
print("""
Build a Book class for a library system.

Requirements:
  __init__(title, author, total_copies)
    • title, author, total_copies stored as instance variables
    • available_copies starts equal to total_copies

  checkout(member_name)
    • If available: decrease available_copies, print confirmation
    • If none available: print "Sorry, '<title>' is currently unavailable."

  return_book()
    • If copies out: increase available_copies, print new count
    • If all already in: print "All copies already in the library."

  status()
    • Print: "<title> by <author> — <available>/<total> copies available"

Expected output:
  'Malgudi Days' checked out by Priya.
  'Malgudi Days' checked out by Arjun.
  Sorry, 'Malgudi Days' is currently unavailable.
  'Malgudi Days' returned. Copies available: 1
  Malgudi Days by R.K. Narayan -- 1/2 copies available
""")

# YOUR CODE HERE
# class Book:
#     def __init__(self, title, author, total_copies):
#         ...


# ── Reference Solution (study after attempting) ──────────────────────────────

class Book:
    """A library book with copy-tracking."""

    def __init__(self, title, author, total_copies):
        self.title            = title
        self.author           = author
        self.total_copies     = total_copies
        self.available_copies = total_copies

    def checkout(self, member_name):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"  '{self.title}' checked out by {member_name}.")
        else:
            print(f"  Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"  '{self.title}' returned. Copies available: {self.available_copies}")
        else:
            print(f"  All copies already in the library.")

    def status(self):
        print(f"  {self.title} by {self.author} "
              f"-- {self.available_copies}/{self.total_copies} copies available")


book = Book("Malgudi Days", "R.K. Narayan", 2)
book.checkout("Priya")
book.checkout("Arjun")
book.checkout("Riya")
book.return_book()
book.status()


# ════════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("DAY 10 SUMMARY")
print("=" * 60)
print("""
What you learned today:
  [+] OOP bundles data + behaviour into objects
  [+] class defines the blueprint; objects are instances
  [+] __init__ is the constructor, runs on object creation
  [+] self refers to the current instance (always first parameter)
  [+] Instance variables (self.x) are unique per object
  [+] Class variables are shared across all instances
  [+] Instance methods access/modify object data via self

Key syntax recap:
  class MyClass:
      class_var = "shared"
      def __init__(self, value):
          self.instance_var = value
      def my_method(self):
          return self.instance_var

Coming up — Day 11: OOP II
  -> Inheritance: child classes reusing parent code
  -> super() to call parent methods
  -> Polymorphism: same method, different behaviour
  -> Dunder methods: __str__, __repr__, __len__, __eq__
""")


if __name__ == "__main__":
    pass   # All demo code runs at module level above — add experiments here!
