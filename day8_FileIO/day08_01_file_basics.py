"""
Day 8 — File I/O
File 1 of 3: File Basics — open(), close(), read/write/append, the with statement

Covers:
    - Opening and closing files with open() / close()
    - File modes: 'r', 'w', 'a', 'r+'
    - Reading files: read(), readline(), readlines(), iterating line by line
    - Writing and appending to files
    - The `with` statement (context manager) and why it's preferred

Prerequisites:
    - Day 7: Strings & String Methods (split, strip, join)
    - Day 6: Data Structures (lists)

How to run:
    python day08_01_file_basics.py

Note: This script creates a few small text files inside a "day08_data" folder
next to this script, so you can see the results for yourself.
"""

import os

# Create a folder to keep our generated files organised
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    """Small helper so every example writes into the day08_data folder."""
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION 1: open() and close() — the manual way
# ════════════════════════════════════════════════════════════
#
# open(filename, mode) returns a "file object" that lets us read or write.
# Once we're done, we MUST call close() to free up the file and make sure
# everything we wrote is actually saved to disk.
#
# Common modes:
#   'r'  -> read (default). File must already exist.
#   'w'  -> write. Creates the file if missing, ERASES it if it already exists.
#   'a'  -> append. Creates the file if missing, adds to the end if it exists.
#   'r+' -> read and write, without erasing existing content.

print("── Concept: open() and close() ──")

f = open(path("diary.txt"), "w")   # 'w' mode creates/overwrites the file
f.write("Day 1: Arrived in Mumbai for the new job.\n")
f.write("Day 2: Explored Marine Drive in the evening.\n")
f.close()   # Without this, the write might not be flushed to disk!

print("diary.txt has been created and closed.")
# Output:
# diary.txt has been created and closed.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 2: The with statement — the preferred way
# ════════════════════════════════════════════════════════════
#
# Manually calling close() is risky: if an error happens between open()
# and close(), the file never gets closed properly. The `with` statement
# (a "context manager") automatically closes the file for us, even if
# something goes wrong inside the block. Always prefer `with`.

print("── Concept: with statement ──")

with open(path("diary.txt"), "a") as f:   # 'a' mode appends, doesn't erase
    f.write("Day 3: Tried vada pav near the office — loved it.\n")
# The file is automatically closed here, as soon as we leave the `with` block.

print("Appended Day 3 entry using 'with'. File is auto-closed now.")
# Output:
# Appended Day 3 entry using 'with'. File is auto-closed now.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 3: Reading files — read(), readline(), readlines()
# ════════════════════════════════════════════════════════════
#
# read()       -> returns the ENTIRE file as one big string
# readline()   -> returns ONE line at a time (keeps track of position)
# readlines()  -> returns a LIST of all lines (each line keeps its '\n')

print("── Concept: read() ──")
with open(path("diary.txt"), "r") as f:
    full_text = f.read()
print(full_text)
# Output:
# Day 1: Arrived in Mumbai for the new job.
# Day 2: Explored Marine Drive in the evening.
# Day 3: Tried vada pav near the office — loved it.

print("-" * 50)

print("── Concept: readline() ──")
with open(path("diary.txt"), "r") as f:
    first_line = f.readline()
    second_line = f.readline()
print(f"First line: {first_line.strip()}")
print(f"Second line: {second_line.strip()}")
# Output:
# First line: Day 1: Arrived in Mumbai for the new job.
# Second line: Day 2: Explored Marine Drive in the evening.

print("-" * 50)

print("── Concept: readlines() ──")
with open(path("diary.txt"), "r") as f:
    all_lines = f.readlines()
print(f"Type: {type(all_lines)}")
print(f"Number of lines: {len(all_lines)}")
print(f"Third line (raw, with \\n): {repr(all_lines[2])}")
# Output:
# Type: <class 'list'>
# Number of lines: 3
# Third line (raw, with \n): 'Day 3: Tried vada pav near the office — loved it.\n'

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 4: Iterating line by line (the memory-efficient way)
# ════════════════════════════════════════════════════════════
#
# For large files, reading the whole thing with read() or readlines()
# can use a lot of memory. Looping directly over the file object reads
# one line at a time, which is far more efficient.

print("── Concept: iterating over a file object ──")
with open(path("diary.txt"), "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"Line {line_number}: {line.strip()}")
# Output:
# Line 1: Day 1: Arrived in Mumbai for the new job.
# Line 2: Day 2: Explored Marine Drive in the evening.
# Line 3: Day 3: Tried vada pav near the office — loved it.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Writing a grocery list (Riya's Mumbai kitchen)
# ════════════════════════════════════════════════════════════

print("── Guided Example 1: Grocery list ──")
grocery_items = ["Basmati rice - 5kg", "Toor dal - 1kg", "Onions - 2kg", "Milk - 1L"]

with open(path("grocery_list.txt"), "w") as f:
    for item in grocery_items:
        f.write(item + "\n")

with open(path("grocery_list.txt"), "r") as f:
    print(f.read())
# Output:
# Basmati rice - 5kg
# Toor dal - 1kg
# Onions - 2kg
# Milk - 1L

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Appending expenses across multiple "sessions"
# ════════════════════════════════════════════════════════════

print("── Guided Example 2: Expense log ──")

# Simulate three separate program runs, each appending one expense
expenses_today = [
    "Auto fare - Rs 80",
    "Lunch at office canteen - Rs 150",
    "Chai and snacks - Rs 40",
]

# Start fresh for this demo
with open(path("expenses.txt"), "w") as f:
    pass  # creates an empty file

for expense in expenses_today:
    with open(path("expenses.txt"), "a") as f:
        f.write(expense + "\n")

with open(path("expenses.txt"), "r") as f:
    lines = f.readlines()

total_entries = len(lines)
print(f"Total expense entries logged: {total_entries}")
for entry in lines:
    print(f"  - {entry.strip()}")
# Output:
# Total expense entries logged: 3
#   - Auto fare - Rs 80
#   - Lunch at office canteen - Rs 150
#   - Chai and snacks - Rs 40

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: Checking if a file exists before reading
# ════════════════════════════════════════════════════════════

print("── Guided Example 3: Safe reading with os.path.exists ──")

report_path = path("sales_report.txt")

if os.path.exists(report_path):
    with open(report_path, "r") as f:
        print(f.read())
else:
    print(f"{os.path.basename(report_path)} does not exist yet. Creating it now...")
    with open(report_path, "w") as f:
        f.write("Arjun's Electronics Store - Weekly Sales\n")
        f.write("Mumbai Branch: Rs 45,000\n")
        f.write("Delhi Branch: Rs 38,500\n")
# Output:
# sales_report.txt does not exist yet. Creating it now...

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Word count on a text file
# ════════════════════════════════════════════════════════════

print("── Guided Example 4: Counting words in diary.txt ──")

with open(path("diary.txt"), "r") as f:
    text = f.read()

word_count = len(text.split())
line_count = len(text.splitlines())

print(f"diary.txt has {line_count} lines and {word_count} words.")
# Output:
# diary.txt has 3 lines and 28 words.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# 🔴 MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Sanjay Verma keeps a file called "attendance.txt" where each line is a
# student's name. Write code that:
#   1. Creates "attendance.txt" with these names, one per line:
#      "Priya Sharma", "Arjun Mehta", "Riya Deshmukh"
#   2. Appends one more name: "Sanjay Verma"
#   3. Reads the file back and prints each name with a serial number,
#      like "1. Priya Sharma"
#
# Expected output:
# 1. Priya Sharma
# 2. Arjun Mehta
# 3. Riya Deshmukh
# 4. Sanjay Verma

print("── Mini-Challenge: Attendance file ──")

# YOUR CODE HERE


# SOLUTION:
# students = ["Priya Sharma", "Arjun Mehta", "Riya Deshmukh"]
# with open(path("attendance.txt"), "w") as f:
#     for name in students:
#         f.write(name + "\n")
#
# with open(path("attendance.txt"), "a") as f:
#     f.write("Sanjay Verma\n")
#
# with open(path("attendance.txt"), "r") as f:
#     names = f.readlines()
#
# for i, name in enumerate(names, start=1):
#     print(f"{i}. {name.strip()}")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file we covered:
#   - open() / close() and why manual close() is risky
#   - The `with` statement for safe, automatic file closing
#   - File modes: 'r', 'w', 'a', 'r+'
#   - read(), readline(), readlines(), and iterating line by line
#   - Practical patterns: checking file existence, appending logs, word counts
#
# Next up (File 2 of 3): The `csv` module — reading and writing tabular
# data like spreadsheets and expense sheets.

if __name__ == "__main__":
    print("Day 8, File 1 of 3 (File Basics) ran successfully.")
