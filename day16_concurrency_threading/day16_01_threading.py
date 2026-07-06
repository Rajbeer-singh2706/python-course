"""
Day 16 - Concurrency Basics
File 1 of 3: The `threading` Module

Covers:
    - Why concurrency matters (I/O-bound vs CPU-bound work)
    - Creating and starting threads with `threading.Thread`
    - `join()` - waiting for a thread to finish
    - Race conditions and why they happen
    - `threading.Lock` - protecting shared state
    - `concurrent.futures.ThreadPoolExecutor` - a higher-level API

Prerequisites:
    - Day 9 (Error Handling)
    - Day 12 (Modules & Packages)

How to run:
    python day16_01_threading.py
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# ════════════════════════════════════════════════════════════════
# SECTION 1: Why Concurrency? I/O-Bound vs CPU-Bound
# ════════════════════════════════════════════════════════════════
# Concurrency lets a program make progress on multiple tasks "at once".
# Two broad categories of work:
#   - I/O-BOUND: waiting on network requests, file reads, database
#     queries (e.g. fetching data from Swiggy's API). The CPU is idle
#     while waiting - threading shines here.
#   - CPU-BOUND: heavy computation (e.g. crunching numbers, image
#     processing). Python's Global Interpreter Lock (GIL) means
#     threads don't truly run Python bytecode in parallel for this -
#     multiprocessing (File 2) is the better tool for CPU-bound work.
#
# threading.Thread is ideal for I/O-bound tasks like downloading
# multiple files or calling multiple APIs at once.

print("Concept: threading is best for I/O-bound tasks (waiting on")
print("network calls, file reads); use multiprocessing for CPU-bound work.")

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2: Creating and Starting a Thread
# ════════════════════════════════════════════════════════════════
# `threading.Thread(target=function, args=(...))` creates a thread.
# `.start()` begins execution; `.join()` blocks the main program
# until that thread finishes.

def download_menu(restaurant_name, delay_seconds):
    """Simulates downloading a restaurant's menu (an I/O-bound task)."""
    time.sleep(delay_seconds)   # simulates network wait, not actual I/O
    print(f"Downloaded menu for {restaurant_name}")


# Create two threads, each simulating a Swiggy API call
thread_1 = threading.Thread(target=download_menu, args=("Punjabi Dhaba", 0.2))
thread_2 = threading.Thread(target=download_menu, args=("South Indian Tiffin", 0.1))

start_time = time.perf_counter()

thread_1.start()   # both threads run concurrently from here
thread_2.start()

thread_1.join()     # wait for thread_1 to finish
thread_2.join()     # wait for thread_2 to finish

elapsed = time.perf_counter() - start_time
print(f"Both downloads finished in about {elapsed:.1f}s (not 0.3s - they overlapped)")
# Output (order may vary since both threads run concurrently):
# Downloaded menu for South Indian Tiffin
# Downloaded menu for Punjabi Dhaba
# Both downloads finished in about 0.2s (not 0.3s - they overlapped)

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3: Race Conditions - Why Shared State Is Dangerous
# ════════════════════════════════════════════════════════════════
# A RACE CONDITION happens when multiple threads read and write shared
# data at the same time, and the final result depends on unpredictable
# timing. Below, several threads increment a shared counter WITHOUT
# protection. We deliberately separate the "read" and "write" steps
# (with a tiny yield in between) to make the race visible - in real
# code, a race can be this subtle even without an explicit yield.

unsafe_counter = 0


def increment_unsafe(times):
    global unsafe_counter
    for _ in range(times):
        current_value = unsafe_counter    # READ
        time.sleep(0)                     # yields control - another thread can run here
        unsafe_counter = current_value + 1  # WRITE (may overwrite another thread's update)


threads = [threading.Thread(target=increment_unsafe, args=(500,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected 2000, got (unsafe): {unsafe_counter}")
# Output: Expected 2000, got (unsafe): <some number less than 2000>
# NOTE: The exact wrong number varies by run - that unpredictability
# IS the race condition. Some increments get silently lost.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 4: threading.Lock - Protecting Shared State
# ════════════════════════════════════════════════════════════════
# A Lock ensures only ONE thread can execute a block of code at a
# time (the "critical section"). Acquiring an already-locked Lock
# makes a thread wait until it's released.

safe_counter = 0
counter_lock = threading.Lock()


def increment_safe(times):
    global safe_counter
    for _ in range(times):
        with counter_lock:      # acquires the lock, releases automatically after
            current_value = safe_counter
            time.sleep(0)        # even with a yield here, the lock prevents a race
            safe_counter = current_value + 1


threads = [threading.Thread(target=increment_safe, args=(500,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected 2000, got (safe): {safe_counter}")
# Output: Expected 2000, got (safe): 2000

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 5: ThreadPoolExecutor - A Higher-Level API
# ════════════════════════════════════════════════════════════════
# Manually creating and joining threads gets tedious for many tasks.
# `ThreadPoolExecutor` manages a pool of worker threads for you.
# `.map()` runs a function over an iterable across the pool and
# returns results IN ORDER (even though execution may finish out of
# order internally).

def get_delivery_estimate(city):
    """Simulates an I/O-bound API call estimating delivery time."""
    delays = {"Mumbai": 0.15, "Delhi": 0.1, "Pune": 0.05}
    time.sleep(delays.get(city, 0.1))
    return f"{city}: 30 minutes"


cities = ["Mumbai", "Delhi", "Pune"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(get_delivery_estimate, cities))

for result in results:
    print(result)
# Output:
# Mumbai: 30 minutes
# Delhi: 30 minutes
# Pune: 30 minutes

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

# ── Example 1: Naming Threads for Clarity ──
def print_task_name():
    print(f"Running on thread: {threading.current_thread().name}")


worker_thread = threading.Thread(target=print_task_name, name="OrderProcessor")
worker_thread.start()
worker_thread.join()
# Output: Running on thread: OrderProcessor

print("-" * 50)

# ── Example 2: Passing Results Back via a Shared List + Lock ──
results_list = []
results_lock = threading.Lock()


def compute_square(number):
    result = number * number
    with results_lock:
        results_list.append(result)


number_threads = [threading.Thread(target=compute_square, args=(n,)) for n in [2, 4, 6]]
for t in number_threads:
    t.start()
for t in number_threads:
    t.join()

print(sorted(results_list))
# Output: [4, 16, 36]

print("-" * 50)

# ── Example 3: Checking if a Thread Is Alive ──
def slow_task():
    time.sleep(0.2)


bg_thread = threading.Thread(target=slow_task)
bg_thread.start()
print(f"Is thread alive right after start? {bg_thread.is_alive()}")
# Output: Is thread alive right after start? True
bg_thread.join()
print(f"Is thread alive after join? {bg_thread.is_alive()}")
# Output: Is thread alive after join? False

print("-" * 50)

# ── Example 4: ThreadPoolExecutor with submit() and Futures ──
def calculate_gst(amount):
    return round(amount * 0.18, 2)


with ThreadPoolExecutor(max_workers=2) as executor:
    future_1 = executor.submit(calculate_gst, 1000)
    future_2 = executor.submit(calculate_gst, 2500)
    print(f"GST on 1000: {future_1.result()}")
    print(f"GST on 2500: {future_2.result()}")
# Output:
# GST on 1000: 180.0
# GST on 2500: 450.0

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Write a function `book_seat_safe(seats_booked_list, passenger_name,
# lock)` that appends `passenger_name` to `seats_booked_list` while
# holding `lock`. Create a shared list and a shared Lock, spawn 3
# threads booking "Priya", "Arjun", and "Meera" respectively, join
# them all, then print sorted(seats_booked_list).
#
# Expected output:
#   ['Arjun', 'Meera', 'Priya']

# YOUR CODE HERE
def book_seat_safe(seats_booked_list, passenger_name, lock):
    with lock:
        seats_booked_list.append(passenger_name)


booking_lock = threading.Lock()
seats_booked = []

passenger_threads = [
    threading.Thread(target=book_seat_safe, args=(seats_booked, name, booking_lock))
    for name in ["Priya", "Arjun", "Meera"]
]

for t in passenger_threads:
    t.start()
for t in passenger_threads:
    t.join()

print(sorted(seats_booked))
# Output: ['Arjun', 'Meera', 'Priya']


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file, you learned:
#   - threading.Thread + start()/join() runs I/O-bound tasks concurrently
#   - Race conditions occur when threads share mutable state unsafely
#   - threading.Lock (with the `with` statement) prevents race conditions
#   - ThreadPoolExecutor offers a higher-level pool-based API
#
# Next file: day16_02_multiprocessing.py
#   - The multiprocessing module for CPU-bound parallelism

if __name__ == "__main__":
    print("\nDay 16, File 1 complete: The threading Module")
