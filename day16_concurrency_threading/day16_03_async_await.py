"""
Day 16 - Concurrency Basics
File 3 of 3: `async` / `await` and `asyncio`

Covers:
    - Coroutines: functions defined with `async def`
    - `await` - pausing a coroutine without blocking the whole program
    - `asyncio.run()` - the entry point for running async code
    - `asyncio.gather()` - running multiple coroutines concurrently
    - `asyncio.sleep()` vs `time.sleep()` - why the difference matters
    - When to choose asyncio vs threading vs multiprocessing

Prerequisites:
    - day16_01_threading.py
    - day16_02_multiprocessing.py

How to run:
    python day16_03_async_await.py
"""

import asyncio
import time

# ════════════════════════════════════════════════════════════════
# SECTION 1: Coroutines - Functions That Can Pause
# ════════════════════════════════════════════════════════════════
# `async def` defines a COROUTINE - a special function that can be
# PAUSED at `await` points and resumed later, without blocking the
# rest of the program. Calling a coroutine function does NOT run it
# immediately - it creates a coroutine OBJECT that must be awaited
# or run through the event loop.

async def greet_async(name):
    """A simple coroutine - notice `async def`."""
    return f"Namaste, {name}!"


# Calling greet_async("Priya") directly does NOT execute the function -
# it returns a coroutine object that needs to be run.
coroutine_object = greet_async("Priya")
print(type(coroutine_object))
# Output: <class 'coroutine'>
coroutine_object.close()  # clean up since we won't run it here

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2: asyncio.run() - The Entry Point
# ════════════════════════════════════════════════════════════════
# `asyncio.run(coroutine)` starts the asyncio EVENT LOOP, runs the
# given coroutine to completion, and returns its result. This is
# typically called ONCE, at the top level of a program.

async def main_greeting():
    message = await greet_async("Arjun")   # await actually RUNS the coroutine
    return message


result = asyncio.run(main_greeting())
print(result)
# Output: Namaste, Arjun!

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3: asyncio.sleep() vs time.sleep()
# ════════════════════════════════════════════════════════════════
# `time.sleep()` BLOCKS the entire program/thread - nothing else can
# run during that time. `asyncio.sleep()` is "cooperative": it pauses
# ONLY the current coroutine, letting the event loop run OTHER
# coroutines during the wait. This is why asyncio is great for
# many concurrent I/O-bound tasks (like juggling API calls).

async def fetch_order_status(order_id, delay_seconds):
    """Simulates an async network call using asyncio.sleep (non-blocking)."""
    await asyncio.sleep(delay_seconds)   # yields control to the event loop
    return f"Order {order_id}: Delivered"


async def run_sequential_awaits():
    """Awaiting one at a time - this does NOT overlap the waits."""
    start = time.perf_counter()
    result_1 = await fetch_order_status("SW1001", 0.1)
    result_2 = await fetch_order_status("SW1002", 0.1)
    elapsed = time.perf_counter() - start
    print(result_1)
    print(result_2)
    print(f"Sequential awaits took about {elapsed:.1f}s (waits did NOT overlap)")
    # Output:
    # Order SW1001: Delivered
    # Order SW1002: Delivered
    # Sequential awaits took about 0.2s (waits did NOT overlap)


asyncio.run(run_sequential_awaits())

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 4: asyncio.gather() - Running Coroutines Concurrently
# ════════════════════════════════════════════════════════════════
# `asyncio.gather(*coroutines)` schedules multiple coroutines to run
# CONCURRENTLY and waits for all of them to finish, returning their
# results in the SAME ORDER they were passed in.

async def run_concurrent_gather():
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch_order_status("SW2001", 0.1),
        fetch_order_status("SW2002", 0.1),
        fetch_order_status("SW2003", 0.1),
    )
    elapsed = time.perf_counter() - start
    for result in results:
        print(result)
    print(f"Concurrent gather took about {elapsed:.1f}s (waits DID overlap)")
    # Output:
    # Order SW2001: Delivered
    # Order SW2002: Delivered
    # Order SW2003: Delivered
    # Concurrent gather took about 0.1s (waits DID overlap)


asyncio.run(run_concurrent_gather())

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 5: Choosing Between asyncio, threading, and multiprocessing
# ════════════════════════════════════════════════════════════════
# | Tool             | Best for                          | Model                    |
# |------------------|------------------------------------|--------------------------|
# | asyncio          | MANY I/O-bound tasks (100s-1000s)  | single-threaded, cooperative |
# | threading        | A FEW I/O-bound tasks               | OS threads, preemptive   |
# | multiprocessing  | CPU-bound tasks                     | separate OS processes    |
#
# asyncio typically scales to far more concurrent tasks than threading
# because it avoids the overhead of OS thread creation/switching - but
# it requires the whole call chain to use `async`/`await` consistently
# ("async all the way down").

print("asyncio    -> best for MANY concurrent I/O-bound tasks (single thread)")
print("threading  -> best for a FEW concurrent I/O-bound tasks")
print("multiprocessing -> best for CPU-bound parallel work")

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

# ── Example 1: A Coroutine That Returns a Computed Value ──
async def calculate_delivery_fee(distance_km):
    await asyncio.sleep(0.05)   # simulate a quick async pricing lookup
    return 20 + (distance_km * 8)


async def example_1():
    fee = await calculate_delivery_fee(5)
    print(f"Delivery fee for 5 km: Rs. {fee}")
    # Output: Delivery fee for 5 km: Rs. 60


asyncio.run(example_1())
print("-" * 50)


# ── Example 2: Gathering Results Into a Dictionary ──
async def get_train_status(train_number):
    await asyncio.sleep(0.05)
    statuses = {"12345": "On Time", "12951": "Delayed by 10 min"}
    return train_number, statuses.get(train_number, "Unknown")


async def example_2():
    results = await asyncio.gather(
        get_train_status("12345"),
        get_train_status("12951"),
    )
    status_dict = dict(results)
    for train_number, status in status_dict.items():
        print(f"Train {train_number}: {status}")
    # Output:
    # Train 12345: On Time
    # Train 12951: Delayed by 10 min


asyncio.run(example_2())
print("-" * 50)


# ── Example 3: asyncio.create_task() for Fire-and-Await-Later ──
async def brew_chai():
    await asyncio.sleep(0.1)
    print("Chai is ready!")
    return "chai"


async def example_3():
    # create_task() schedules the coroutine to start running NOW,
    # without blocking - we can do other work before awaiting it.
    chai_task = asyncio.create_task(brew_chai())
    print("Chai is brewing in the background...")
    result = await chai_task   # now we wait for it to finish
    print(f"Enjoying the {result}")
    # Output:
    # Chai is brewing in the background...
    # Chai is ready!
    # Enjoying the chai


asyncio.run(example_3())
print("-" * 50)


# ── Example 4: Handling Errors in Async Code ──
async def risky_api_call(should_fail):
    await asyncio.sleep(0.02)
    if should_fail:
        raise ValueError("API returned an error")
    return "Success"


async def example_4():
    try:
        result = await risky_api_call(True)
        print(result)
    except ValueError as error:
        print(f"Caught error: {error}")
    # Output: Caught error: API returned an error


asyncio.run(example_4())
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Write an async function `check_stock(item_name, in_stock)` that
# awaits asyncio.sleep(0.02) then returns f"{item_name}: In Stock" if
# in_stock is True, else f"{item_name}: Out of Stock". Using
# asyncio.gather(), concurrently check stock for:
#   ("Basmati Rice", True), ("Toor Dal", False), ("Sunflower Oil", True)
# and print each result.
#
# Expected output:
#   Basmati Rice: In Stock
#   Toor Dal: Out of Stock
#   Sunflower Oil: In Stock

# YOUR CODE HERE
async def check_stock(item_name, in_stock):
    await asyncio.sleep(0.02)
    if in_stock:
        return f"{item_name}: In Stock"
    return f"{item_name}: Out of Stock"


async def run_mini_challenge():
    items = [("Basmati Rice", True), ("Toor Dal", False), ("Sunflower Oil", True)]
    results = await asyncio.gather(*(check_stock(name, stock) for name, stock in items))
    for result in results:
        print(result)


asyncio.run(run_mini_challenge())
# Output:
# Basmati Rice: In Stock
# Toor Dal: Out of Stock
# Sunflower Oil: In Stock


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file, you learned:
#   - `async def` creates a coroutine function; calling it returns a
#     coroutine object that must be awaited or run
#   - `asyncio.run()` is the top-level entry point that starts the
#     event loop
#   - `asyncio.sleep()` is non-blocking, unlike `time.sleep()`
#   - `asyncio.gather()` runs multiple coroutines concurrently
#   - asyncio suits MANY I/O-bound tasks; threading suits a FEW;
#     multiprocessing suits CPU-bound work
#
# This completes Day 16! You now understand all three concurrency
# models Python offers: threading, multiprocessing, and asyncio.
#
# Next up: Day 17 - Advanced OOP
#   - Abstract base classes, metaclasses, Protocol classes, dataclasses

if __name__ == "__main__":
    print("\nDay 16, File 3 complete: async/await and asyncio")
