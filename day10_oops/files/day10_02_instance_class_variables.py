"""
Day 10 — Object-Oriented Programming I
File 2 of 2: Instance Variables vs Class Variables, Instance Methods

Covers:
    - Instance variables (unique per object)
    - Class variables (shared across all objects)
    - How Python looks up attributes (instance first, then class)
    - Instance methods in more depth

Prerequisites:
    - day10_01_classes_basics.py (classes, __init__, self)

How to run:
    python day10_02_instance_class_variables.py
"""

# ════════════════════════════════════════════════════════
# SECTION 1: INSTANCE VARIABLES (RECAP)
# ════════════════════════════════════════════════════════

# ── Concept: Instance variables ──
# Every attribute we set using `self.xxx = value` inside __init__ (or any
# other method) is an INSTANCE VARIABLE. Each object gets its OWN separate
# copy — changing one object's instance variable never affects another.

print("=" * 50)
print("SECTION 1: Instance variables recap")
print("=" * 50)


class Employee:
    """An employee at a Bengaluru tech company."""

    def __init__(self, name, department):
        self.name = name              # instance variable
        self.department = department  # instance variable


meera = Employee("Meera", "Engineering")
arjun = Employee("Arjun", "Sales")

meera.department = "Data Science"  # only changes Meera's copy

print(f"Meera's department: {meera.department}")
print(f"Arjun's department: {arjun.department}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: CLASS VARIABLES
# ════════════════════════════════════════════════════════

# ── Concept: Class variables ──
# A CLASS VARIABLE is defined directly inside the class body (NOT inside
# __init__, and NOT prefixed with self). It is SHARED by every instance of
# the class — there is only ever one copy, no matter how many objects exist.
#
# Common uses: company-wide constants, counters that track how many objects
# have been created, default settings shared by all instances.

class Employee:
    """An employee at a Bengaluru tech company."""

    company_name = "TechNova Solutions"  # class variable — shared by ALL employees
    employee_count = 0                   # class variable — tracks total employees

    def __init__(self, name, department):
        self.name = name              # instance variable — unique per object
        self.department = department  # instance variable — unique per object
        Employee.employee_count += 1  # updating the SHARED class variable


meera = Employee("Meera", "Engineering")
arjun = Employee("Arjun", "Sales")
sanjay = Employee("Sanjay Verma", "Marketing")

print(f"Company: {meera.company_name}")     # accessed through an instance
print(f"Company: {Employee.company_name}")  # accessed through the class itself
print(f"Total employees created: {Employee.employee_count}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: THE ATTRIBUTE LOOKUP RULE (instance shadows class)
# ════════════════════════════════════════════════════════

# ── Concept: Instance attributes shadow class attributes ──
# When you access obj.attribute, Python first checks if `attribute` exists
# on the INSTANCE. If not found there, it falls back to the CLASS.
#
# If you assign obj.attribute = value, this ALWAYS creates (or overwrites)
# an INSTANCE variable — it never modifies the class variable, even if the
# names match!

class Task:
    """A task with a shared default priority."""

    default_priority = "Medium"  # class variable

    def __init__(self, description):
        self.description = description
        # Note: no self.priority set here — instances will "inherit"
        # default_priority from the class UNTIL they set their own.


task_a = Task("Update Flipkart order status")
task_b = Task("Fix IRCTC booking bug")

print(f"Task A priority (from class): {task_a.default_priority}")
print(f"Task B priority (from class): {task_b.default_priority}")

# Now we give task_b its OWN instance-level priority:
task_b.default_priority = "High"

print(f"After override -> Task A priority: {task_a.default_priority}")  # unchanged
print(f"After override -> Task B priority: {task_b.default_priority}")  # changed

# Changing the CLASS variable affects only objects that haven't overridden it:
Task.default_priority = "Low"
print(f"After class change -> Task A priority: {task_a.default_priority}")  # follows class
print(f"After class change -> Task B priority: {task_b.default_priority}")  # stays overridden
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 4: INSTANCE METHODS IN DEPTH
# ════════════════════════════════════════════════════════

# ── Concept: Instance methods ──
# A method defined inside a class, taking `self` as its first parameter, is
# an INSTANCE METHOD. It can read and modify the calling object's instance
# variables, and can also read (though not directly reassign) class
# variables through `self` or the class name.

class ShoppingCart:
    """A shopping cart for a Flipkart-style e-commerce order."""

    tax_rate = 0.18  # class variable — 18% GST, shared by every cart

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []          # instance variable — each cart has its own list
        self.subtotal = 0.0      # instance variable

    def add_item(self, item_name, price):
        self.items.append(item_name)
        self.subtotal += price
        print(f"Added '{item_name}' (Rs.{price}) to {self.customer_name}'s cart")

    def total_with_tax(self):
        tax_amount = self.subtotal * self.tax_rate  # reading class variable via self
        total = self.subtotal + tax_amount
        return total

    def summary(self):
        print(f"--- Cart summary for {self.customer_name} ---")
        print(f"Items: {', '.join(self.items)}")
        print(f"Subtotal: Rs.{self.subtotal:.2f}")
        print(f"Total (incl. {int(self.tax_rate * 100)}% GST): Rs.{self.total_with_tax():.2f}")


cart = ShoppingCart("Riya Deshmukh")
cart.add_item("Wireless Mouse", 799)
cart.add_item("USB-C Cable", 349)
cart.summary()
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 5: GUIDED EXAMPLES (Indian context)
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION 5: Guided Examples")
print("=" * 50)

# ── Example 1: A Counter using a class variable ──
class SwiggyOrder:
    """Tracks orders placed on a Swiggy-style food delivery app."""

    total_orders_today = 0  # class variable shared across all orders

    def __init__(self, customer_name, restaurant):
        self.customer_name = customer_name
        self.restaurant = restaurant
        SwiggyOrder.total_orders_today += 1
        self.order_number = SwiggyOrder.total_orders_today  # instance snapshot

    def show_order(self):
        print(f"Order #{self.order_number}: {self.customer_name} ordered from {self.restaurant}")


order1 = SwiggyOrder("Priya", "Saravana Bhavan")
order2 = SwiggyOrder("Arjun", "Bikanervala")
order3 = SwiggyOrder("Sanjay Verma", "Barbeque Nation")

order1.show_order()
order2.show_order()
order3.show_order()
print(f"Total orders placed today: {SwiggyOrder.total_orders_today}")
print("-" * 50)


# ── Example 2: Instance method that resets instance state ──
class CricketScorecard:
    """A live scorecard for a gully cricket match in Pune."""

    format_name = "T20"  # class variable — same format for every match created

    def __init__(self, team_name):
        self.team_name = team_name
        self.runs = 0
        self.wickets = 0

    def add_runs(self, runs):
        self.runs += runs

    def lose_wicket(self):
        self.wickets += 1

    def reset_innings(self):
        self.runs = 0
        self.wickets = 0
        print(f"{self.team_name}'s innings has been reset")

    def show_score(self):
        print(f"{self.team_name} ({self.format_name}): {self.runs}/{self.wickets}")


team_score = CricketScorecard("Mumbai Warriors")
team_score.add_runs(4)
team_score.add_runs(6)
team_score.lose_wicket()
team_score.show_score()
team_score.reset_innings()
team_score.show_score()
print("-" * 50)


# ── Example 3: Class variable used as a shared configuration ──
class KiranaStoreBill:
    """A bill generator for a neighbourhood kirana store."""

    store_name = "Deshmukh General Store"  # class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  # instance variable: item_name -> price

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def print_bill(self):
        print(f"===== {self.store_name} =====")
        print(f"Customer: {self.customer_name}")
        total = 0
        for item_name, price in self.items.items():
            print(f"  {item_name}: Rs.{price}")
            total += price
        print(f"  TOTAL: Rs.{total}")


bill = KiranaStoreBill("Meera")
bill.add_item("Rice (5kg)", 350)
bill.add_item("Toor Dal (1kg)", 140)
bill.add_item("Cooking Oil (1L)", 180)
bill.print_bill()
print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════

# Create a class called `TrainTicket` for an IRCTC-style booking system.
#
# Requirements:
#   1. Add a class variable `platform = "IRCTC"`.
#   2. Add a class variable `tickets_booked = 0` that counts every ticket
#      ever created.
#   3. __init__ should accept `passenger_name` and `train_number`, store
#      them as instance variables, and increment `tickets_booked`.
#   4. Add an instance method `show_ticket(self)` that prints something like:
#         "[IRCTC] Ticket for Priya on train 12951"
#   5. Create tickets for "Priya" on train "12951" and "Arjun" on train
#      "16032", then print `TrainTicket.tickets_booked`.
#
# Expected output (approx):
#   [IRCTC] Ticket for Priya on train 12951
#   [IRCTC] Ticket for Arjun on train 16032
#   Total tickets booked: 2

# YOUR CODE HERE


# SOLUTION:
# class TrainTicket:
#     platform = "IRCTC"
#     tickets_booked = 0
#
#     def __init__(self, passenger_name, train_number):
#         self.passenger_name = passenger_name
#         self.train_number = train_number
#         TrainTicket.tickets_booked += 1
#
#     def show_ticket(self):
#         print(f"[{self.platform}] Ticket for {self.passenger_name} on train {self.train_number}")
#
# ticket1 = TrainTicket("Priya", "12951")
# ticket2 = TrainTicket("Arjun", "16032")
# ticket1.show_ticket()
# ticket2.show_ticket()
# print(f"Total tickets booked: {TrainTicket.tickets_booked}")


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
# In this file, we covered:
#   - Instance variables (unique per object, set with self.xxx)
#   - Class variables (shared by all objects, defined in the class body)
#   - How attribute lookup falls back from instance to class
#   - How assigning obj.attr = value always creates an instance variable
#   - Instance methods that read/update both instance and class state
#
# Next up (Day 11):
#   - Inheritance and super()
#   - Polymorphism and encapsulation
#   - Dunder methods — __str__, __repr__, __len__, __eq__
