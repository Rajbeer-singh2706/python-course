"""
Day 07 — Strings & String Methods
File 2 of 3: split(), join(), strip(), replace() & Common Methods

Covers:
    - split() — breaking a string into a list
    - join() — combining a list into a string
    - strip() / lstrip() / rstrip() — removing whitespace
    - replace() — substituting substrings
    - Other everyday methods: upper(), lower(), title(), find(), count()

Prerequisites:
    - Day 06 (Data Structures — lists)
    - Day 07 File 1 (String Formatting & f-strings)

How to run:
    python day07_02_string_methods.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: split() — String to List
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("SECTION 1: split()")
print("=" * 50)

# split() defaults to splitting on whitespace
full_name = "Arjun Kumar Verma"
name_parts = full_name.split()
print(name_parts)
# Output: ['Arjun', 'Kumar', 'Verma']

# You can split on any delimiter
csv_line = "Priya,28,Mumbai,Software Engineer"
fields = csv_line.split(",")
print(fields)
# Output: ['Priya', '28', 'Mumbai', 'Software Engineer']

# maxsplit limits how many splits happen
path = "home/priya/documents/report.pdf"
first_two = path.split("/", maxsplit=1)
print(first_two)
# Output: ['home', 'priya/documents/report.pdf']


# ────────────────────────────────────────────────────────────
# ── Concept: join() — List to String ──
# ────────────────────────────────────────────────────────────
print("-" * 50)
print("join()")
print("-" * 50)

# join() is called ON the separator, and takes an iterable
words = ["Sanjay", "lives", "in", "Delhi"]
sentence = " ".join(words)
print(sentence)
# Output: Sanjay lives in Delhi

# A common pattern: build a CSV row from a list
row_values = ["Riya Deshmukh", "31", "Pune", "Data Analyst"]
csv_row = ",".join(row_values)
print(csv_row)
# Output: Riya Deshmukh,31,Pune,Data Analyst

# join() with a different separator
tags = ["python", "beginner", "mumbai-batch"]
hashtags = " #".join(tags)
print(f"#{hashtags}")
# Output: #python #beginner #mumbai-batch


# ────────────────────────────────────────────────────────────
# ── Concept: strip(), lstrip(), rstrip() ──
# ────────────────────────────────────────────────────────────
# Real-world data (form inputs, file reads) often has extra
# whitespace. strip() removes it from both ends by default.

print("-" * 50)
print("strip() family")
print("-" * 50)

messy_input = "   Priya Sharma   "  # simulating input() from a form
print(f"[{messy_input.strip()}]")
# Output: [Priya Sharma]

print(f"[{messy_input.lstrip()}]")
# Output: [Priya Sharma   ]

print(f"[{messy_input.rstrip()}]")
# Output: [   Priya Sharma]

# strip() can also remove specific characters, not just whitespace
raw_code = "###PYTHON-COURSE###"
print(raw_code.strip("#"))
# Output: PYTHON-COURSE


# ────────────────────────────────────────────────────────────
# ── Concept: replace() ──
# ────────────────────────────────────────────────────────────
print("-" * 50)
print("replace()")
print("-" * 50)

address = "12 MG Road, Bengaluru - 560001"
updated_address = address.replace("Bengaluru", "Mumbai")
print(updated_address)
# Output: 12 MG Road, Mumbai - 560001

# replace() has an optional count argument
noisy_text = "hmm hmm hmm, that's interesting"
cleaned_once = noisy_text.replace("hmm", "well", 1)
print(cleaned_once)
# Output: well hmm hmm, that's interesting


# ────────────────────────────────────────────────────────────
# ── Concept: Other Everyday Methods ──
# ────────────────────────────────────────────────────────────
print("-" * 50)
print("Other Common Methods")
print("-" * 50)

product_name = "wireless mouse"
print(product_name.upper())        # WIRELESS MOUSE
print(product_name.title())        # Wireless Mouse
print(product_name.capitalize())   # Wireless mouse

review_text = "Great product, great price, great service!"
print(review_text.count("great"))  # Output: 2 (case-sensitive)
print(review_text.lower().count("great"))  # Output: 3

order_note = "Deliver to Riya Deshmukh, Flat 4B"
print(order_note.find("Deshmukh"))   # Output: 17 (starting index)
print(order_note.startswith("Deliver"))  # Output: True
print(order_note.endswith("4B"))         # Output: True


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — India-Contextualized
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)

# Example 1: Cleaning a messy user-entered phone number
print("-" * 50)
print("Example 1: Cleaning a Phone Number")
raw_phone = "  +91-98765 43210  "
clean_phone = raw_phone.strip().replace("-", "").replace(" ", "")
print(clean_phone)
# Output: +919876543210

# Example 2: Splitting a full address into parts
print("-" * 50)
print("Example 2: Splitting an Address")
full_address = "Flat 302, Green Meadows, Andheri West, Mumbai, 400058"
address_parts = full_address.split(", ")
print(address_parts)
print(f"City: {address_parts[-2]}, PIN: {address_parts[-1]}")
# Output:
# ['Flat 302', 'Green Meadows', 'Andheri West', 'Mumbai', '400058']
# City: Mumbai, PIN: 400058

# Example 3: Rebuilding a name from parts (join)
print("-" * 50)
print("Example 3: Rebuilding a Full Name")
first = "Sanjay"
middle = "Ramesh"
last = "Verma"
full = " ".join([first, middle, last])
print(full)
# Output: Sanjay Ramesh Verma

# Example 4: Anonymizing an email for a support ticket log
print("-" * 50)
print("Example 4: Anonymizing an Email")
email = "priya.sharma@example.com"
username, domain = email.split("@")
masked = username[0] + "***@" + domain
print(masked)
# Output: p***@example.com


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Given a raw CSV line simulating a student record, clean it up
# and print each field on its own line, stripped of extra spaces.
#
# Given:
raw_record = "  Arjun Kumar , 22 ,  Delhi , Computer Science  "
#
# Expected output:
# Arjun Kumar
# 22
# Delhi
# Computer Science

# YOUR CODE HERE


# SOLUTION:
# fields = raw_record.split(",")
# for field in fields:
#     print(field.strip())


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file, you learned:
#   - split() to break strings into lists
#   - join() to combine lists back into strings
#   - strip()/lstrip()/rstrip() to clean whitespace
#   - replace() to substitute substrings
#   - upper(), lower(), title(), count(), find(), startswith(),
#     endswith() for everyday text operations
#
# Next up (File 3 of 3): the `re` module — pattern matching with
# search(), match(), and findall().
