"""
Day 25 — Databases & Packaging
File 1 of 3: SQLite Basics with the `sqlite3` Module

What this file covers:
    - Connecting to a SQLite database file with sqlite3.connect()
    - Creating tables with CREATE TABLE
    - Inserting rows safely with parameterized queries (avoiding SQL injection)
    - Reading rows with SELECT, fetchone(), fetchall()
    - Updating and deleting rows
    - Using the `with` statement / context managers for connections
    - Committing transactions and understanding autocommit pitfalls

Prerequisites:
    - Day 8 (File I/O) — reading/writing files, context managers
    - Day 9 (Error Handling) — try/except for handling database errors

How to run:
    python day25_01_sqlite_basics.py

This file creates a temporary database file called "tiffin_orders.db" in the
same folder. Feel free to delete it after running — the script recreates it
fresh every time it runs.
"""

import sqlite3
import os

# ════════════════════════════════════════════════════════════════
# SECTION 1: Connecting to SQLite and Creating a Table
# ════════════════════════════════════════════════════════════════
#
# SQLite stores an entire database in a single file on disk. Python ships
# with the `sqlite3` module built in — no installation needed. A connection
# object represents an open link to that file, and a cursor is what you use
# to actually run SQL commands and read results back.
#
# Why SQLite for this lesson: it needs zero setup (no server, no username/
# password), which makes it perfect for learning — and it is genuinely used
# in production for small-to-medium apps, mobile apps, and local caching.

DB_FILE = "tiffin_orders.db"

# Start fresh each time we run this file, so the demo output is predictable
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# ── Opening a Connection ──
# sqlite3.connect() creates the file if it doesn't exist yet.
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# ── Creating a Table ──
# CREATE TABLE defines the column names and types. SQLite is flexible about
# types compared to other databases, but it's good practice to declare them
# clearly anyway — it documents intent and Python's sqlite3 module still
# respects the common ones (INTEGER, TEXT, REAL, BLOB).
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name          TEXT NOT NULL,
        city          TEXT NOT NULL,
        phone         TEXT,
        is_premium    INTEGER DEFAULT 0
    )
""")
connection.commit()
print("Table 'customers' created.")
# Output:
# Table 'customers' created.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2: Inserting Rows Safely (Parameterized Queries)
# ════════════════════════════════════════════════════════════════
#
# NEVER build SQL strings with f-strings or % formatting when inserting
# user-supplied data — that opens the door to SQL injection attacks.
# Instead, use "?" placeholders and pass values as a tuple. sqlite3 escapes
# them safely for you.

# ── Single Insert ──
cursor.execute(
    "INSERT INTO customers (name, city, phone, is_premium) VALUES (?, ?, ?, ?)",
    ("Priya Sharma", "Mumbai", "9820011223", 1)
)
connection.commit()
print(f"Inserted customer with id: {cursor.lastrowid}")
# Output:
# Inserted customer with id: 1

# ── Bulk Insert with executemany() ──
# When inserting many rows at once, executemany() is far more efficient
# than looping and calling execute() repeatedly.
more_customers = [
    ("Arjun Mehta", "Delhi", "9911223344", 0),
    ("Riya Deshmukh", "Pune", "9765432109", 1),
    ("Sanjay Verma", "Jaipur", "9812345670", 0),
    ("Meera Iyer", "Chennai", "9944556677", 1),
]
cursor.executemany(
    "INSERT INTO customers (name, city, phone, is_premium) VALUES (?, ?, ?, ?)",
    more_customers
)
connection.commit()
print(f"Total rows inserted this batch: {cursor.rowcount}")
# Output:
# Total rows inserted this batch: 4

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3: Reading Rows — fetchone(), fetchall(), fetchmany()
# ════════════════════════════════════════════════════════════════

# ── fetchall(): get every matching row as a list of tuples ──
cursor.execute("SELECT customer_id, name, city FROM customers")
all_rows = cursor.fetchall()
print("All customers:")
for row in all_rows:
    print(f"  {row}")
# Output:
# All customers:
#   (1, 'Priya Sharma', 'Mumbai')
#   (2, 'Arjun Mehta', 'Delhi')
#   (3, 'Riya Deshmukh', 'Pune')
#   (4, 'Sanjay Verma', 'Jaipur')
#   (5, 'Meera Iyer', 'Chennai')

# ── fetchone(): get a single row (useful for "find by id" queries) ──
cursor.execute("SELECT name, city FROM customers WHERE customer_id = ?", (2,))
single_row = cursor.fetchone()
print(f"Customer #2: {single_row}")
# Output:
# Customer #2: ('Arjun Mehta', 'Delhi')

# ── WHERE clause with filtering ──
cursor.execute("SELECT name, city FROM customers WHERE is_premium = 1")
premium_customers = cursor.fetchall()
print(f"Premium customers: {premium_customers}")
# Output:
# Premium customers: [('Priya Sharma', 'Mumbai'), ('Riya Deshmukh', 'Pune'), ('Meera Iyer', 'Chennai')]

# ── Making rows dict-like with row_factory ──
# By default, rows come back as plain tuples. Setting row_factory to
# sqlite3.Row lets you access columns by name, which is much more readable.
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute("SELECT name, city FROM customers WHERE customer_id = ?", (1,))
row = cursor.fetchone()
print(f"Name: {row['name']}, City: {row['city']}")
# Output:
# Name: Priya Sharma, City: Mumbai

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 4: Updating and Deleting Rows
# ════════════════════════════════════════════════════════════════

# ── UPDATE ──
cursor.execute(
    "UPDATE customers SET is_premium = ? WHERE name = ?",
    (1, "Arjun Mehta")
)
connection.commit()
print(f"Rows updated: {cursor.rowcount}")
# Output:
# Rows updated: 1

# ── DELETE ──
cursor.execute("DELETE FROM customers WHERE name = ?", ("Sanjay Verma",))
connection.commit()
print(f"Rows deleted: {cursor.rowcount}")
# Output:
# Rows deleted: 1

# ── Verifying the changes ──
cursor.execute("SELECT COUNT(*) FROM customers")
count = cursor.fetchone()[0]
print(f"Remaining customers: {count}")
# Output:
# Remaining customers: 4

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 5: Using `with` for Connections (Context Managers)
# ════════════════════════════════════════════════════════════════
#
# IMPORTANT SQLITE QUIRK: `with sqlite3.connect(...) as conn:` only wraps
# the TRANSACTION (auto-commit on success, auto-rollback on error) — it does
# NOT close the connection for you the way a file's `with` block does.
# You still need conn.close() explicitly, or use a nested try/finally.

connection.close()

with sqlite3.connect(DB_FILE) as conn:
    conn.execute(
        "INSERT INTO customers (name, city, phone, is_premium) VALUES (?, ?, ?, ?)",
        ("Karan Nair", "Bengaluru", "9900112233", 0)
    )
    # No explicit commit() needed here — the `with` block commits automatically
    # on successful exit, because sqlite3's context manager wraps the transaction.
print("Insert via 'with' block committed automatically.")
# Output:
# Insert via 'with' block committed automatically.

# Still need to close the connection manually — `with` did not do this
conn.close()

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 6: Guided Examples (Indian E-Commerce Context)
# ════════════════════════════════════════════════════════════════

def setup_orders_table(conn):
    """Create an 'orders' table linked to customers via a foreign key."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id   INTEGER NOT NULL,
            item          TEXT NOT NULL,
            amount_rupees REAL NOT NULL,
            status        TEXT DEFAULT 'placed',
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        )
    """)
    conn.commit()


# ── Example 1: Setting up a related "orders" table ──
conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
setup_orders_table(conn)
print("Example 1: 'orders' table created with a foreign key to 'customers'.")
# Output:
# Example 1: 'orders' table created with a foreign key to 'customers'.

# ── Example 2: Placing a few Swiggy-style food orders ──
sample_orders = [
    (1, "Butter Chicken Thali", 349.0, "delivered"),
    (2, "Masala Dosa Combo", 179.0, "preparing"),
    (3, "Paneer Tikka Wrap", 220.0, "delivered"),
    (1, "Cold Coffee", 90.0, "placed"),
]
conn.executemany(
    "INSERT INTO orders (customer_id, item, amount_rupees, status) VALUES (?, ?, ?, ?)",
    sample_orders
)
conn.commit()
print(f"Example 2: {conn.execute('SELECT COUNT(*) FROM orders').fetchone()[0]} orders placed.")
# Output:
# Example 2: 4 orders placed.

# ── Example 3: JOIN across customers and orders ──
join_query = """
    SELECT customers.name, orders.item, orders.amount_rupees, orders.status
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id
    ORDER BY orders.order_id
"""
print("Example 3: Orders with customer names (JOIN)")
for row in conn.execute(join_query):
    print(f"  {row['name']} ordered {row['item']} (Rs. {row['amount_rupees']}) — {row['status']}")
# Output:
# Example 3: Orders with customer names (JOIN)
#   Priya Sharma ordered Butter Chicken Thali (Rs. 349.0) — delivered
#   Arjun Mehta ordered Masala Dosa Combo (Rs. 179.0) — preparing
#   Riya Deshmukh ordered Paneer Tikka Wrap (Rs. 220.0) — delivered
#   Priya Sharma ordered Cold Coffee (Rs. 90.0) — placed

# ── Example 4: Aggregation — total spend per customer ──
agg_query = """
    SELECT customers.name, SUM(orders.amount_rupees) AS total_spent
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id
    GROUP BY customers.name
    ORDER BY total_spent DESC
"""
print("Example 4: Total spend per customer")
for row in conn.execute(agg_query):
    print(f"  {row['name']}: Rs. {row['total_spent']}")
# Output:
# Example 4: Total spend per customer
#   Priya Sharma: Rs. 439.0
#   Riya Deshmukh: Rs. 220.0
#   Arjun Mehta: Rs. 179.0

conn.close()
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Write a function `get_orders_by_status(db_file, status)` that:
#   1. Opens a connection to db_file
#   2. Returns a list of dicts, each with keys "customer_name" and "item",
#      for every order matching the given status
#   3. Closes the connection before returning
#
# Expected output when called with status="delivered":
#   [{'customer_name': 'Priya Sharma', 'item': 'Butter Chicken Thali'},
#    {'customer_name': 'Riya Deshmukh', 'item': 'Paneer Tikka Wrap'}]

# YOUR CODE HERE


# ── Solution (uncomment to check your work) ──
# def get_orders_by_status(db_file, status):
#     conn = sqlite3.connect(db_file)
#     conn.row_factory = sqlite3.Row
#     query = """
#         SELECT customers.name AS customer_name, orders.item
#         FROM orders
#         JOIN customers ON orders.customer_id = customers.customer_id
#         WHERE orders.status = ?
#     """
#     rows = conn.execute(query, (status,)).fetchall()
#     conn.close()
#     return [{"customer_name": row["customer_name"], "item": row["item"]} for row in rows]
#
# result = get_orders_by_status(DB_FILE, "delivered")
# print(result)
# Expected output:
# [{'customer_name': 'Priya Sharma', 'item': 'Butter Chicken Thali'},
#  {'customer_name': 'Riya Deshmukh', 'item': 'Paneer Tikka Wrap'}]


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Connecting to SQLite files with sqlite3.connect()
#   - Creating tables and using parameterized queries (? placeholders)
#   - executemany() for bulk inserts
#   - fetchone(), fetchall(), and sqlite3.Row for dict-style access
#   - UPDATE / DELETE with WHERE clauses
#   - The `with` block's transaction-only behaviour (still need conn.close())
#   - JOINs and GROUP BY aggregations across related tables
#
# Next up: day25_02_sqlalchemy_orm.py — the same operations, but using
# SQLAlchemy's ORM so you can work with Python objects instead of raw SQL.

if __name__ == "__main__":
    print("Day 25, File 1 complete: SQLite basics demonstrated end-to-end.")
