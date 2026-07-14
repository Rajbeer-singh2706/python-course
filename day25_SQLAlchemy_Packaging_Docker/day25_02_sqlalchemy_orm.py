"""
Day 25 — Databases & Packaging
File 2 of 3: SQLAlchemy ORM — Models, Sessions, and CRUD

What this file covers:
    - What an ORM is and why it's useful (mapping Python classes to tables)
    - Declarative models with SQLAlchemy 2.0 style (Mapped, mapped_column)
    - Creating an engine and initializing tables with Base.metadata.create_all()
    - Sessions — the ORM's "unit of work" for talking to the database
    - CRUD operations using Python objects instead of raw SQL strings
    - Relationships — one-to-many with relationship() and ForeignKey
    - A quick look at database migrations (why they matter, Alembic in one paragraph)

Prerequisites:
    - Day 10-11 (OOP I & II) — classes, __init__, inheritance
    - day25_01_sqlite_basics.py — raw SQL concepts this file builds on

How to run:
    python day25_02_sqlalchemy_orm.py

Install SQLAlchemy first if you haven't already:
    uv add sqlalchemy
    (or) pip install sqlalchemy --break-system-packages
"""

import os
from sqlalchemy import create_engine, ForeignKey, String, Float, Integer
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship, Session
)

# ════════════════════════════════════════════════════════════════
# SECTION 1: Why an ORM? Declarative Models
# ════════════════════════════════════════════════════════════════
#
# In File 1 you wrote raw SQL strings: "INSERT INTO customers VALUES (?,?)".
# That works, but it means your database schema lives in string literals
# scattered across your code, with no help from your editor or type checker.
#
# An ORM (Object-Relational Mapper) lets you define your schema as Python
# classes instead. SQLAlchemy then translates operations on those classes
# into the SQL your database actually needs. You get autocomplete, type
# checking, and the ability to swap databases (SQLite -> PostgreSQL) with
# very few code changes.

DB_FILE = "bookstore.db"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)


class Base(DeclarativeBase):
    """Every model class inherits from this shared declarative base.
    SQLAlchemy uses it to collect metadata about all your tables."""
    pass


# ── Defining a Model (maps to a "authors" table) ──
# Mapped[type] + mapped_column() is the modern (2.0-style) way to declare
# columns. It reads naturally and plugs into type checkers like mypy.
class Author(Base):
    __tablename__ = "authors"

    author_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50))

    # ── One-to-Many Relationship ──
    # An author can have many books. `relationship()` doesn't create a
    # column — it tells the ORM how to fetch related rows automatically.
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def __repr__(self):
        return f"Author(id={self.author_id}, name={self.name!r}, city={self.city!r})"


class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    price_rupees: Mapped[float] = mapped_column(Float, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.author_id"))

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"Book(id={self.book_id}, title={self.title!r}, price={self.price_rupees})"


print("Models defined: Author, Book (with a one-to-many relationship).")
# Output:
# Models defined: Author, Book (with a one-to-many relationship).

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2: Engine, Table Creation, and Sessions
# ════════════════════════════════════════════════════════════════
#
# The "engine" is SQLAlchemy's connection to the actual database file.
# echo=False keeps the demo output clean; set echo=True while debugging to
# see every SQL statement SQLAlchemy generates under the hood.
engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)

# create_all() reads every Base subclass and issues CREATE TABLE for each
# one that doesn't already exist — similar to what we did by hand in File 1.
Base.metadata.create_all(engine)
print("Tables created from models: authors, books")
# Output:
# Tables created from models: authors, books

# ── What is a Session? ──
# A Session is the ORM's "workspace" — you add/modify Python objects in
# it, and session.commit() translates those changes into SQL and writes
# them to the database in one transaction. Think of it as a shopping cart
# for database changes.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3: CRUD — Create
# ════════════════════════════════════════════════════════════════

with Session(engine) as session:
    # ── Creating objects just like any other Python class ──
    author1 = Author(name="Ruskin Bond", city="Landour")
    author2 = Author(name="Chetan Bhagat", city="New Delhi")

    # Adding related Book objects directly through the relationship list —
    # SQLAlchemy figures out the foreign key automatically.
    author1.books.append(Book(title="The Blue Umbrella", price_rupees=199.0))
    author1.books.append(Book(title="Rusty the Mountain Boy", price_rupees=249.0))
    author2.books.append(Book(title="Five Point Someone", price_rupees=299.0))

    session.add_all([author1, author2])
    session.commit()
    print(f"Inserted authors with ids: {author1.author_id}, {author2.author_id}")
# Output:
# Inserted authors with ids: 1, 2

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 4: CRUD — Read
# ════════════════════════════════════════════════════════════════

from sqlalchemy import select

with Session(engine) as session:
    # ── select() replaces raw "SELECT * FROM ..." strings ──
    stmt = select(Author)
    all_authors = session.scalars(stmt).all()
    print("All authors:")
    for author in all_authors:
        print(f"  {author}")
    # Output:
    # All authors:
    #   Author(id=1, name='Ruskin Bond', city='Landour')
    #   Author(id=2, name='Chetan Bhagat', city='New Delhi')

    # ── Filtering with .where() ──
    stmt = select(Book).where(Book.price_rupees > 200)
    pricier_books = session.scalars(stmt).all()
    print("Books over Rs. 200:")
    for book in pricier_books:
        print(f"  {book}")
    # Output:
    # Books over Rs. 200:
    #   Book(id=2, title='Rusty the Mountain Boy', price=249.0)
    #   Book(id=3, title='Five Point Someone', price=299.0)

    # ── Accessing a relationship automatically fetches related rows ──
    ruskin = session.scalars(select(Author).where(Author.name == "Ruskin Bond")).first()
    print(f"{ruskin.name}'s books: {[b.title for b in ruskin.books]}")
    # Output:
    # Ruskin Bond's books: ['The Blue Umbrella', 'Rusty the Mountain Boy']

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 5: CRUD — Update and Delete
# ════════════════════════════════════════════════════════════════

with Session(engine) as session:
    # ── Update: fetch the object, change an attribute, commit ──
    book = session.scalars(select(Book).where(Book.title == "Five Point Someone")).first()
    book.price_rupees = 279.0
    session.commit()
    print(f"Updated price: {book}")
    # Output:
    # Updated price: Book(id=3, title='Five Point Someone', price=279.0)

    # ── Delete: fetch the object, session.delete(), commit ──
    umbrella = session.scalars(select(Book).where(Book.title == "The Blue Umbrella")).first()
    session.delete(umbrella)
    session.commit()
    remaining = session.scalars(select(Book)).all()
    print(f"Remaining books: {[b.title for b in remaining]}")
    # Output:
    # Remaining books: ['Rusty the Mountain Boy', 'Five Point Someone']

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 6: Guided Examples
# ════════════════════════════════════════════════════════════════

# ── Example 1: Adding several books for a new author in one go ──
with Session(engine) as session:
    new_author = Author(name="Sudha Murty", city="Bengaluru")
    new_author.books = [
        Book(title="Wise and Otherwise", price_rupees=180.0),
        Book(title="The Old Man and His God", price_rupees=210.0),
        Book(title="Grandma's Bag of Stories", price_rupees=160.0),
    ]
    session.add(new_author)
    session.commit()
    print(f"Example 1: Added {new_author.name} with {len(new_author.books)} books.")
# Output:
# Example 1: Added Sudha Murty with 3 books.

# ── Example 2: Aggregation — total catalog value with func.sum() ──
from sqlalchemy import func

with Session(engine) as session:
    total_value = session.scalar(select(func.sum(Book.price_rupees)))
    print(f"Example 2: Total catalog value: Rs. {total_value}")
# Output:
# Example 2: Total catalog value: Rs. 1078.0

# ── Example 3: Counting books per author with GROUP BY ──
with Session(engine) as session:
    stmt = (
        select(Author.name, func.count(Book.book_id))
        .join(Book, Book.author_id == Author.author_id)
        .group_by(Author.name)
    )
    print("Example 3: Book count per author")
    for name, book_count in session.execute(stmt):
        print(f"  {name}: {book_count} book(s)")
# Output:
# Example 3: Book count per author
#   Ruskin Bond: 1 book(s)
#   Chetan Bhagat: 1 book(s)
#   Sudha Murty: 3 book(s)

# ── Example 4: Ordering results — cheapest books first ──
with Session(engine) as session:
    stmt = select(Book).order_by(Book.price_rupees.asc()).limit(3)
    cheapest = session.scalars(stmt).all()
    print("Example 4: 3 cheapest books")
    for b in cheapest:
        print(f"  {b.title}: Rs. {b.price_rupees}")
# Output:
# Example 4: 3 cheapest books
#   Grandma's Bag of Stories: Rs. 160.0
#   Wise and Otherwise: Rs. 180.0
#   The Old Man and His God: Rs. 210.0

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 7: A Word on Migrations
# ════════════════════════════════════════════════════════════════
#
# Base.metadata.create_all() only creates tables that don't exist yet — it
# will NOT alter an existing table if you add a new column to a model
# later. In real projects, schema changes are managed with a migration
# tool such as Alembic, which generates versioned scripts (e.g.
# "add is_bestseller column to books") that can be applied and rolled back
# in order, on any environment (your laptop, staging, production) so the
# database schema always matches what your models expect. For this course,
# knowing create_all() is enough — Alembic is a natural next tool to learn
# once you're comfortable with the ORM basics above.

print("Migrations note: create_all() only adds NEW tables, never alters existing ones.")
# Output:
# Migrations note: create_all() only adds NEW tables, never alters existing ones.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Write a function `authors_with_expensive_books(engine, threshold)` that
# returns a sorted list of unique author names who have at least one book
# priced ABOVE the given threshold. Use a JOIN + DISTINCT-style approach
# (hint: a Python set() works fine here too).
#
# Expected output when called with threshold=200:
#   ['Chetan Bhagat', 'Ruskin Bond', 'Sudha Murty']

# YOUR CODE HERE


# ── Solution (uncomment to check your work) ──
# def authors_with_expensive_books(engine, threshold):
#     with Session(engine) as session:
#         stmt = (
#             select(Author.name)
#             .join(Book, Book.author_id == Author.author_id)
#             .where(Book.price_rupees > threshold)
#             .distinct()
#         )
#         names = session.scalars(stmt).all()
#         return sorted(names)
#
# result = authors_with_expensive_books(engine, 200)
# print(result)
# Expected output:
# ['Chetan Bhagat', 'Ruskin Bond', 'Sudha Murty']


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Declaring models with DeclarativeBase, Mapped, and mapped_column()
#   - create_engine() and Base.metadata.create_all() to build the schema
#   - Session as a "unit of work" — add(), commit(), scalars(), select()
#   - relationship() + ForeignKey for one-to-many links between tables
#   - CRUD entirely through Python objects, no raw SQL strings
#   - func.sum(), func.count(), join(), group_by(), order_by(), limit()
#   - Why real projects use a migration tool like Alembic
#
# Next up: day25_03_packaging_docker.py — turning your Python project into
# an installable package and a Docker container.

if __name__ == "__main__":
    print("Day 25, File 2 complete: SQLAlchemy ORM demonstrated end-to-end.")
