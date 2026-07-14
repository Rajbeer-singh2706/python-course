"""
Day 8 — Practice Problems
File 1 of 3: Section A (Prior Days Review) + Section B (File Basics)

Cumulative scope: Days 2-8 (variables, control flow, loops, functions,
data structures, strings, file basics).

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — multi-step, closer to a real task

Section index (across all 3 files):
    A. Prior Days Review        (this file)
    B. File Basics               (this file)
    C. csv Module                 (day08_practise_problems_02_csv_module.py)
    D. json Module                (day08_practise_problems_03_json_module.py)
    E. Mixed Challenges           (day08_practise_problems_03_json_module.py)

How to run:
    python day08_practise_problems_01_file_basics.py
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review (Days 2-7)
# ════════════════════════════════════════════════════════════

# --- Problem A1 --- 🟢 Warm-up
# Given the list of prices below, use a list comprehension (Day 6) to
# create a new list "discounted" where every price is reduced by 10%.
# Print the discounted list.
# Expected output: [450.0, 900.0, 1350.0]

prices = [500, 1000, 1500]

# YOUR CODE HERE


# SOLUTION:
# discounted = [p * 0.9 for p in prices]
# print(discounted)

print("-" * 50)


# --- Problem A2 --- 🟡 Core
# Meera has a sentence stored in a string (Day 7). Use split(), a loop,
# and an if condition to count how many words start with a capital letter.
# Expected output: 5

sentence = "Meera Went To Bengaluru for a Conference"

# YOUR CODE HERE


# SOLUTION:
# words = sentence.split()
# capital_count = 0
# for word in words:
#     if word[0].isupper():
#         capital_count += 1
# print(capital_count)

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — File Basics (open, with, read/write/append)
# ════════════════════════════════════════════════════════════

# --- Problem B1 --- 🟢 Warm-up
# Using the `with` statement, create a file called "notes.txt" (use the
# path() helper) and write the line "Meeting with Priya at 4 PM" to it.
# Then read the file back and print its contents.
# Expected output: Meeting with Priya at 4 PM

# YOUR CODE HERE


# SOLUTION:
# with open(path("notes.txt"), "w") as f:
#     f.write("Meeting with Priya at 4 PM")
#
# with open(path("notes.txt"), "r") as f:
#     print(f.read())

print("-" * 50)


# --- Problem B2 --- 🟢 Warm-up
# Append the line "Follow up with Arjun tomorrow" to "notes.txt" from B1.
# Then read all lines using readlines() and print how many lines the
# file now has.
# Expected output: 2

# YOUR CODE HERE


# SOLUTION:
# with open(path("notes.txt"), "a") as f:
#     f.write("\nFollow up with Arjun tomorrow")
#
# with open(path("notes.txt"), "r") as f:
#     lines = f.readlines()
# print(len(lines))

print("-" * 50)


# --- Problem B3 --- 🟡 Core
# Riya keeps a "cities.txt" file with one city per line. Write code that:
#   1. Creates cities.txt with: "Mumbai", "Delhi", "Pune", "Bengaluru"
#   2. Reads it back and prints only the cities whose name has more than
#      5 letters, one per line.
# Expected output:
# Mumbai
# Bengaluru

# YOUR CODE HERE


# SOLUTION:
# cities = ["Mumbai", "Delhi", "Pune", "Bengaluru"]
# with open(path("cities.txt"), "w") as f:
#     for city in cities:
#         f.write(city + "\n")
#
# with open(path("cities.txt"), "r") as f:
#     for line in f:
#         city_name = line.strip()
#         if len(city_name) > 5:
#             print(city_name)

print("-" * 50)


# --- Problem B4 --- 🟡 Core
# Write a function count_lines(filename) that opens the given file with
# `with` and returns the number of lines in it. Test it on "cities.txt"
# from B3.
# Expected output: 4

# YOUR CODE HERE


# SOLUTION:
# def count_lines(filename):
#     with open(filename, "r") as f:
#         return len(f.readlines())
#
# print(count_lines(path("cities.txt")))

print("-" * 50)


# --- Problem B5 --- 🔴 Challenge
# Sanjay has a file "marks.txt" where each line is "name,marks" (as plain
# text, not real CSV yet — that's next file!). Write code that:
#   1. Creates marks.txt with these lines:
#      "Priya,88", "Arjun,72", "Riya,95", "Sanjay,60"
#   2. Reads the file, splits each line on the comma, converts marks to
#      int, and prints the name of the student with the HIGHEST marks.
# Expected output: Riya scored the highest with 95 marks.

# YOUR CODE HERE


# SOLUTION:
# records = ["Priya,88", "Arjun,72", "Riya,95", "Sanjay,60"]
# with open(path("marks.txt"), "w") as f:
#     for record in records:
#         f.write(record + "\n")
#
# top_name = None
# top_marks = -1
# with open(path("marks.txt"), "r") as f:
#     for line in f:
#         name, marks_str = line.strip().split(",")
#         marks = int(marks_str)
#         if marks > top_marks:
#             top_marks = marks
#             top_name = name
#
# print(f"{top_name} scored the highest with {top_marks} marks.")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections covered in this file:
#   A. Prior Days Review — 2 problems (list comprehension, strings)
#   B. File Basics — 5 problems (open, with, read/write/append)
#
# Difficulty breakdown: 3x 🟢 Warm-up | 3x 🟡 Core | 1x 🔴 Challenge
#
# Next up: day08_practise_problems_02_csv_module.py — Section C (csv module)

if __name__ == "__main__":
    print("Day 8 Practice — File 1 of 3 (Sections A-B) ran successfully.")
