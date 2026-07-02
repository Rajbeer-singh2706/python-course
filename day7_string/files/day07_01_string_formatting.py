"""
Day 07 — Strings & String Methods
File 1 of 3: String Formatting & f-strings

Covers:
    - The % operator (old-style formatting)
    - str.format() (positional and named placeholders)
    - f-strings (modern, preferred style)
    - Format specifiers: width, precision, alignment, commas, percentages

Prerequisites:
    - Day 02 (Variables & Data Types)
    - Day 06 (Data Structures — dictionaries, lists)

How to run:
    python day07_01_string_formatting.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: Why String Formatting?
# ════════════════════════════════════════════════════════════
# When we build messages for users, we rarely want to just print
# raw variables — we want to control spacing, decimal places,
# and readability. Python gives us three ways to do this.

print("=" * 50)
print("SECTION 1: Why String Formatting?")
print("=" * 50)

name = "Priya"
city = "Mumbai"
print("Hello, " + name + "! Welcome to " + city + ".")
# Output: Hello, Priya! Welcome to Mumbai.
# Concatenation with + works, but gets messy fast, especially
# with numbers that need type conversion.


# ────────────────────────────────────────────────────────────
# ── Concept: The % Operator (Old-Style Formatting) ──
# ────────────────────────────────────────────────────────────
# You will see this in older codebases. %s = string, %d = int,
# %.2f = float with 2 decimal places.

print("-" * 50)
print("The %% Operator")
print("-" * 50)

student_name = "Arjun"
marks = 87
print("%s scored %d marks." % (student_name, marks))
# Output: Arjun scored 87 marks.

price = 1499.5
print("The price is Rs. %.2f" % price)
# Output: The price is Rs. 1499.50


# ────────────────────────────────────────────────────────────
# ── Concept: str.format() ──
# ────────────────────────────────────────────────────────────
# format() uses {} placeholders. You can fill them by position,
# by index, or by keyword — which makes the template reusable.

print("-" * 50)
print("str.format()")
print("-" * 50)

city_name = "Delhi"
temperature = 32.5
print("{} is currently {} degrees Celsius.".format(city_name, temperature))
# Output: Delhi is currently 32.5 degrees Celsius.

# Positional indices let you reuse or reorder values
print("{0} works in {1}. {0} loves {1}!".format("Riya", "Bengaluru"))
# Output: Riya works in Bengaluru. Riya loves Bengaluru!

# Named placeholders make templates self-documenting
print("{student} paid Rs. {amount} for the course.".format(
    student="Sanjay", amount=4999))
# Output: Sanjay paid Rs. 4999 for the course.


# ────────────────────────────────────────────────────────────
# ── Concept: f-strings (Preferred in Modern Python) ──
# ────────────────────────────────────────────────────────────
# f-strings (Python 3.6+) let you embed expressions directly
# inside {}. They are faster, more readable, and the standard
# choice for new code.

print("-" * 50)
print("f-strings")
print("-" * 50)

employee = "Priya Sharma"
salary = 65000
print(f"{employee} earns Rs. {salary} per month.")
# Output: Priya Sharma earns Rs. 65000 per month.

# f-strings can hold any valid expression, not just variables
tax_rate = 0.10
print(f"Tax deducted: Rs. {salary * tax_rate}")
# Output: Tax deducted: Rs. 6500.0

# Calling functions inside an f-string works too
print(f"Employee name in uppercase: {employee.upper()}")
# Output: Employee name in uppercase: PRIYA SHARMA


# ────────────────────────────────────────────────────────────
# ── Concept: Format Specifiers ──
# ────────────────────────────────────────────────────────────
# After a colon inside {}, you can control width, decimal
# precision, alignment, and thousands separators.

print("-" * 50)
print("Format Specifiers")
print("-" * 50)

amount_due = 125000.789
print(f"Rounded to 2 decimals: Rs. {amount_due:.2f}")
# Output: Rounded to 2 decimals: Rs. 125000.79

print(f"With comma separator: Rs. {amount_due:,.2f}")
# Output: With comma separator: Rs. 125,000.79

score_percent = 0.876
print(f"Score: {score_percent:.1%}")
# Output: Score: 87.6%

# Alignment and width — useful for building aligned tables
for student, score in [("Arjun", 78), ("Riya", 91), ("Sanjay", 65)]:
    print(f"{student:<10}{score:>5}")
# Output:
# Arjun        78
# Riya         91
# Sanjay       65


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — India-Contextualized
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)

# Example 1: Building a grocery receipt line
print("-" * 50)
print("Example 1: Grocery Receipt Line")
item_name = "Basmati Rice (5kg)"
item_price = 649.0
print(f"{item_name:<25}Rs. {item_price:>8.2f}")
# Output: Basmati Rice (5kg)      Rs.   649.00

# Example 2: Formatting a student report card line
print("-" * 50)
print("Example 2: Report Card Line")
subject = "Mathematics"
marks_obtained = 92
total_marks = 100
percentage = (marks_obtained / total_marks) * 100
print(f"{subject}: {marks_obtained}/{total_marks} ({percentage:.1f}%)")
# Output: Mathematics: 92/100 (92.0%)

# Example 3: A multi-line invoice summary for a Mumbai vendor
print("-" * 50)
print("Example 3: Invoice Summary")
vendor = "Deshmukh Textiles"
invoice_no = 2201
subtotal = 8500.0
gst = subtotal * 0.18
total = subtotal + gst
print(f"Invoice #{invoice_no} — {vendor}")
print(f"{'Subtotal:':<12}Rs. {subtotal:>10,.2f}")
print(f"{'GST (18%):':<12}Rs. {gst:>10,.2f}")
print(f"{'Total:':<12}Rs. {total:>10,.2f}")
# Output:
# Invoice #2201 — Deshmukh Textiles
# Subtotal:   Rs.    8500.00
# GST (18%):  Rs.    1530.00
# Total:      Rs.   10030.00

# Example 4: Formatting a delivery ETA message
print("-" * 50)
print("Example 4: Delivery ETA Message")
customer = "Kavita Nair"
order_id = "MUM90231"
eta_minutes = 28
print(f"Hi {customer}, your order #{order_id} arrives in {eta_minutes} min.")
# Output: Hi Kavita Nair, your order #MUM90231 arrives in 28 min.


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Build a formatted "salary slip" line for an employee that shows:
#   name (left-aligned, width 15), department (width 12),
#   and net salary with a comma separator and 2 decimal places.
#
# Given:
emp_name = "Neha Kulkarni"
department = "Finance"
net_salary = 78542.5
#
# Expected output (approximately):
# Neha Kulkarni  Finance     Rs. 78,542.50

# YOUR CODE HERE


# SOLUTION:
# print(f"{emp_name:<15}{department:<12}Rs. {net_salary:,.2f}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file, you learned:
#   - The old % operator for simple substitution
#   - str.format() with positional and named placeholders
#   - f-strings — the modern, preferred approach
#   - Format specifiers for width, precision, alignment, and commas
#
# Next up (File 2 of 3): split(), join(), strip(), and replace()
# — the everyday string methods you'll use to clean and transform
# text data.
