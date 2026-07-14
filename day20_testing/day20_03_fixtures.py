"""
Day 20 — Testing (Part 3: pytest Fixtures)
=============================================

WHAT THIS FILE COVERS:
    - What a fixture is and why it beats manual setUp/tearDown
    - Writing a fixture with @pytest.fixture
    - Injecting fixtures into test functions (dependency injection)
    - Fixture scopes: function, class, module, session
    - Fixtures that yield (setup + teardown in one function)
    - Using multiple fixtures together

PREREQUISITES:
    - day20_02_pytest_basics.py (same day, previous file)

HOW TO RUN:
    pytest day20_03_fixtures.py -v
"""

import sys
import pytest


# ════════════════════════════════════════════════════════════
# SECTION 1: What Problem Do Fixtures Solve?
# ════════════════════════════════════════════════════════════
#
# Meera Iyer is testing a `BankAccount` class. Nearly every test needs
# a fresh BankAccount to start from. Instead of repeating the same
# setup code in every test function, we write ONE fixture function
# and pytest "injects" it into any test that asks for it by name.


class BankAccount:
    """A simple bank account (used throughout this file's examples)."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transaction_log: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        self.transaction_log.append(f"Deposited ₹{amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.transaction_log.append(f"Withdrew ₹{amount}")


# ════════════════════════════════════════════════════════════
# SECTION 2: A Basic Fixture
# ════════════════════════════════════════════════════════════
#
# @pytest.fixture marks a function as a fixture. Any test function
# that names a PARAMETER matching the fixture's name automatically
# receives its return value.


@pytest.fixture
def fresh_account():
    """Provide a brand-new BankAccount for Meera Iyer, with ₹1000 balance."""
    return BankAccount(owner="Meera Iyer", balance=1000.0)


def test_initial_balance(fresh_account):
    # pytest sees the `fresh_account` parameter name and matches it
    # to the fixture function above — no import, no manual call needed.
    assert fresh_account.balance == 1000.0


def test_deposit_increases_balance(fresh_account):
    fresh_account.deposit(500)
    assert fresh_account.balance == 1500.0


def test_withdraw_decreases_balance(fresh_account):
    fresh_account.withdraw(300)
    assert fresh_account.balance == 700.0


def test_withdraw_more_than_balance_raises(fresh_account):
    with pytest.raises(ValueError):
        fresh_account.withdraw(5000)


# NOTE: Every test above gets its OWN fresh_account — pytest calls the
# fixture function again for each test (default scope="function"),
# so tests never accidentally share state.


# ════════════════════════════════════════════════════════════
# SECTION 3: Fixtures That Yield — Setup AND Teardown
# ════════════════════════════════════════════════════════════
#
# Using `yield` instead of `return` lets a fixture run cleanup code
# AFTER the test finishes — similar to tearDown in unittest.


@pytest.fixture
def logged_account():
    """A fixture demonstrating setup + teardown in one function."""
    print("\n[SETUP] Opening account for Sanjay Verma...")
    account = BankAccount(owner="Sanjay Verma", balance=2000.0)
    yield account  # <-- test code runs here, using `account`
    print("[TEARDOWN] Closing account, final log:", account.transaction_log)


def test_logged_account_deposit(logged_account):
    logged_account.deposit(100)
    assert logged_account.balance == 2100.0
    assert "Deposited ₹100" in logged_account.transaction_log


# ════════════════════════════════════════════════════════════
# SECTION 4: Fixture Scopes
# ════════════════════════════════════════════════════════════
#
#   scope="function"  (default) -> runs once PER TEST FUNCTION
#   scope="class"                -> runs once per test CLASS
#   scope="module"                -> runs once per FILE
#   scope="session"                -> runs once for the ENTIRE test run
#
# Use broader scopes for EXPENSIVE setup (e.g. a database connection)
# that many tests can safely share.


@pytest.fixture(scope="module")
def mock_database_connection():
    """Simulates an expensive DB connection, shared by all tests in this file."""
    print("\n[MODULE FIXTURE] Connecting to mock SQLite test database (once)...")
    connection = {"status": "connected", "db_name": "test_bank.db"}
    yield connection
    print("[MODULE FIXTURE] Disconnecting from mock database (once)...")


def test_db_connection_status(mock_database_connection):
    assert mock_database_connection["status"] == "connected"


def test_db_connection_name(mock_database_connection):
    assert mock_database_connection["db_name"] == "test_bank.db"


# ════════════════════════════════════════════════════════════
# SECTION 5: Using Multiple Fixtures in One Test
# ════════════════════════════════════════════════════════════


@pytest.fixture
def second_account():
    """A second account, for tests that need TWO accounts (e.g. transfers)."""
    return BankAccount(owner="Priya Sharma", balance=500.0)


def transfer(sender: BankAccount, receiver: BankAccount, amount: float) -> None:
    sender.withdraw(amount)
    receiver.deposit(amount)


def test_transfer_between_accounts(fresh_account, second_account):
    # Both fixtures are injected by simply naming them as parameters.
    transfer(sender=fresh_account, receiver=second_account, amount=200)
    assert fresh_account.balance == 800.0
    assert second_account.balance == 700.0


# ════════════════════════════════════════════════════════════
# SECTION 6: A Fixture Built From Another Fixture
# ════════════════════════════════════════════════════════════
#
# Fixtures can depend on OTHER fixtures — pytest resolves the chain
# automatically.


@pytest.fixture
def account_with_history(fresh_account):
    """Takes the fresh_account fixture and adds some transaction history."""
    fresh_account.deposit(200)
    fresh_account.withdraw(50)
    return fresh_account


def test_account_with_history_balance(account_with_history):
    assert account_with_history.balance == 1150.0


def test_account_with_history_log_length(account_with_history):
    assert len(account_with_history.transaction_log) == 2


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE: Ola/Uber-style Ride Fixture
# ════════════════════════════════════════════════════════════

class Ride:
    def __init__(self, rider: str, distance_km: float):
        self.rider = rider
        self.distance_km = distance_km
        self.fare = round(distance_km * 12.5 + 25, 2)  # ₹12.5/km + ₹25 base fare
        self.status = "requested"

    def start(self):
        self.status = "in_progress"

    def complete(self):
        self.status = "completed"


@pytest.fixture
def sample_ride():
    """A requested ride for Riya Deshmukh, 8.4 km."""
    return Ride(rider="Riya Deshmukh", distance_km=8.4)


def test_ride_fare_calculation(sample_ride):
    assert sample_ride.fare == 130.0


def test_ride_starts_as_requested(sample_ride):
    assert sample_ride.status == "requested"


def test_ride_lifecycle(sample_ride):
    sample_ride.start()
    assert sample_ride.status == "in_progress"
    sample_ride.complete()
    assert sample_ride.status == "completed"


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Write a fixture called `sample_playlist` that returns a dict like:
#   {"name": "Road Trip Mix", "songs": ["Song A", "Song B", "Song C"]}
#
# Then write 2 tests using that fixture:
#   1. test that the playlist has exactly 3 songs
#   2. test that "Song B" is in the playlist
#
# YOUR CODE HERE


# ---- SOLUTION ----
# @pytest.fixture
# def sample_playlist():
#     return {"name": "Road Trip Mix", "songs": ["Song A", "Song B", "Song C"]}
#
#
# def test_playlist_song_count(sample_playlist):
#     assert len(sample_playlist["songs"]) == 3
#
#
# def test_playlist_contains_song_b(sample_playlist):
#     assert "Song B" in sample_playlist["songs"]
# Expected: both tests pass


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - @pytest.fixture and dependency injection via parameter names
#   - yield-based fixtures for setup + teardown
#   - Fixture scopes: function, class, module, session
#   - Fixtures depending on other fixtures
#   - Using multiple fixtures in a single test
#
# NEXT FILE: day20_04_mocking.py
#   -> unittest.mock: Mock objects, patch(), and testing code that
#      talks to external services (APIs, databases, payment gateways).

if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
