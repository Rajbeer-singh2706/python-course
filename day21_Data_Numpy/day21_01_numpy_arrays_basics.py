"""
Day 21 — Data & NumPy (Part 1 of 3)
Topic: NumPy Arrays vs Python Lists, Array Creation, Vectorized Operations

What this file covers:
    - Why NumPy exists and how ndarray differs from a Python list
    - Creating arrays: from lists, np.zeros, np.ones, np.arange, np.linspace
    - Array attributes: shape, dtype, ndim, size
    - Vectorized arithmetic (no manual loops needed)
    - Performance comparison: Python list loop vs NumPy vectorized operation

Prerequisites:
    - Day 6  : Lists, list comprehensions
    - Day 15 : map()/filter(), lambda expressions
    - Day 22 (later) will build on this with Pandas DataFrames

How to run:
    python day21_01_numpy_arrays_basics.py
"""

import numpy as np
import time

# ════════════════════════════════════════════════════════════════
# SECTION 1: Why NumPy? Lists vs Arrays
# ════════════════════════════════════════════════════════════════
# A Python list can hold mixed types and grows/shrinks freely, but that
# flexibility costs speed. Every element is a full Python object with
# its own memory overhead. NumPy's ndarray stores elements of a SINGLE
# type in one contiguous block of memory, which is why math on arrays
# is dramatically faster than looping over lists in pure Python.

# ── Concept: A Python list of prices (in rupees) for Swiggy orders ──
swiggy_order_prices = [249, 399, 180, 550, 275]
print("Python list:", swiggy_order_prices)
print("Type of list:", type(swiggy_order_prices))
# Output: Python list: [249, 399, 180, 550, 275]
# Output: Type of list: <class 'list'>

# ── Concept: The same data as a NumPy array ──
swiggy_prices_arr = np.array(swiggy_order_prices)
print("NumPy array:", swiggy_prices_arr)
print("Type of array:", type(swiggy_prices_arr))
# Output: NumPy array: [249 399 180 550 275]
# Output: Type of array: <class 'numpy.ndarray'>

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: Creating Arrays
# ════════════════════════════════════════════════════════════════

# ── Concept: np.array() from a Python list ──
zomato_ratings = np.array([4.2, 3.9, 4.6, 4.1, 3.7])
print("Zomato ratings array:", zomato_ratings)
# Output: Zomato ratings array: [4.2 3.9 4.6 4.1 3.7]

# ── Concept: np.zeros() and np.ones() — placeholder arrays ──
# Useful for pre-allocating space before filling in real values.
empty_slots = np.zeros(5)          # 5 zeros, e.g. unfilled delivery slots
full_slots = np.ones(5)            # 5 ones, e.g. all slots "booked" flag
print("Zeros:", empty_slots)
print("Ones:", full_slots)
# Output: Zeros: [0. 0. 0. 0. 0.]
# Output: Ones: [1. 1. 1. 1. 1.]

# ── Concept: np.arange() — like range(), but returns an array ──
# np.arange(start, stop, step)
delivery_day_numbers = np.arange(1, 11)   # 1 to 10
print("Delivery day numbers:", delivery_day_numbers)
# Output: Delivery day numbers: [ 1  2  3  4  5  6  7  8  9 10]

even_days = np.arange(0, 30, 2)
print("Even days in a 30-day month:", even_days)
# Output: Even days in a 30-day month: [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]

# ── Concept: np.linspace() — evenly spaced values between two points ──
# np.linspace(start, stop, num_points) — includes both endpoints.
# Useful for generating, say, 5 evenly spaced discount percentages.
discount_levels = np.linspace(0, 50, 6)
print("Discount levels (%):", discount_levels)
# Output: Discount levels (%): [ 0. 10. 20. 30. 40. 50.]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: Array Attributes
# ════════════════════════════════════════════════════════════════
# Every ndarray carries metadata describing its structure.

irctc_seat_matrix = np.array([
    [1, 0, 1, 1],   # Coach A: booked(1)/available(0) per seat
    [0, 0, 1, 0],   # Coach B
    [1, 1, 1, 0],   # Coach C
])

print("Shape:", irctc_seat_matrix.shape)   # (rows, columns)
print("Ndim:", irctc_seat_matrix.ndim)     # number of dimensions
print("Size:", irctc_seat_matrix.size)     # total number of elements
print("Dtype:", irctc_seat_matrix.dtype)   # data type of elements
# Output: Shape: (3, 4)
# Output: Ndim: 2
# Output: Size: 12
# Output: Dtype: int64

# dtype can be set explicitly at creation time.
paytm_balances = np.array([1500, 2300, 980], dtype=np.float64)
print("Float dtype balances:", paytm_balances, "| dtype:", paytm_balances.dtype)
# Output: Float dtype balances: [1500. 2300.  980.] | dtype: float64

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 4: Vectorized Operations
# ════════════════════════════════════════════════════════════════
# "Vectorized" means the operation applies to every element at once,
# without writing an explicit loop. This is the core superpower of NumPy.

flipkart_prices = np.array([1200, 3400, 899, 15999, 599])
gst_rate = 0.18

# ── Concept: Arithmetic broadcasts across the whole array ──
prices_with_gst = flipkart_prices * (1 + gst_rate)
print("Prices with 18% GST:", prices_with_gst)
# Output: Prices with 18% GST: [ 1416.  4012.   1060.82 18878.82   706.82]

# ── Concept: Element-wise comparison returns a boolean array ──
above_1000 = flipkart_prices > 1000
print("Above Rs 1000?:", above_1000)
# Output: Above Rs 1000?: [ True  True False  True False]

# ── Concept: Boolean array used to filter (boolean masking) ──
expensive_items = flipkart_prices[above_1000]
print("Expensive items:", expensive_items)
# Output: Expensive items: [ 1200  3400 15999]

# ── Concept: Aggregation functions ──
print("Total spend:", flipkart_prices.sum())
print("Average price:", flipkart_prices.mean())
print("Most expensive:", flipkart_prices.max())
print("Cheapest:", flipkart_prices.min())
# Output: Total spend: 22097
# Output: Average price: 4419.4
# Output: Most expensive: 15999
# Output: Cheapest: 599

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 5: Performance — Loop vs Vectorized
# ════════════════════════════════════════════════════════════════
# Let's prove the speed difference by squaring one million numbers
# two different ways: a pure Python loop, and a vectorized NumPy call.

N = 1_000_000
python_list = list(range(N))
numpy_array = np.arange(N)

start = time.perf_counter()
squared_list = [x * x for x in python_list]
python_time = time.perf_counter() - start

start = time.perf_counter()
squared_array = numpy_array ** 2
numpy_time = time.perf_counter() - start

print(f"Python list comprehension time: {python_time:.4f} seconds")
print(f"NumPy vectorized time:          {numpy_time:.4f} seconds")
print(f"NumPy was roughly {python_time / numpy_time:.1f}x faster")
# Output (actual numbers vary by machine, but NumPy is consistently faster):
# Python list comprehension time: 0.0xxx seconds
# NumPy vectorized time:          0.00xx seconds
# NumPy was roughly Nx faster

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Riya's BigBasket monthly grocery spend
# ════════════════════════════════════════════════════════════════
bigbasket_spend = np.array([2400, 1980, 3100, 2650, 2200])  # 5 weeks
weekly_labels = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

print("Riya Deshmukh's BigBasket spend tracker")
for label, amount in zip(weekly_labels, bigbasket_spend):
    print(f"  {label}: Rs {amount}")
print(f"Total for the month: Rs {bigbasket_spend.sum()}")
print(f"Average weekly spend: Rs {bigbasket_spend.mean():.2f}")
# Output:
# Riya Deshmukh's BigBasket spend tracker
#   Week 1: Rs 2400
#   Week 2: Rs 1980
#   Week 3: Rs 3100
#   Week 4: Rs 2650
#   Week 5: Rs 2200
# Total for the month: Rs 12330
# Average weekly spend: Rs 2466.00

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Arjun's Razorpay transaction fees
# ════════════════════════════════════════════════════════════════
razorpay_transactions = np.array([500, 12000, 3400, 890, 25000, 150])
fee_rate = 0.02  # 2% payment gateway fee

fees = razorpay_transactions * fee_rate
net_amounts = razorpay_transactions - fees

print("Arjun Mehta's Razorpay transactions")
print("Transaction amounts:", razorpay_transactions)
print("Fees charged:       ", fees)
print("Net amounts:        ", net_amounts)
print(f"Total fees paid this month: Rs {fees.sum():.2f}")
# Output:
# Arjun Mehta's Razorpay transactions
# Transaction amounts: [  500 12000  3400   890 25000   150]
# Fees charged:        [ 10.  240.   68.   17.8 500.    3. ]
# Net amounts:         [  490.   11760.    3332.     872.2  24500.    147. ]
# Total fees paid this month: Rs 838.80

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: Sanjay's IRCTC coach occupancy check
# ════════════════════════════════════════════════════════════════
coach_capacity = np.array([72, 72, 64, 72])          # seats per coach
coach_booked = np.array([65, 70, 40, 58])            # booked seats

occupancy_pct = (coach_booked / coach_capacity) * 100
print("Sanjay Verma checking IRCTC coach occupancy")
print("Capacity:  ", coach_capacity)
print("Booked:    ", coach_booked)
print("Occupancy%:", np.round(occupancy_pct, 1))
# Output:
# Sanjay Verma checking IRCTC coach occupancy
# Capacity:   [72 72 64 72]
# Booked:     [65 70 40 58]
# Occupancy%: [90.3 97.2 62.5 80.6]

nearly_full = occupancy_pct > 85
print("Coaches nearly full (>85%):", nearly_full)
# Output: Coaches nearly full (>85%): [ True  True False False]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Meera's Paytm wallet — mean, std deviation
# ════════════════════════════════════════════════════════════════
paytm_daily_spend = np.array([120, 340, 90, 560, 210, 480, 75])  # 1 week

print("Meera Iyer's Paytm wallet — weekly spend analysis")
print("Daily spend:", paytm_daily_spend)
print(f"Mean spend:    Rs {paytm_daily_spend.mean():.2f}")
print(f"Std deviation: Rs {paytm_daily_spend.std():.2f}")
print(f"Highest spend day: Rs {paytm_daily_spend.max()}")
# Output:
# Meera Iyer's Paytm wallet — weekly spend analysis
# Daily spend: [120 340  90 560 210 480  75]
# Mean spend:    Rs 267.86
# Std deviation: Rs 181.10
# Highest spend day: Rs 560

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Priya Sharma runs a small Bengaluru bakery. She has a NumPy array of
# daily sales (in rupees) for a 7-day week:
#   sales = np.array([3200, 4100, 2900, 5000, 4700, 6200, 5800])
#
# Tasks:
#   1. Print the total weekly sales.
#   2. Print the average daily sales, rounded to 2 decimal places.
#   3. Create a boolean array marking which days had sales above Rs 5000.
#   4. Use that boolean array to print only the "good" days' sales.
#
# Expected output:
#   Total weekly sales: 31900
#   Average daily sales: 4557.14
#   Above Rs 5000?: [False False False  True False  True  True]
#   Good days' sales: [5000 6200 5800]

# YOUR CODE HERE
sales = np.array([3200, 4100, 2900, 5000, 4700, 6200, 5800])

# SOLUTION:
# total = sales.sum()
# average = sales.mean()
# above_5000 = sales > 5000
# good_days = sales[above_5000]
# print("Total weekly sales:", total)
# print(f"Average daily sales: {average:.2f}")
# print("Above Rs 5000?:", above_5000)
# print("Good days' sales:", good_days)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file you learned:
#   - Why ndarray beats a plain Python list for numeric work
#   - How to create arrays with np.array, np.zeros, np.ones,
#     np.arange, and np.linspace
#   - Core attributes: shape, ndim, size, dtype
#   - Vectorized arithmetic, comparisons, boolean masking, and
#     aggregation functions (sum, mean, max, min, std)
#   - A real performance comparison proving NumPy's speed advantage
#
# Next up: day21_02_broadcasting_indexing.py
#   - Broadcasting rules for arrays of different shapes
#   - Advanced slicing and indexing (2D arrays, fancy indexing)

if __name__ == "__main__":
    print("Day 21, Part 1 complete: NumPy Arrays vs Python Lists.")
