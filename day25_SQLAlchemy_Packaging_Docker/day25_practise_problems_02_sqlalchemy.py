"""
Day 25 — Databases & Packaging — Practice Problems (File 2 of 3)

Cumulative scope: Days 10-11 (OOP), Day 25 (SQLAlchemy ORM)

Difficulty legend:
    🟢 Warm-up  — direct application of one concept
    🟡 Core      — combines 2-3 concepts, requires some thought
    🔴 Challenge — multi-step, closer to a real-world task

Section index:
    Section C — SQLAlchemy ORM (models, sessions, relationships, aggregation)

How to run:
    python day25_practise_problems_02_sqlalchemy.py

All solutions are commented out below their starter code. Try each problem
yourself first, then uncomment the SOLUTION block to check your work.
"""

import os
from sqlalchemy import create_engine, ForeignKey, String, Integer, select, func, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

DB = "grocery_practice.db"
if os.path.exists(DB):
    os.remove(DB)


class Base(DeclarativeBase):
    pass


class Store(Base):
    __tablename__ = "stores"
    store_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    products: Mapped[list["Product"]] = relationship(back_populates="store")


class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column()
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.store_id"))
    store: Mapped["Store"] = relationship(back_populates="products")


print("=" * 50)
print("SECTION C — SQLAlchemy ORM")
print("=" * 50)
print("Models 'Store' and 'Product' are already defined above for you to use.")
print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem C1 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Create an engine pointing at DB and call Base.metadata.create_all() to
# build the "stores" and "products" tables. Then use sqlalchemy.inspect()
# to list the table names that now exist, sorted alphabetically.
#
# Expected output: ['products', 'stores']

# YOUR CODE HERE


# SOLUTION:
# engine = create_engine(f"sqlite:///{DB}")
# Base.metadata.create_all(engine)
# inspector = inspect(engine)
# print(sorted(inspector.get_table_names()))
# Expected output:
# ['products', 'stores']

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem C2 — 🟢 Warm-up
# ────────────────────────────────────────────────────────────────
# Using a Session, create a Store named "BigBasket Andheri" with two
# Product children: ("Amul Milk 1L", price=66.0) and
# ("Basmati Rice 5kg", price=450.0). Add and commit, then print the
# store's generated store_id.
#
# Expected output: 1

# YOUR CODE HERE


# SOLUTION:
# with Session(engine) as session:
#     bb = Store(name="BigBasket Andheri")
#     bb.products = [
#         Product(name="Amul Milk 1L", price=66.0),
#         Product(name="Basmati Rice 5kg", price=450.0),
#     ]
#     session.add(bb)
#     session.commit()
#     print(bb.store_id)
# Expected output:
# 1

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem C3 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Write a select() query that finds all products priced above Rs. 100,
# and print a list of their names.
#
# Expected output: ['Basmati Rice 5kg']

# YOUR CODE HERE


# SOLUTION:
# with Session(engine) as session:
#     stmt = select(Product).where(Product.price > 100)
#     expensive = session.scalars(stmt).all()
#     print([p.name for p in expensive])
# Expected output:
# ['Basmati Rice 5kg']

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem C4 — 🟡 Core
# ────────────────────────────────────────────────────────────────
# Fetch the "BigBasket Andheri" store by name, then use its `.products`
# relationship to print a list of all its product names (no extra query
# needed — the relationship does the work).
#
# Expected output: ['Amul Milk 1L', 'Basmati Rice 5kg']

# YOUR CODE HERE


# SOLUTION:
# with Session(engine) as session:
#     store = session.scalars(select(Store).where(Store.name == "BigBasket Andheri")).first()
#     print([p.name for p in store.products])
# Expected output:
# ['Amul Milk 1L', 'Basmati Rice 5kg']

print("-" * 50)


# ────────────────────────────────────────────────────────────────
# Problem C5 — 🔴 Challenge
# ────────────────────────────────────────────────────────────────
# Write a query using func.sum() and a join() + group_by() that returns
# each store's name paired with the total value of its product catalog
# (sum of all its products' prices).
#
# Expected output: [('BigBasket Andheri', 516.0)]

# YOUR CODE HERE


# SOLUTION:
# with Session(engine) as session:
#     stmt = (
#         select(Store.name, func.sum(Product.price))
#         .join(Product)
#         .group_by(Store.name)
#     )
#     print(list(session.execute(stmt)))
# Expected output:
# [('BigBasket Andheri', 516.0)]

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# Section in this file:
#   C — SQLAlchemy ORM: 5 problems (create_all + inspect, Session CRUD,
#       select().where() filtering, relationship traversal, func.sum()
#       aggregation with join + group_by)
#
# Difficulty breakdown: 2 🟢 warm-up, 2 🟡 core, 1 🔴 challenge (5 problems)
#
# Next: day25_practise_problems_03_packaging_docker.py — Section D
# (packaging & Docker) and Section E (mixed challenges combining
# everything from Day 25).

if __name__ == "__main__":
    print("Day 25 Practice Set — File 2 (Section C) loaded. Try the problems above!")
