"""
Day 16 - Concurrency Basics
File 2 of 3: The `multiprocessing` Module

Covers:
    - Why multiprocessing exists (bypassing the GIL for CPU-bound work)
    - Creating and starting processes with `multiprocessing.Process`
    - Sharing results back with `multiprocessing.Queue`
    - `ProcessPoolExecutor` - a higher-level API (like ThreadPoolExecutor)
    - Threading vs multiprocessing: when to use which

Prerequisites:
    - day16_01_threading.py

How to run:
    python day16_02_multiprocessing.py

IMPORTANT: On some platforms (Windows, and macOS with the "spawn"
start method), multiprocessing code MUST live inside
`if __name__ == "__main__":` to avoid infinite process spawning.
This file follows that convention throughout.
"""

import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor


# ════════════════════════════════════════════════════════════════
# SECTION 1: Why multiprocessing? Escaping the GIL
# ════════════════════════════════════════════════════════════════
# CPython's Global Interpreter Lock (GIL) allows only ONE thread to
# execute Python bytecode at a time, even on a multi-core machine.
# For CPU-bound work (heavy computation), threading.Thread objects
# don't actually run in parallel - they take turns.
#
# multiprocessing.Process creates a SEPARATE PYTHON PROCESS, each
# with its OWN GIL and memory space. This means CPU-bound work can
# run truly in parallel across multiple CPU cores.

def count_primes_up_to(limit):
    """CPU-bound task: count prime numbers up to `limit`."""
    count = 0
    for number in range(2, limit):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


# ════════════════════════════════════════════════════════════════
# SECTION 2: Creating and Starting a Process
# ════════════════════════════════════════════════════════════════
# The API mirrors threading.Thread closely: Process(target=...),
# .start(), .join(). Processes do NOT share memory, so a function's
# return value is NOT automatically available to the parent - print
# statements inside a process go to the same terminal, but variables
# do not carry back automatically (see Section 3 for how to fix this).

def announce_batch_start(batch_name):
    print(f"Processing batch: {batch_name} (PID: {multiprocessing.current_process().pid})")


def run_section_2():
    process_1 = multiprocessing.Process(target=announce_batch_start, args=("Batch-A",))
    process_2 = multiprocessing.Process(target=announce_batch_start, args=("Batch-B",))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
    # Output (PIDs will vary, order may vary):
    # Processing batch: Batch-A (PID: <some number>)
    # Processing batch: Batch-B (PID: <some number>)


# ════════════════════════════════════════════════════════════════
# SECTION 3: Getting Results Back with multiprocessing.Queue
# ════════════════════════════════════════════════════════════════
# Since processes don't share memory, we use a Queue (a process-safe
# pipe) to send results from a child process back to the parent.

def compute_and_queue(number, result_queue):
    result_queue.put((number, number * number))


def run_section_3():
    result_queue = multiprocessing.Queue()
    numbers = [3, 5, 7]

    processes = [
        multiprocessing.Process(target=compute_and_queue, args=(n, result_queue))
        for n in numbers
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # Collect results from the queue (order may not match input order)
    results = {}
    while not result_queue.empty():
        number, square = result_queue.get()
        results[number] = square

    for n in sorted(results):
        print(f"{n} squared is {results[n]}")
    # Output:
    # 3 squared is 9
    # 5 squared is 25
    # 7 squared is 49


# ════════════════════════════════════════════════════════════════
# SECTION 4: ProcessPoolExecutor - A Higher-Level API
# ════════════════════════════════════════════════════════════════
# Just like ThreadPoolExecutor, but backed by separate processes.
# `.map()` distributes work across worker processes and returns
# results IN ORDER.

def run_section_4():
    limits = [10_000, 20_000, 5_000]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(count_primes_up_to, limits))

    for limit, prime_count in zip(limits, results):
        print(f"Primes below {limit}: {prime_count}")
    # Output:
    # Primes below 10000: 1229
    # Primes below 20000: 2262
    # Primes below 5000: 669


# ════════════════════════════════════════════════════════════════
# SECTION 5: Threading vs Multiprocessing - Choosing the Right Tool
# ════════════════════════════════════════════════════════════════
# | Situation                          | Use             |
# |-------------------------------------|-----------------|
# | Waiting on network/API calls        | threading       |
# | Waiting on file/disk I/O            | threading       |
# | Heavy number crunching              | multiprocessing |
# | Image/video processing              | multiprocessing |
# | Need to share memory easily         | threading       |
# | Need true parallel CPU execution    | multiprocessing |

def print_comparison_table():
    print("threading    -> best for I/O-bound waiting (network, disk)")
    print("multiprocessing -> best for CPU-bound crunching (math, data processing)")


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

def square_task(n, q):
    q.put(n * n)


def cube_task(n):
    return n ** 3


def run_guided_examples():
    # ── Example 1: Two Processes Working on Different Tasks ──
    queue_1 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=square_task, args=(6, queue_1))
    p1.start()
    p1.join()
    print(f"Square of 6: {queue_1.get()}")
    # Output: Square of 6: 36

    print("-" * 50)

    # ── Example 2: ProcessPoolExecutor with submit() and Futures ──
    with ProcessPoolExecutor(max_workers=2) as executor:
        future_1 = executor.submit(cube_task, 3)
        future_2 = executor.submit(cube_task, 4)
        print(f"Cube of 3: {future_1.result()}")
        print(f"Cube of 4: {future_2.result()}")
    # Output:
    # Cube of 3: 27
    # Cube of 4: 64

    print("-" * 50)

    # ── Example 3: Checking Process Identity ──
    current = multiprocessing.current_process()
    print(f"Main process name: {current.name}")
    # Output: Main process name: MainProcess

    print("-" * 50)

    # ── Example 4: Comparing Timing - Sequential vs Parallel (Conceptual) ──
    start = time.perf_counter()
    sequential_result = [count_primes_up_to(8000) for _ in range(3)]
    sequential_time = time.perf_counter() - start
    print(f"Sequential 3x count_primes_up_to(8000): {sequential_result} in {sequential_time:.3f}s")
    # Output: Sequential 3x count_primes_up_to(8000): [1007, 1007, 1007] in <some time>s
    # NOTE: Exact timing varies by machine - the key takeaway is that
    # ProcessPoolExecutor (Section 4) can run this kind of work in
    # PARALLEL across cores, while a plain loop runs it one at a time.


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Write a function `factorial_task(n, result_queue)` that computes n!
# (factorial) and puts the tuple (n, result) onto result_queue. Spawn
# 3 processes for n = 5, 6, 7. Collect all results into a dictionary
# and print them in order of n (5, 6, 7).
#
# Expected output:
#   5! = 120
#   6! = 720
#   7! = 5040

# YOUR CODE HERE
def factorial_task(n, result_queue):
    result = 1
    for i in range(2, n + 1):
        result *= i
    result_queue.put((n, result))


def run_mini_challenge():
    factorial_queue = multiprocessing.Queue()
    factorial_processes = [
        multiprocessing.Process(target=factorial_task, args=(n, factorial_queue))
        for n in [5, 6, 7]
    ]
    for p in factorial_processes:
        p.start()
    for p in factorial_processes:
        p.join()

    factorial_results = {}
    while not factorial_queue.empty():
        n, result = factorial_queue.get()
        factorial_results[n] = result

    for n in sorted(factorial_results):
        print(f"{n}! = {factorial_results[n]}")
    # Output:
    # 5! = 120
    # 6! = 720
    # 7! = 5040


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file, you learned:
#   - multiprocessing.Process creates separate OS processes, bypassing the GIL
#   - Processes don't share memory - use multiprocessing.Queue to pass results
#   - ProcessPoolExecutor offers a higher-level pool-based API
#   - threading = I/O-bound; multiprocessing = CPU-bound
#
# Next file: day16_03_async_await.py
#   - async/await syntax and asyncio.run() for cooperative concurrency

if __name__ == "__main__":
    run_section_2()
    print("-" * 50)
    run_section_3()
    print("-" * 50)
    run_section_4()
    print("-" * 50)
    print_comparison_table()
    print("-" * 50)
    run_guided_examples()
    print("-" * 50)
    run_mini_challenge()
    print("\nDay 16, File 2 complete: The multiprocessing Module")
