"""
Day 07 — Strings & String Methods
File 3 of 3: The `re` Module — Pattern Matching Basics

Covers:
    - re.search() — find a pattern anywhere in a string
    - re.match() — find a pattern at the start of a string
    - re.findall() — find all non-overlapping matches
    - Basic pattern syntax: \\d, \\w, \\s, +, *, {n}

Prerequisites:
    - Day 07 File 1 (String Formatting)
    - Day 07 File 2 (split, join, strip, replace)

How to run:
    python day07_03_regex_basics.py
"""

import re

# ════════════════════════════════════════════════════════════
# SECTION 1: Why Regular Expressions?
# ════════════════════════════════════════════════════════════
# String methods like find() and replace() work on exact text.
# Regular expressions (regex) let you match PATTERNS — like
# "any 10-digit number" or "any word starting with a capital
# letter" — which is far more powerful for validating and
# extracting data.

print("=" * 50)
print("SECTION 1: Why Regex?")
print("=" * 50)

feedback = "Contact Arjun at 9876543210 or arjun.k@example.com"
# Finding a phone number with plain string methods is painful.
# With regex, it's one line:
phone_match = re.search(r"\d{10}", feedback)
print(phone_match.group())
# Output: 9876543210


# ────────────────────────────────────────────────────────────
# ── Concept: re.search() ──
# ────────────────────────────────────────────────────────────
# search() scans the ENTIRE string and returns the first match
# as a Match object, or None if nothing matches.

print("-" * 50)
print("re.search()")
print("-" * 50)

review = "Delivery was late, but the packaging was excellent."
result = re.search(r"late", review)
if result:
    print(f"Found '{result.group()}' at position {result.start()}")
# Output: Found 'late' at position 14

no_result = re.search(r"refund", review)
print(no_result)
# Output: None


# ────────────────────────────────────────────────────────────
# ── Concept: re.match() ──
# ────────────────────────────────────────────────────────────
# match() only checks the BEGINNING of the string. If the
# pattern isn't right at the start, it returns None — even if
# it exists elsewhere in the string.

print("-" * 50)
print("re.match()")
print("-" * 50)

order_code = "MUM2026-0093"
starts_with_mum = re.match(r"MUM", order_code)
print(starts_with_mum.group() if starts_with_mum else "No match")
# Output: MUM

order_code_2 = "ORD-MUM2026-0093"
starts_with_mum_2 = re.match(r"MUM", order_code_2)
print(starts_with_mum_2)
# Output: None (MUM is not at the very start here)


# ────────────────────────────────────────────────────────────
# ── Concept: re.findall() ──
# ────────────────────────────────────────────────────────────
# findall() returns a LIST of every non-overlapping match in
# the string — the most commonly used function for extraction.

print("-" * 50)
print("re.findall()")
print("-" * 50)

transaction_log = "Paid Rs.500, Rs.1200, and Rs.75 across 3 orders"
amounts = re.findall(r"\d+", transaction_log)
print(amounts)
# Output: ['500', '1200', '75', '3']

# \d = digit, \w = word character (letters/digits/underscore),
# \s = whitespace. + means "one or more".
emails_text = "Reach priya@example.com or sanjay.verma@company.co.in"
emails = re.findall(r"[\w.]+@[\w.]+", emails_text)
print(emails)
# Output: ['priya@example.com', 'sanjay.verma@company.co.in']


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — India-Contextualized
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)

# Example 1: Validating a 10-digit Indian mobile number
print("-" * 50)
print("Example 1: Validating a Mobile Number")
candidate_number = "9876543210"
is_valid = bool(re.match(r"^[6-9]\d{9}$", candidate_number))
print(f"{candidate_number} valid? {is_valid}")
# Output: 9876543210 valid? True

# Example 2: Extracting all PIN codes from a delivery log
print("-" * 50)
print("Example 2: Extracting PIN Codes")
delivery_log = "Delivered to 400058, 110001, and 560001 today"
pin_codes = re.findall(r"\b\d{6}\b", delivery_log)
print(pin_codes)
# Output: ['400058', '110001', '560001']

# Example 3: Checking if a username follows the allowed pattern
print("-" * 50)
print("Example 3: Checking a Username Pattern")
username = "riya_deshmukh_99"
is_valid_username = bool(re.match(r"^[a-z_]+\d*$", username))
print(f"{username} valid? {is_valid_username}")
# Output: riya_deshmukh_99 valid? True

# Example 4: Splitting free text into individual sentences
print("-" * 50)
print("Example 4: Extracting Sentences")
paragraph = "Priya joined in 2023. She works in Mumbai. She loves Python!"
sentences = re.findall(r"[^.!]+[.!]", paragraph)
print([s.strip() for s in sentences])
# Output: ['Priya joined in 2023.', 'She works in Mumbai.', 'She loves Python!']


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Given a raw support message, extract every email address it
# contains using re.findall().
#
# Given:
support_message = (
    "Please cc sanjay.verma@example.com and priya.s@company.in "
    "on all future updates."
)
#
# Expected output:
# ['sanjay.verma@example.com', 'priya.s@company.in']

# YOUR CODE HERE


# SOLUTION:
# found_emails = re.findall(r"[\w.]+@[\w.]+", support_message)
# print(found_emails)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file, you learned:
#   - re.search() — find the first match anywhere in a string
#   - re.match() — check only the start of a string
#   - re.findall() — collect every match as a list
#   - Basic pattern syntax: \d, \w, \s, +, {n}, character classes
#
# This wraps up Day 07! Next session (Day 08) covers File I/O —
# reading, writing, and working with CSV and JSON files.
