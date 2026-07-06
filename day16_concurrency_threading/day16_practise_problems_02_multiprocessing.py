"""
Day 16 - Practice Problems (File 2 of 3)
Topic: The `multiprocessing` Module

Cumulative scope: Days 1-16

Difficulty legend:
    🟢 Warm-up   - direct application of one concept
    🟡 Core      - combines a few ideas, slightly more logic
    🔴 Challenge - multi-step reasoning, edge cases

Section Index:
    Section D - Process, start()/join() (4 problems)
    Section E - Queue & ProcessPoolExecutor (3 problems)

IMPORTANT: All problems in this file are wrapped in functions and
only executed inside `if __name__ == "__main__":`, which is required
for multiprocessing to work safely and portably.

How to run:
    python day16_practise_problems_02_multiprocessing.py
"""

import multiprocessing
from concurrent.futures import ProcessPoolExecutor


# ════════════════════════════════════════════════════════════════
# SECTION D: Process, start()/join()
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem D1  🟢 Warm-up
# --------------------------------------------------------------
# Write a function `print_greeting(name)` that prints
# f"Hello from process, {name}!". Create a single Process targeting
# it with "Meera", start it, and join it.
# Expected output:
#   Hello from process, Meera!

def print_greeting(name):
    print(f"Hello from process, {name}!")


def solve_d1():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_d1():
#     p = multiprocessing.Process(target=print_greeting, args=("Meera",))
#     p.start()
#     p.join()

# --------------------------------------------------------------
# Problem D2  🟡 Core
# --------------------------------------------------------------
# Write a function `cube_number(n, result_queue)` that puts n**3 onto
# result_queue. Spawn a single process for n=4, join it, then print
# the value retrieved from the queue.
# Expected output:
#   64

def cube_number(n, result_queue):
    result_queue.put(n ** 3)


def solve_d2():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_d2():
#     q = multiprocessing.Queue()
#     p = multiprocessing.Process(target=cube_number, args=(4, q))
#     p.start()
#     p.join()
#     print(q.get())

# --------------------------------------------------------------
# Problem D3  🟡 Core
# --------------------------------------------------------------
# Write a function `sum_range(start, end, result_queue)` that puts
# sum(range(start, end)) onto result_queue. Spawn TWO processes:
# one for sum_range(0, 50, q) and one for sum_range(50, 100, q).
# Join both, then print the TOTAL of both values pulled from the
# queue (order doesn't matter since you're summing them).
# Expected output:
#   4950

def sum_range(start, end, result_queue):
    result_queue.put(sum(range(start, end)))


def solve_d3():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_d3():
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=sum_range, args=(0, 50, q))
#     p2 = multiprocessing.Process(target=sum_range, args=(50, 100, q))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     total = q.get() + q.get()
#     print(total)

# --------------------------------------------------------------
# Problem D4  🟡 Core
# --------------------------------------------------------------
# Write a function `get_process_names(queue_obj)` that puts
# multiprocessing.current_process().name onto queue_obj. Spawn 2
# processes running this function, join them, collect both names
# from the queue into a list, and print how many UNIQUE process
# names were collected (should be 2, since each child gets its own
# default name).
# Expected output:
#   2

def get_process_names(queue_obj):
    queue_obj.put(multiprocessing.current_process().name)


def solve_d4():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_d4():
#     q = multiprocessing.Queue()
#     procs = [multiprocessing.Process(target=get_process_names, args=(q,)) for _ in range(2)]
#     for p in procs:
#         p.start()
#     for p in procs:
#         p.join()
#     names = [q.get() for _ in range(2)]
#     print(len(set(names)))


# ════════════════════════════════════════════════════════════════
# SECTION E: Queue & ProcessPoolExecutor
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem E1  🟡 Core
# --------------------------------------------------------------
# Using ProcessPoolExecutor, write `double_value(n)` returning n * 2.
# Use executor.map() to double each value in [5, 10, 15] and print
# the resulting list.
# Expected output:
#   [10, 20, 30]

def double_value(n):
    return n * 2


def solve_e1():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_e1():
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         results = list(executor.map(double_value, [5, 10, 15]))
#     print(results)

# --------------------------------------------------------------
# Problem E2  🟡 Core
# --------------------------------------------------------------
# Using ProcessPoolExecutor with .submit() and .result(), write
# `word_length(word)` returning len(word). Submit "Bengaluru" and
# "Chennai" as two separate futures, and print their lengths as a
# tuple (len_1, len_2).
# Expected output:
#   (9, 7)

def word_length(word):
    return len(word)


def solve_e2():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_e2():
#     with ProcessPoolExecutor(max_workers=2) as executor:
#         future_1 = executor.submit(word_length, "Bengaluru")
#         future_2 = executor.submit(word_length, "Chennai")
#         print((future_1.result(), future_2.result()))

# --------------------------------------------------------------
# Problem E3  🔴 Challenge
# --------------------------------------------------------------
# Write a function `is_perfect_square(n)` returning True if n is a
# perfect square, else False. Using ProcessPoolExecutor.map(), check
# numbers = [16, 20, 25, 30, 36] and build a dictionary mapping each
# number to its True/False result, then print the dictionary.
# Expected output:
#   {16: True, 20: False, 25: True, 30: False, 36: True}

def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n


def solve_e3():
    # YOUR CODE HERE
    pass


# SOLUTION:
# def solve_e3():
#     numbers = [16, 20, 25, 30, 36]
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results = list(executor.map(is_perfect_square, numbers))
#     print(dict(zip(numbers, results)))


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   D - Process, start()/join()             (4 problems)
#   E - Queue & ProcessPoolExecutor         (3 problems)
# Total: 7 problems | 🟢 1  🟡 5  🔴 1
#
# Next file: day16_practise_problems_03_async_mixed.py
#   - async/await, asyncio.gather() + mixed challenges combining all
#     three concurrency models

if __name__ == "__main__":
    print("Fill in each solve_*() function above with YOUR CODE, then")
    print("uncomment the calls below one at a time to test them.")
    print("-" * 50)
    solve_d1()
    print("-" * 50)
    solve_d2()
    print("-" * 50)
    solve_d3()
    print("-" * 50)
    solve_d4()
    print("-" * 50)
    solve_e1()
    print("-" * 50)
    solve_e2()
    print("-" * 50)
    solve_e3()
    print("\nDay 16, Practice File 2 loaded.")
