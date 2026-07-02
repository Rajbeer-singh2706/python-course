"""
Day 8 — Practice Problems
File 3 of 3: Section D (json Module) + Section E (Mixed Challenges)

Cumulative scope: Days 2-8, focused on the json module plus a final
set of mixed challenges combining file I/O, csv, and json together.

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — multi-step, closer to a real task

Section index (across all 3 files):
    A. Prior Days Review        (day08_practise_problems_01_file_basics.py)
    B. File Basics               (day08_practise_problems_01_file_basics.py)
    C. csv Module                 (day08_practise_problems_02_csv_module.py)
    D. json Module                (this file)
    E. Mixed Challenges           (this file)

How to run:
    python day08_practise_problems_03_json_module.py
"""

import csv
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION D — json Module
# ════════════════════════════════════════════════════════════

# --- Problem D1 --- 🟢 Warm-up
# Create a dict "movie" with keys "title": "3 Idiots", "year": 2009,
# "rating": 8.4. Write it to "movie.json" using json.dump() with indent=4,
# then read it back and print the title.
# Expected output: 3 Idiots

# YOUR CODE HERE


# SOLUTION:
# movie = {"title": "3 Idiots", "year": 2009, "rating": 8.4}
# with open(path("movie.json"), "w") as f:
#     json.dump(movie, f, indent=4)
#
# with open(path("movie.json"), "r") as f:
#     loaded = json.load(f)
# print(loaded["title"])

print("-" * 50)


# --- Problem D2 --- 🟢 Warm-up
# Convert the dict {"city": "Pune", "pincode": 411001} to a JSON string
# using json.dumps(), print it, then convert it back to a dict using
# json.loads() and print the pincode.
# Expected output:
# {"city": "Pune", "pincode": 411001}
# 411001

# YOUR CODE HERE


# SOLUTION:
# data = {"city": "Pune", "pincode": 411001}
# json_str = json.dumps(data)
# print(json_str)
# parsed = json.loads(json_str)
# print(parsed["pincode"])

print("-" * 50)


# --- Problem D3 --- 🟡 Core
# Arjun has a list of 3 dicts representing books:
#   {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam"}
#   {"title": "The White Tiger", "author": "Aravind Adiga"}
#   {"title": "Train to Pakistan", "author": "Khushwant Singh"}
# Write this list to "books.json" with indent=4, read it back, and print
# each book as "TITLE by AUTHOR".
# Expected output:
# Wings of Fire by A.P.J. Abdul Kalam
# The White Tiger by Aravind Adiga
# Train to Pakistan by Khushwant Singh

# YOUR CODE HERE


# SOLUTION:
# books = [
#     {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam"},
#     {"title": "The White Tiger", "author": "Aravind Adiga"},
#     {"title": "Train to Pakistan", "author": "Khushwant Singh"},
# ]
# with open(path("books.json"), "w") as f:
#     json.dump(books, f, indent=4)
#
# with open(path("books.json"), "r") as f:
#     loaded_books = json.load(f)
#
# for book in loaded_books:
#     print(f"{book['title']} by {book['author']}")

print("-" * 50)


# --- Problem D4 --- 🟡 Core
# Write a function total_marks(filename) that reads a JSON file containing
# a list of student dicts (each with a "marks" key) and returns the sum
# of all marks. Test it on a file "test_scores.json" containing:
#   [{"name": "Priya", "marks": 88}, {"name": "Arjun", "marks": 72},
#    {"name": "Riya", "marks": 95}]
# Expected output: 255

# YOUR CODE HERE


# SOLUTION:
# scores = [
#     {"name": "Priya", "marks": 88},
#     {"name": "Arjun", "marks": 72},
#     {"name": "Riya", "marks": 95},
# ]
# with open(path("test_scores.json"), "w") as f:
#     json.dump(scores, f, indent=4)
#
# def total_marks(filename):
#     with open(filename, "r") as f:
#         data = json.load(f)
#     return sum(student["marks"] for student in data)
#
# print(total_marks(path("test_scores.json")))

print("-" * 50)


# --- Problem D5 --- 🔴 Challenge
# Sanjay stores his monthly budget as nested JSON:
#   {"month": "June", "categories": {"rent": 15000, "food": 6000,
#    "travel": 2500, "entertainment": 1500}}
# Write this to "budget.json", read it back, and print the category
# name with the HIGHEST spend, along with the TOTAL of all categories.
# Expected output: Highest: rent (Rs 15000), Total: Rs 25000

# YOUR CODE HERE


# SOLUTION:
# budget = {
#     "month": "June",
#     "categories": {"rent": 15000, "food": 6000, "travel": 2500, "entertainment": 1500},
# }
# with open(path("budget.json"), "w") as f:
#     json.dump(budget, f, indent=4)
#
# with open(path("budget.json"), "r") as f:
#     loaded_budget = json.load(f)
#
# categories = loaded_budget["categories"]
# highest_category = max(categories, key=categories.get)
# total = sum(categories.values())
#
# print(f"Highest: {highest_category} (Rs {categories[highest_category]}), Total: Rs {total}")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges (File I/O + csv + json + prior days)
# ════════════════════════════════════════════════════════════

# --- Problem E1 --- 🔴 Challenge
# Convert data from CSV to JSON. Priya has "attendance.csv" with columns
# "name", "days_present". Write code that:
#   1. Creates attendance.csv (csv.DictWriter) with rows:
#        {"name": "Priya", "days_present": 22}
#        {"name": "Arjun", "days_present": 19}
#        {"name": "Riya", "days_present": 25}
#   2. Reads the CSV with csv.DictReader, builds a list of dicts (convert
#      days_present to int), and writes that list to "attendance.json"
#      using json.dump() with indent=4.
#   3. Reads attendance.json back and prints the name of whoever has the
#      MOST days present.
# Expected output: Riya has the most days present: 25

# YOUR CODE HERE


# SOLUTION:
# att_fields = ["name", "days_present"]
# att_rows = [
#     {"name": "Priya", "days_present": 22},
#     {"name": "Arjun", "days_present": 19},
#     {"name": "Riya", "days_present": 25},
# ]
# with open(path("attendance.csv"), "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=att_fields)
#     writer.writeheader()
#     writer.writerows(att_rows)
#
# converted = []
# with open(path("attendance.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         converted.append({"name": row["name"], "days_present": int(row["days_present"])})
#
# with open(path("attendance.json"), "w") as f:
#     json.dump(converted, f, indent=4)
#
# with open(path("attendance.json"), "r") as f:
#     att_data = json.load(f)
#
# top_student = max(att_data, key=lambda s: s["days_present"])
# print(f"{top_student['name']} has the most days present: {top_student['days_present']}")

print("-" * 50)


# --- Problem E2 --- 🔴 Challenge
# Build a simple expense tracker. Write code that:
#   1. Starts with this list of expense dicts:
#        {"category": "Food", "amount": 3500}
#        {"category": "Travel", "amount": 1200}
#        {"category": "Food", "amount": 800}
#        {"category": "Rent", "amount": 15000}
#        {"category": "Travel", "amount": 600}
#   2. Uses a dictionary (Day 6) to sum amounts by category (so "Food"
#      totals 4300, "Travel" totals 1800, "Rent" totals 15000).
#   3. Writes the resulting summary dict to "expense_summary.json".
#   4. Reads it back and prints each category and total, sorted by total
#      amount from highest to lowest, in the format "Rent: Rs 15000".
# Expected output:
# Rent: Rs 15000
# Food: Rs 4300
# Travel: Rs 1800

# YOUR CODE HERE


# SOLUTION:
# expenses = [
#     {"category": "Food", "amount": 3500},
#     {"category": "Travel", "amount": 1200},
#     {"category": "Food", "amount": 800},
#     {"category": "Rent", "amount": 15000},
#     {"category": "Travel", "amount": 600},
# ]
#
# summary = {}
# for expense in expenses:
#     cat = expense["category"]
#     summary[cat] = summary.get(cat, 0) + expense["amount"]
#
# with open(path("expense_summary.json"), "w") as f:
#     json.dump(summary, f, indent=4)
#
# with open(path("expense_summary.json"), "r") as f:
#     loaded_summary = json.load(f)
#
# for category, total in sorted(loaded_summary.items(), key=lambda item: item[1], reverse=True):
#     print(f"{category}: Rs {total}")

print("-" * 50)


# --- Problem E3 --- 🔴 Challenge
# Meera wants a combined report. Write code that:
#   1. Creates "students.csv" (csv.DictWriter) with columns "name", "marks"
#      and rows: {"name": "Priya", "marks": 88}, {"name": "Arjun", "marks": 72},
#      {"name": "Riya", "marks": 95}, {"name": "Sanjay", "marks": 60}
#   2. Reads the CSV, calculates the class average (rounded to 2 decimals),
#      and builds a report dict:
#      {"class_average": <avg>, "top_scorer": <name of highest>,
#       "total_students": <count>}
#   3. Writes the report to "report.json" and prints it back in the format:
#      "Average: 78.75 | Top: Riya | Students: 4"
# Expected output: Average: 78.75 | Top: Riya | Students: 4

# YOUR CODE HERE


# SOLUTION:
# stu_fields = ["name", "marks"]
# stu_rows = [
#     {"name": "Priya", "marks": 88},
#     {"name": "Arjun", "marks": 72},
#     {"name": "Riya", "marks": 95},
#     {"name": "Sanjay", "marks": 60},
# ]
# with open(path("students.csv"), "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=stu_fields)
#     writer.writeheader()
#     writer.writerows(stu_rows)
#
# marks_list = []
# with open(path("students.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         marks_list.append({"name": row["name"], "marks": int(row["marks"])})
#
# class_average = round(sum(s["marks"] for s in marks_list) / len(marks_list), 2)
# top_scorer = max(marks_list, key=lambda s: s["marks"])["name"]
#
# report = {
#     "class_average": class_average,
#     "top_scorer": top_scorer,
#     "total_students": len(marks_list),
# }
#
# with open(path("report.json"), "w") as f:
#     json.dump(report, f, indent=4)
#
# with open(path("report.json"), "r") as f:
#     loaded_report = json.load(f)
#
# print(
#     f"Average: {loaded_report['class_average']} | "
#     f"Top: {loaded_report['top_scorer']} | "
#     f"Students: {loaded_report['total_students']}"
# )

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY — Day 8 Practice Problems (All Sections)
# ════════════════════════════════════════════════════════════
#
# Section A — Prior Days Review           : 2 problems
# Section B — File Basics                 : 5 problems
# Section C — csv Module                  : 5 problems
# Section D — json Module                 : 5 problems
# Section E — Mixed Challenges            : 3 problems
# ------------------------------------------------------------
# TOTAL                                   : 20 problems
#
# Difficulty breakdown: 7x 🟢 Warm-up | 8x 🟡 Core | 5x 🔴 Challenge
#
# Next up: Day 9 — Error Handling practice problems.

if __name__ == "__main__":
    print("Day 8 Practice — File 3 of 3 (Sections D-E) ran successfully.")
