"""
Day 12 — Modules & Packages (Part 3 of 3)
==========================================

Topic   : Standard library modules — os, sys, math, datetime, pathlib
Covers  : Common, everyday functions from five core standard library
          modules that ship with every Python installation
Prereqs : Day 12 Part 1 (imports & packages), Day 12 Part 2 (__main__ guard)
Run with: python day12_03_stdlib_modules.py

WHY THESE FIVE MODULES?
Python's standard library is sometimes called "batteries included" —
these five modules cover file system access (os, pathlib), program/
system info (sys), math (math), and dates/times (datetime). You will
use at least one of these in nearly every script you write from here
onward, including the Day 26-30 capstone project.
"""

import os
import sys
import math
import datetime
from pathlib import Path

# ════════════════════════════════════════════════════════════════
# SECTION 1: THE `os` MODULE — OPERATING SYSTEM INTERACTION
# ════════════════════════════════════════════════════════════════

# ── Concept: os.getcwd(), os.listdir(), os.environ ──
print("── os module ──")
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

files_here = os.listdir(current_directory)
print(f"Number of items in this folder: {len(files_here)}")

# os.environ lets you read environment variables (e.g. system settings)
home_path = os.environ.get("HOME", "Not set on this system")
print(f"HOME environment variable: {home_path}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: THE `sys` MODULE — INTERPRETER & PROGRAM INFO
# ════════════════════════════════════════════════════════════════

# ── Concept: sys.version, sys.argv, sys.exit() (not called here) ──
print("── sys module ──")
print(f"Python version running this script: {sys.version.split()[0]}")
print(f"Command-line arguments passed to script: {sys.argv}")
# Output (when run with no extra args): ['day12_03_stdlib_modules.py']

# sys.exit(code) would stop the program immediately with an exit code.
# We do NOT call it here since it would end the script early, but in
# real CLI tools (like our Day 26-30 capstone) it is used to signal
# success (0) or failure (non-zero) to whoever ran the program.
print("sys.exit(code) is used to stop a program early (not called in this demo)")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: THE `math` MODULE — RECAP & EXTRAS
# ════════════════════════════════════════════════════════════════

# ── Concept: math.pow, math.log, math.gcd, math.isclose ──
print("── math module ──")
print(f"2 raised to the power 10: {math.pow(2, 10)}")
print(f"Natural log of 100: {math.log(100):.4f}")
print(f"GCD of 48 and 180: {math.gcd(48, 180)}")
print(f"Is 0.1 + 0.2 close to 0.3? {math.isclose(0.1 + 0.2, 0.3)}")
# Output:
# 2 raised to the power 10: 1024.0
# Natural log of 100: 4.6052
# GCD of 48 and 180: 12
# Is 0.1 + 0.2 close to 0.3? True

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 4: THE `datetime` MODULE — DATES AND TIMES
# ════════════════════════════════════════════════════════════════

# ── Concept: datetime.now(), date(), timedelta(), strftime() ──
print("── datetime module ──")
now = datetime.datetime.now()
print(f"Current date and time: {now.strftime('%d-%m-%Y %H:%M:%S')}")

independence_day = datetime.date(2026, 8, 15)
days_remaining = (independence_day - now.date()).days
print(f"Days remaining until Independence Day 2026: {days_remaining}")

one_week_later = now + datetime.timedelta(days=7)
print(f"One week from now: {one_week_later.strftime('%d-%m-%Y')}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 5: THE `pathlib` MODULE — MODERN FILE PATHS
# ════════════════════════════════════════════════════════════════

# ── Concept: Path objects instead of raw strings ──
# pathlib.Path is the modern, recommended way to work with file paths —
# preferred over building path strings manually with os.path.
print("── pathlib module ──")
current_path = Path(current_directory)
print(f"As a Path object: {current_path}")
print(f"Parent directory: {current_path.parent}")

sample_file_path = current_path / "day12_notes.txt"
print(f"Joined path (using / operator): {sample_file_path}")
print(f"File extension would be: {sample_file_path.suffix}")
print(f"File stem (name without extension): {sample_file_path.stem}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Mumbai Weather Station Logger (combining all five)
# ════════════════════════════════════════════════════════════════

print("── Guided Example 1: Building today's log filename with pathlib ──")
log_folder = Path(current_directory) / "weather_logs"
today_str = datetime.date.today().strftime("%Y_%m_%d")
log_file = log_folder / f"mumbai_weather_{today_str}.log"
print(f"Today's log file would be saved at: {log_file}")

print("-" * 50)

print("── Guided Example 2: Calculating heat index roughly using math ──")
temperature_c = 36.5
humidity_percent = 78
heat_index_estimate = temperature_c + 0.05 * humidity_percent
print(f"Temp: {temperature_c}°C, Humidity: {humidity_percent}% -> "
      f"rough heat index: {heat_index_estimate:.1f}°C")

print("-" * 50)

print("── Guided Example 3: Listing only .py files using os and pathlib ──")
py_files = [f for f in current_path.iterdir() if f.suffix == ".py"]
print(f"Python files found in this folder: {len(py_files)}")
for f in py_files[:3]:
    print(f"  - {f.name}")

print("-" * 50)

print("── Guided Example 4: Logging a reading with a timestamp ──")


def format_log_entry(city, temp_c, reading_time):
    return f"[{reading_time.strftime('%H:%M:%S')}] {city}: {temp_c}°C"


reading_time = datetime.datetime.now()
print(format_log_entry("Mumbai", 33.2, reading_time))

print("-" * 50)

print("── Guided Example 5: Checking the platform with sys/os ──")
print(f"Platform identifier (sys.platform): {sys.platform}")
print(f"Path separator on this system (os.sep): '{os.sep}'")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# 1. Use pathlib to build a Path for a file named "rainfall_report.csv"
#    inside a "reports" subfolder of the current directory.
# 2. Use math.ceil to round up a rainfall value of 47.3 mm.
# 3. Use datetime to print today's date in DD-MM-YYYY format.
# 4. Print a single combined sentence using all three results.
#
# Expected output (date will vary):
#    Report path: <path>/reports/rainfall_report.csv | Rainfall (rounded
#    up): 48 mm | Report date: <DD-MM-YYYY>

# YOUR CODE HERE
report_path = current_path / "reports" / "rainfall_report.csv"
rainfall_rounded = math.ceil(47.3)
report_date = datetime.date.today().strftime("%d-%m-%Y")
print(
    f"Report path: {report_path} | "
    f"Rainfall (rounded up): {rainfall_rounded} mm | "
    f"Report date: {report_date}"
)

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Covered in this file:
#   - os: getcwd(), listdir(), environ
#   - sys: version, argv, exit() (referenced)
#   - math: pow(), log(), gcd(), isclose()
#   - datetime: now(), date(), timedelta(), strftime()
#   - pathlib: Path objects, the / join operator, .suffix, .stem, .parent
#
# This wraps up Day 12 — Modules & Packages. Next session (Day 13) moves
# into Iterators & Generators: the __iter__/__next__ protocol, the yield
# keyword, generator expressions, and the itertools module.

if __name__ == "__main__":
    print("\nDay 12, Part 3 (Standard Library Modules) complete!")
    print("Day 12 — Modules & Packages — fully complete!")
