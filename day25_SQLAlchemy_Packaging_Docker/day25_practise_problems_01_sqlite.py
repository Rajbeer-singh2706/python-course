"""
Day 25 — Databases & Packaging — Practice Problems (File 1 of 3)

Cumulative scope: Days 1-25 (heaviest focus: sqlite3 module, Day 25)

Difficulty legend:
    🟢 Warm-up  — direct application of one concept
    🟡 Core      — combines 2-3 concepts, requires some thought
    🔴 Challenge — multi-step, closer to a real-world task

Section index:
    Section A — Prior Days Review (dictionaries, file I/O, custom exceptions)
    Section B — SQLite Basics (this file's current-day focus)

How to run:
    python day25_practise_problems_01_sqlite.py

All solutions are commented out below their starter code. Try each problem
yourself first, then uncomment the SOLUTION block to check your work.
"""

import sqlite3
import os
import csv

print("=" * 50)
print("SECTION A — Prior Days Review")
print("=" * 50)

# ────────────────────────────────────────────────────────────────
# Problem A1 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# You have a dictionary of restaurant names mapped to their Zomato rating.
# Write a function `highest_rated_restaurant(ratings)` that returns the
# name of the restaurant with the highest rating.
#
# Expected output for the sample data below: "Zomato Zaika"

ratings = {"Swiggy Bowl House": 4.2, "Zomato Zaika": 4.6, "Punjabi Tadka": 4.4}

# YOUR CODE HERE


# SOLUTION:
# def highest_rated_restaurant(ratings):
#     return max(ratings, key=ratings.get)
#
# print(highest_rated_restaurant(ratings))
# Expected output:
# Zomato Zaika

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem A2 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Write a function `write_and_read_expenses(filename, expenses)` that:
#   1. Writes a list of (item, amount) tuples to a CSV file with a header
#      row "item,amount"
#   2. Reads the file back in and returns the SUM of all amounts as a float
#   3. Deletes the file before returning
#
# Expected output for the sample data below: 615.0

expenses = [("Auto fare", 60), ("Chai", 15), ("Groceries", 540)]

# YOUR CODE HERE


# SOLUTION:
# def write_and_read_expenses(filename, expenses):
#     with open(filename, "w", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["item", "amount"])
#         writer.writerows(expenses)
#     with open(filename, "r", newline="") as f:
#         reader = csv.reader(f)
#         next(reader)  # skip header
#         total = sum(float(row[1]) for row in reader)
#     os.remove(filename)
#     return total
#
# print(write_and_read_expenses("expenses.csv", expenses))
# Expected output:
# 615.0

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem A3 — 🔴 Challenge
# ────────────────────────────────────────────────────────────────
# Define a custom exception class `InvalidOrderAmountError`. Write a
# function `validate_order(amount)` that raises this exception with the
# message f"Order amount must be positive, got {amount}" if amount <= 0,
# and otherwise returns f"Order of Rs. {amount} accepted".
#
# Catch the exception when calling validate_order(-50) and print its
# message.
#
# Expected output: "Order amount must be positive, got -50"

# YOUR CODE HERE


# SOLUTION:
# class InvalidOrderAmountError(Exception):
#     pass
#
# def validate_order(amount):
#     if amount <= 0:
#         raise InvalidOrderAmountError(f"Order amount must be positive, got {amount}")
#     return f"Order of Rs. {amount} accepted"
#
# try:
#     validate_order(-50)
# except InvalidOrderAmountError as e:
#     print(str(e))
# Expected output:
# Order amount must be positive, got -50

print("-" * 50)


print("=" * 50)
print("SECTION B — SQLite Basics")
print("=" * 50)

# ────────────────────────────────────────────────────────────────
# Problem B1 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Create a SQLite database "movies.db" with a table "movies" having
# columns: id (INTEGER PRIMARY KEY), title (TEXT), rating (REAL).
# Insert one row: ("3 Idiots", 8.4). Fetch and print it back using
# fetchone() with a WHERE id = 1 clause.
#
# Expected output: ('3 Idiots', 8.4)

# YOUR CODE HERE


# SOLUTION:
# DB = "movies.db"
# if os.path.exists(DB):
#     os.remove(DB)
# conn = sqlite3.connect(DB)
# conn.execute("CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT, rating REAL)")
# conn.commit()
# conn.execute("INSERT INTO movies (title, rating) VALUES (?, ?)", ("3 Idiots", 8.4))
# conn.commit()
# row = conn.execute("SELECT title, rating FROM movies WHERE id = 1").fetchone()
# print(row)
# Expected output:
# ('3 Idiots', 8.4)

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem B2 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Using the same "movies" table from B1, use executemany() to insert
# these three more movies:
#   ("Dangal", 8.3), ("Lagaan", 8.1), ("Zindagi Na Milegi Dobara", 8.2)
# Then SELECT all titles (fetchall()) and print the result.
#
# Expected output:
# [('3 Idiots',), ('Dangal',), ('Lagaan',), ('Zindagi Na Milegi Dobara',)]

# YOUR CODE HERE


# SOLUTION:
# movies = [("Dangal", 8.3), ("Lagaan", 8.1), ("Zindagi Na Milegi Dobara", 8.2)]
# conn.executemany("INSERT INTO movies (title, rating) VALUES (?, ?)", movies)
# conn.commit()
# all_rows = conn.execute("SELECT title FROM movies").fetchall()
# print(all_rows)
# Expected output:
# [('3 Idiots',), ('Dangal',), ('Lagaan',), ('Zindagi Na Milegi Dobara',)]

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem B3 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Write and run an UPDATE statement (using a parameterized query) that
# sets "Dangal"'s rating to 8.5. Then SELECT its rating back and print it.
#
# Expected output: 8.5

# YOUR CODE HERE


# SOLUTION:
# conn.execute("UPDATE movies SET rating = ? WHERE title = ?", (8.5, "Dangal"))
# conn.commit()
# updated = conn.execute("SELECT rating FROM movies WHERE title = ?", ("Dangal",)).fetchone()[0]
# print(updated)
# Expected output:
# 8.5

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem B4 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Set the connection's row_factory to sqlite3.Row. Write a query that
# selects title and rating for every movie with rating > 8.2, and build
# a list of dicts like {"title": ..., "rating": ...} from the results.
#
# Expected output:
# [{'title': '3 Idiots', 'rating': 8.4}, {'title': 'Dangal', 'rating': 8.5}]

# YOUR CODE HERE


# SOLUTION:
# conn.row_factory = sqlite3.Row
# cur = conn.cursor()
# cur.execute("SELECT title, rating FROM movies WHERE rating > ?", (8.2,))
# result = [{"title": r["title"], "rating": r["rating"]} for r in cur.fetchall()]
# print(result)
# Expected output:
# [{'title': '3 Idiots', 'rating': 8.4}, {'title': 'Dangal', 'rating': 8.5}]

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem B5 — 🔴 Challenge
# ────────────────────────────────────────────────────────────────
# Create two new tables in the same database:
#   stations(id INTEGER PRIMARY KEY, name TEXT)
#   bookings(id INTEGER PRIMARY KEY, station_id INTEGER, passengers INTEGER)
#
# Insert stations: "Mumbai Central", "New Delhi", "Chennai Central"
# Insert bookings: (station=Mumbai Central, 3), (station=Mumbai Central, 2),
#                  (station=New Delhi, 5), (station=Chennai Central, 1)
#
# Write a JOIN + GROUP BY query that returns each station's TOTAL
# passengers, ordered by total passengers descending, then station name
# ascending (as a tiebreaker for equal totals).
#
# Expected output:
# [('Mumbai Central', 5), ('New Delhi', 5), ('Chennai Central', 1)]

# YOUR CODE HERE


# SOLUTION:
# conn.execute("CREATE TABLE stations (id INTEGER PRIMARY KEY, name TEXT)")
# conn.execute("CREATE TABLE bookings (id INTEGER PRIMARY KEY, station_id INTEGER, passengers INTEGER)")
# conn.executemany("INSERT INTO stations (name) VALUES (?)",
#                   [("Mumbai Central",), ("New Delhi",), ("Chennai Central",)])
# conn.commit()
# conn.executemany(
#     "INSERT INTO bookings (station_id, passengers) VALUES (?, ?)",
#     [(1, 3), (1, 2), (2, 5), (3, 1)]
# )
# conn.commit()
# cur.execute("""
#     SELECT stations.name, SUM(bookings.passengers) as total_passengers
#     FROM bookings JOIN stations ON bookings.station_id = stations.id
#     GROUP BY stations.name
#     ORDER BY total_passengers DESC, stations.name ASC
# """)
# result = [(r["name"], r["total_passengers"]) for r in cur.fetchall()]
# print(result)
# conn.close()
# os.remove(DB)
# Expected output:
# [('Mumbai Central', 5), ('New Delhi', 5), ('Chennai Central', 1)]

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# Sections in this file:
#   A — Prior Days Review: 3 problems (dictionaries, CSV file I/O, custom exceptions)
#   B — SQLite Basics: 5 problems (CREATE TABLE, INSERT, executemany,
#       UPDATE, sqlite3.Row, multi-table JOIN + GROUP BY)
#
# Difficulty breakdown: 3 🟢 warm-up, 3 🟡 core, 2 🔴 challenge (8 problems)
#
# Next: day25_practise_problems_02_sqlalchemy.py — Section C, covering
# SQLAlchemy ORM models, sessions, relationships, and aggregation.

if __name__ == "__main__":
    print("Day 25 Practice Set — File 1 (Sections A-B) loaded. Try the problems above!")
