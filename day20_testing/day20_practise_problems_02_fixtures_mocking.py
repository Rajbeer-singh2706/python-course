"""
Day 20 — Practice Problems (Part 2 of 3)
===========================================
Topic: Testing — pytest Fixtures & Mocking

CUMULATIVE SCOPE: Builds on day20_practise_problems_01, plus Day 10-11
(OOP), Day 12 (modules), and Day 20 fixture/mocking concepts.

DIFFICULTY LEGEND:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines 2+ ideas, requires some thought
    🔴 Challenge — multi-step, real-world style problem

SECTION INDEX (this file):
    Section C — pytest Fixtures    (5 problems)
    Section D — Mocking            (5 problems)

HOW TO RUN:
    pytest day20_practise_problems_02_fixtures_mocking.py -v
"""

import pytest
from unittest.mock import Mock, patch


# ════════════════════════════════════════════════════════════
# SECTION C — pytest Fixtures
# ════════════════════════════════════════════════════════════

# ── Problem C1 ──
# 🟢 Warm-up
# Write a fixture `sample_student` that returns a dict:
#   {"name": "Priya Sharma", "marks": [88, 92, 79]}
# Then write a test using the fixture that checks the average of
# `marks` is greater than 80.

# YOUR CODE HERE


# ---- SOLUTION ----
# @pytest.fixture
# def sample_student():
#     return {"name": "Priya Sharma", "marks": [88, 92, 79]}
#
# def test_student_average_above_80(sample_student):
#     average = sum(sample_student["marks"]) / len(sample_student["marks"])
#     assert average > 80
# Expected: test passes (average is ~86.3)
print("-" * 50)


# ── Problem C2 ──
# 🟢 Warm-up
# Write a fixture `empty_list` that returns an empty Python list.
# Then write 2 tests: one checking the list is empty at the start,
# and another (independent) test that appends an item and checks the
# length is 1 — proving each test gets a FRESH list (default scope).

# YOUR CODE HERE


# ---- SOLUTION ----
# @pytest.fixture
# def empty_list():
#     return []
#
# def test_list_starts_empty(empty_list):
#     assert len(empty_list) == 0
#
# def test_list_after_append(empty_list):
#     empty_list.append("Bengaluru")
#     assert len(empty_list) == 1
# Expected: both tests pass independently (no shared state)
print("-" * 50)


# ── Problem C3 ──
# 🟡 Core
# Write a class `Playlist` with `songs: list[str]` and methods
# `add_song(name)` and `remove_song(name)`. Write a fixture
# `sample_playlist` that returns a Playlist pre-loaded with 3 songs.
# Write tests for: adding a song increases the count, removing an
# existing song decreases the count, removing a non-existent song
# raises a ValueError.

# YOUR CODE HERE


# ---- SOLUTION ----
# class Playlist:
#     def __init__(self, songs=None):
#         self.songs = songs if songs is not None else []
#
#     def add_song(self, name):
#         self.songs.append(name)
#
#     def remove_song(self, name):
#         if name not in self.songs:
#             raise ValueError(f"{name} not in playlist")
#         self.songs.remove(name)
#
# @pytest.fixture
# def sample_playlist():
#     return Playlist(songs=["Kesariya", "Tum Hi Ho", "Zinda"])
#
# def test_add_song_increases_count(sample_playlist):
#     sample_playlist.add_song("Chaiyya Chaiyya")
#     assert len(sample_playlist.songs) == 4
#
# def test_remove_existing_song(sample_playlist):
#     sample_playlist.remove_song("Tum Hi Ho")
#     assert len(sample_playlist.songs) == 2
#
# def test_remove_nonexistent_song_raises(sample_playlist):
#     with pytest.raises(ValueError):
#         sample_playlist.remove_song("Not A Real Song")
# Expected: all 3 tests pass
print("-" * 50)


# ── Problem C4 ──
# 🟡 Core
# Write a yield-based fixture `temp_counter` that: prints "start" before
# yielding a dict {"count": 0}, and prints "end" after the test finishes.
# Write a test that increments the counter's "count" key twice and
# asserts it equals 2.

# YOUR CODE HERE


# ---- SOLUTION ----
# @pytest.fixture
# def temp_counter():
#     print("\nstart")
#     counter = {"count": 0}
#     yield counter
#     print("end")
#
# def test_counter_increment_twice(temp_counter):
#     temp_counter["count"] += 1
#     temp_counter["count"] += 1
#     assert temp_counter["count"] == 2
# Expected: test passes; "start" prints before, "end" prints after
# (visible with `pytest -s`)
print("-" * 50)


# ── Problem C5 ──
# 🔴 Challenge
# Write a fixture `base_menu` returning
#   {"Dosa": 60, "Idli": 40, "Vada": 30}
# and a SECOND fixture `discounted_menu(base_menu)` that depends on the
# first, applying a flat 10% discount to every item's price (round to
# 2 decimals). Write a test using `discounted_menu` that checks Dosa's
# discounted price is 54.0.

# YOUR CODE HERE


# ---- SOLUTION ----
# @pytest.fixture
# def base_menu():
#     return {"Dosa": 60, "Idli": 40, "Vada": 30}
#
# @pytest.fixture
# def discounted_menu(base_menu):
#     return {item: round(price * 0.9, 2) for item, price in base_menu.items()}
#
# def test_discounted_dosa_price(discounted_menu):
#     assert discounted_menu["Dosa"] == 54.0
# Expected: test passes
print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION D — Mocking
# ════════════════════════════════════════════════════════════

# ── Problem D1 ──
# 🟢 Warm-up
# Create a Mock object called `fake_printer`. Call `fake_printer.print_receipt(total=250)`.
# Then write an assertion checking it was called exactly once with total=250.

# YOUR CODE HERE


# ---- SOLUTION ----
# def test_fake_printer_called_correctly():
#     fake_printer = Mock()
#     fake_printer.print_receipt(total=250)
#     fake_printer.print_receipt.assert_called_once_with(total=250)
# Expected: test passes
print("-" * 50)


# ── Problem D2 ──
# 🟢 Warm-up
# Create a Mock object `fake_weather_api` and set its `.get_temperature`
# return_value to 32.5. Write a test asserting that calling
# `fake_weather_api.get_temperature("Chennai")` returns 32.5.

# YOUR CODE HERE


# ---- SOLUTION ----
# def test_fake_weather_api_returns_configured_value():
#     fake_weather_api = Mock()
#     fake_weather_api.get_temperature.return_value = 32.5
#     assert fake_weather_api.get_temperature("Chennai") == 32.5
# Expected: test passes
print("-" * 50)


# ── Problem D3 ──
# 🟡 Core
# Write a function `get_wallet_balance(user_id: str, wallet_client) -> float`
# that calls `wallet_client.fetch_balance(user_id)` and returns the
# result. Write 2 tests using a Mock for wallet_client: one where
# fetch_balance returns 500.0, and one where it raises a
# ConnectionError (use pytest.raises to confirm it propagates).

# YOUR CODE HERE


# ---- SOLUTION ----
# def get_wallet_balance(user_id, wallet_client):
#     return wallet_client.fetch_balance(user_id)
#
# def test_get_wallet_balance_success():
#     mock_client = Mock()
#     mock_client.fetch_balance.return_value = 500.0
#     assert get_wallet_balance("user_42", mock_client) == 500.0
#
# def test_get_wallet_balance_connection_error():
#     mock_client = Mock()
#     mock_client.fetch_balance.side_effect = ConnectionError("Paytm API down")
#     with pytest.raises(ConnectionError):
#         get_wallet_balance("user_42", mock_client)
# Expected: both tests pass
print("-" * 50)


# ── Problem D4 ──
# 🟡 Core
# There's a module-level function `_send_email(to, subject, body)` that
# would normally hit a real email server. Write a function
# `notify_order_shipped(to: str, order_id: int) -> bool` that calls
# `_send_email` and returns True if it doesn't raise. Use `patch()` to
# replace `_send_email` in a test and assert it was called with the
# right `to` address.

# YOUR CODE HERE


# ---- SOLUTION ----
# def _send_email(to, subject, body):
#     raise RuntimeError("Would hit a real email server in production!")
#
# def notify_order_shipped(to, order_id):
#     _send_email(to, f"Order #{order_id} Shipped", "Your order is on its way!")
#     return True
#
# def test_notify_order_shipped():
#     with patch(f"{__name__}._send_email") as mock_send:
#         result = notify_order_shipped("riya@example.com", 1042)
#         assert result is True
#         mock_send.assert_called_once()
#         args, kwargs = mock_send.call_args
#         assert args[0] == "riya@example.com"
# Expected: test passes
print("-" * 50)


# ── Problem D5 ──
# 🔴 Challenge
# Write a class `NotificationService` with a constructor that takes an
# `sms_client`. Add a method `remind_payment_due(mobile: str, amount: float) -> bool`
# that calls `sms_client.send(mobile, message)` and returns True only if
# the response dict's "status" key equals "delivered". Write tests using
# `Mock(spec=...)`-style mocks for: successful delivery, failed delivery,
# and a case where `sms_client.send` raises a TimeoutError (test should
# assert the exception propagates, using pytest.raises).

# YOUR CODE HERE


# ---- SOLUTION ----
# class SmsClient:
#     def send(self, mobile, message):
#         raise NotImplementedError("Real SMS gateway — never call in tests!")
#
# class NotificationService:
#     def __init__(self, sms_client):
#         self.sms_client = sms_client
#
#     def remind_payment_due(self, mobile, amount):
#         response = self.sms_client.send(mobile, f"Payment of Rs.{amount} is due")
#         return response.get("status") == "delivered"
#
# def test_remind_payment_due_success():
#     mock_sms = Mock(spec=SmsClient)
#     mock_sms.send.return_value = {"status": "delivered"}
#     service = NotificationService(mock_sms)
#     assert service.remind_payment_due("9123456780", 499.0) is True
#
# def test_remind_payment_due_failure():
#     mock_sms = Mock(spec=SmsClient)
#     mock_sms.send.return_value = {"status": "failed"}
#     service = NotificationService(mock_sms)
#     assert service.remind_payment_due("9123456780", 499.0) is False
#
# def test_remind_payment_due_timeout_propagates():
#     mock_sms = Mock(spec=SmsClient)
#     mock_sms.send.side_effect = TimeoutError("SMS gateway timed out")
#     service = NotificationService(mock_sms)
#     with pytest.raises(TimeoutError):
#         service.remind_payment_due("9123456780", 499.0)
# Expected: all 3 tests pass
print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# SECTIONS IN THIS FILE:
#   C — pytest Fixtures    (5 problems)
#   D — Mocking            (5 problems)
#
# DIFFICULTY BREAKDOWN: 4x 🟢 Warm-up | 4x 🟡 Core | 2x 🔴 Challenge
#
# NEXT FILE: day20_practise_problems_03_mixed_challenges.py
#   -> Section E: Mixed Challenges combining all of Day 20 + prior days

if __name__ == "__main__":
    print("All solutions are commented out above.")
    print("Uncomment a solution block and run with `pytest <this file> -v` to try it.")
