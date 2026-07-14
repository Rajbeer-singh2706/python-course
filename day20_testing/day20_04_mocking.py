"""
Day 20 — Testing (Part 4: Mocking with unittest.mock)
========================================================

WHAT THIS FILE COVERS:
    - Why we "mock" external dependencies (APIs, databases, payment gateways)
    - Mock and MagicMock objects
    - Setting return values and side effects on a mock
    - patch() — temporarily replacing a real object with a mock during a test
    - Asserting a mock was called (assert_called_with, call_count, etc.)
    - Using pytest's `monkeypatch` fixture as a lightweight alternative

PREREQUISITES:
    - day20_03_fixtures.py (same day, previous file)
    - Day 23 concepts are previewed lightly here (requests library),
      but full API coverage comes in Day 23.

HOW TO RUN:
    pytest day20_04_mocking.py -v
"""

import sys
from unittest.mock import Mock, MagicMock, patch

import pytest


# ════════════════════════════════════════════════════════════
# SECTION 1: Why Do We Mock Things?
# ════════════════════════════════════════════════════════════
#
# Arjun Mehta is building a function that calls the Razorpay payment
# API to charge a customer. He wants to test his OWN logic — like
# "if the payment fails, mark the order as failed" — WITHOUT actually
# hitting Razorpay's real servers every time he runs his tests.
#
# A "mock" is a fake stand-in object that pretends to be the real
# thing. You control exactly what it returns, and you can check
# afterward exactly how it was used.


# ════════════════════════════════════════════════════════════
# SECTION 2: Mock and MagicMock Basics
# ════════════════════════════════════════════════════════════

def test_basic_mock_object():
    # A Mock object will happily accept ANY attribute or method call.
    fake_gateway = Mock()
    fake_gateway.charge(amount=500)  # doesn't error, even though charge() isn't "real"

    # We can check that the call actually happened:
    fake_gateway.charge.assert_called_once_with(amount=500)


def test_mock_return_value():
    fake_gateway = Mock()
    # Configure exactly what calling `.charge()` should return:
    fake_gateway.charge.return_value = {"status": "success", "transaction_id": "TXN123"}

    result = fake_gateway.charge(amount=999)
    assert result["status"] == "success"
    assert result["transaction_id"] == "TXN123"


def test_magicmock_supports_dunder_methods():
    # MagicMock additionally supports "magic methods" like __len__, __iter__
    fake_cart = MagicMock()
    fake_cart.__len__.return_value = 3
    assert len(fake_cart) == 3


# ════════════════════════════════════════════════════════════
# SECTION 3: Side Effects — Simulating Errors or Sequences
# ════════════════════════════════════════════════════════════

def test_mock_side_effect_raises_exception():
    fake_gateway = Mock()
    fake_gateway.charge.side_effect = ConnectionError("Razorpay servers unreachable")

    with pytest.raises(ConnectionError):
        fake_gateway.charge(amount=500)


def test_mock_side_effect_sequence():
    # side_effect can be a list — each call returns the NEXT value
    fake_sensor = Mock()
    fake_sensor.read_temperature.side_effect = [28.5, 29.0, 29.5]

    readings = [fake_sensor.read_temperature() for _ in range(3)]
    assert readings == [28.5, 29.0, 29.5]


# ════════════════════════════════════════════════════════════
# SECTION 4: patch() — Replacing Real Objects During a Test
# ════════════════════════════════════════════════════════════
#
# The REAL power of mocking is `patch()`: it temporarily replaces a
# real function/class (often one that hits a network or a database)
# with a Mock, for the DURATION of the test only.


def fetch_delivery_estimate(pincode: str) -> str:
    """
    In production this would call a real logistics API (e.g. Delhivery).
    For teaching purposes we simulate the "real" external call with
    a module-level function so we have something to patch().
    """
    return _call_external_logistics_api(pincode)


def _call_external_logistics_api(pincode: str) -> str:
    # Imagine this makes a slow, real network request in production.
    raise RuntimeError("This should never actually run in tests!")


def test_fetch_delivery_estimate_with_patch():
    # patch() targets the NAME as it is looked up in THIS module.
    with patch(f"{__name__}._call_external_logistics_api") as mock_api:
        mock_api.return_value = "2-3 business days"

        result = fetch_delivery_estimate("411045")

        assert result == "2-3 business days"
        mock_api.assert_called_once_with("411045")


# patch() can also be used as a DECORATOR instead of a `with` block:
@patch(f"{__name__}._call_external_logistics_api")
def test_fetch_delivery_estimate_with_decorator(mock_api):
    mock_api.return_value = "Same day delivery"
    result = fetch_delivery_estimate("560001")
    assert result == "Same day delivery"


# ════════════════════════════════════════════════════════════
# SECTION 5: Mocking a Class Method (e.g. a Database Layer)
# ════════════════════════════════════════════════════════════

class OrderRepository:
    """Pretend this talks to a real Postgres/SQLite database."""

    def save(self, order: dict) -> int:
        raise NotImplementedError("Real DB write — never call this in tests!")

    def find_by_id(self, order_id: int) -> dict:
        raise NotImplementedError("Real DB read — never call this in tests!")


class OrderService:
    """The class we actually want to test — its LOGIC, not the DB."""

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def place_order(self, customer: str, amount: float) -> dict:
        if amount <= 0:
            raise ValueError("Order amount must be positive")
        order = {"customer": customer, "amount": amount, "status": "placed"}
        order_id = self.repository.save(order)
        return {"order_id": order_id, **order}


def test_order_service_uses_repository():
    # We create a Mock STANDING IN for the real repository entirely —
    # no need to patch anything since we control object creation.
    mock_repo = Mock(spec=OrderRepository)
    mock_repo.save.return_value = 42

    service = OrderService(repository=mock_repo)
    result = service.place_order(customer="Priya Sharma", amount=1250.0)

    assert result["order_id"] == 42
    assert result["status"] == "placed"
    mock_repo.save.assert_called_once()


def test_order_service_rejects_invalid_amount():
    mock_repo = Mock(spec=OrderRepository)
    service = OrderService(repository=mock_repo)

    with pytest.raises(ValueError):
        service.place_order(customer="Sanjay Verma", amount=-100)

    # Crucially: the repository should NEVER have been called
    mock_repo.save.assert_not_called()


# ════════════════════════════════════════════════════════════
# SECTION 6: `spec=` — Guarding Against Typos in Mocks
# ════════════════════════════════════════════════════════════
#
# Without `spec=`, a Mock will accept ANY attribute name, even typos.
# Passing `spec=SomeClass` restricts the mock to only the real class's
# attributes, so a typo raises an AttributeError immediately.


def test_mock_spec_catches_typo():
    mock_repo = Mock(spec=OrderRepository)
    with pytest.raises(AttributeError):
        mock_repo.saev({"typo": "in method name"})  # not a real method name


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE: pytest's Built-in monkeypatch Fixture
# ════════════════════════════════════════════════════════════
#
# pytest ships a lighter-weight alternative to unittest.mock.patch
# called `monkeypatch` — a fixture you can request directly.

import os


def get_environment_name() -> str:
    return os.environ.get("APP_ENV", "development")


def test_get_environment_name_with_monkeypatch(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    assert get_environment_name() == "production"


def test_get_environment_name_default(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    assert get_environment_name() == "development"


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Write a function `send_otp(mobile: str, sms_client) -> bool` that:
#   - calls sms_client.send(mobile, message) with some OTP message
#   - returns True if sms_client.send() returns {"status": "sent"}
#   - returns False otherwise
#
# Then write 2 tests using a Mock for sms_client:
#   1. sms_client.send returns {"status": "sent"} -> send_otp returns True
#   2. sms_client.send returns {"status": "failed"} -> send_otp returns False
#
# YOUR CODE HERE


# ---- SOLUTION ----
# def send_otp(mobile: str, sms_client) -> bool:
#     response = sms_client.send(mobile, "Your OTP is 4821")
#     return response.get("status") == "sent"
#
#
# def test_send_otp_success():
#     mock_sms = Mock()
#     mock_sms.send.return_value = {"status": "sent"}
#     assert send_otp("9876543210", mock_sms) is True
#
#
# def test_send_otp_failure():
#     mock_sms = Mock()
#     mock_sms.send.return_value = {"status": "failed"}
#     assert send_otp("9876543210", mock_sms) is False
# Expected: both tests pass


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Mock / MagicMock objects and return_value / side_effect
#   - patch() as a context manager and as a decorator
#   - Injecting mocks via constructor parameters (dependency injection)
#   - spec= to catch typos in mocked attributes
#   - pytest's built-in monkeypatch fixture
#
# NEXT FILE: day20_05_coverage_tdd.py
#   -> Coverage reports with pytest-cov, and an introduction to
#      Test-Driven Development (TDD): red -> green -> refactor.

if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
