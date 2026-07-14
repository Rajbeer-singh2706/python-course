"""
Day 22 — Data & Pandas
File 2 of 5: Reading and Writing CSV Files with Pandas

Covers:
    - Writing a DataFrame to CSV with .to_csv()
    - Reading a CSV back into a DataFrame with pd.read_csv()
    - Useful read_csv() parameters: index_col, usecols, dtype, parse_dates
    - Handling missing values while reading (na_values)
    - Exporting a filtered/derived DataFrame back to CSV

Prerequisites:
    - Day 8 (File I/O — csv module)
    - File 1 of Day 22 (DataFrame/Series basics)

How to run:
    python day22_02_read_write_csv.py

Note: This script creates its own sample CSV files in the same folder
      so it can run standalone without any external data file.
"""

import pandas as pd
import os

print("=" * 60)
print("DAY 22 - PANDAS: READING & WRITING CSV FILES")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION 1: Creating a Sample DataFrame to Export
# ════════════════════════════════════════════════════════════
print("\n── Building a Sample DataFrame ──")

irctc_bookings = pd.DataFrame({
    "pnr": ["2421567890", "2421567891", "2421567892", "2421567893", "2421567894"],
    "passenger": ["Priya Sharma", "Arjun Mehta", "Riya Deshmukh", "Sanjay Verma", "Meera Iyer"],
    "train_no": ["12951", "12622", "12301", "12002", "22691"],
    "from_station": ["Mumbai", "Chennai", "Howrah", "New Delhi", "Bengaluru"],
    "to_station": ["New Delhi", "Bengaluru", "New Delhi", "Bhopal", "New Delhi"],
    "fare": [1750, 890, 2100, 630, 2450],
    "class": ["3A", "SL", "2A", "CC", "1A"],
})
print(irctc_bookings)

# ════════════════════════════════════════════════════════════
# SECTION 2: Writing to CSV — .to_csv()
# ════════════════════════════════════════════════════════════
print("\n── Writing to CSV ──")

# index=False stops Pandas from writing the 0,1,2... row index as a column
irctc_bookings.to_csv("irctc_bookings.csv", index=False)
print("Saved irctc_bookings.csv")

# Peek at the raw file content to see what was written
with open("irctc_bookings.csv") as f:
    print("\nRaw CSV content (first 3 lines):")
    for i, line in enumerate(f):
        if i >= 3:
            break
        print(line.rstrip())
# Output: header row + first two data rows, comma-separated

# ════════════════════════════════════════════════════════════
# SECTION 3: Reading from CSV — pd.read_csv()
# ════════════════════════════════════════════════════════════
print("\n── Reading from CSV ──")

bookings_df = pd.read_csv("irctc_bookings.csv")
print(bookings_df)
print("\nDtypes after reading back:")
print(bookings_df.dtypes)
# Note: 'pnr' becomes int64 unless we tell Pandas to keep it as a string!

# ════════════════════════════════════════════════════════════
# SECTION 4: Controlling dtypes and Index While Reading
# ════════════════════════════════════════════════════════════
print("\n── Controlling dtypes with dtype= ──")

# Force pnr and train_no to stay as strings (leading zeros / long numbers
# can be corrupted if read as integers)
bookings_typed = pd.read_csv(
    "irctc_bookings.csv",
    dtype={"pnr": str, "train_no": str},
)
print(bookings_typed.dtypes)

print("\n── Using a column as the index: index_col= ──")
bookings_indexed = pd.read_csv("irctc_bookings.csv", index_col="pnr", dtype={"pnr": str})
print(bookings_indexed)
# Output: 'pnr' is now the row label instead of a regular column

print("\n── Reading only specific columns: usecols= ──")
bookings_partial = pd.read_csv(
    "irctc_bookings.csv",
    usecols=["passenger", "from_station", "to_station", "fare"],
)
print(bookings_partial)

# ════════════════════════════════════════════════════════════
# SECTION 5: Handling Missing Values
# ════════════════════════════════════════════════════════════
print("\n── Handling Missing Values ──")

# Create a CSV that has some missing/placeholder values, like real data often does
messy_csv = "irctc_bookings_messy.csv"
with open(messy_csv, "w") as f:
    f.write("pnr,passenger,fare,class\n")
    f.write("2421567895,Karan Malhotra,NA,SL\n")
    f.write("2421567896,Ananya Rao,1200,--\n")
    f.write("2421567897,Vikram Nair,,3A\n")

# na_values tells Pandas which strings should be treated as missing (NaN)
messy_df = pd.read_csv(messy_csv, na_values=["NA", "--"])
print(messy_df)
# Output: 'NA', '--', and blank cells all become NaN

print("\nMissing value check with .isna():")
print(messy_df.isna())

print("\nCount of missing values per column:")
print(messy_df.isna().sum())

# Fill missing fares with 0, and missing class with "Unknown"
messy_df["fare"] = messy_df["fare"].fillna(0)
messy_df["class"] = messy_df["class"].fillna("Unknown")
print("\nAfter filling missing values:")
print(messy_df)

# Drop any remaining rows that still have missing values (none left here)
clean_df = messy_df.dropna()
print("\nAfter dropna() (no rows lost since we already filled everything):")
print(clean_df)

# ════════════════════════════════════════════════════════════
# SECTION 6: Exporting a Filtered / Derived DataFrame
# ════════════════════════════════════════════════════════════
print("\n── Exporting a Derived DataFrame ──")

# Only export premium bookings (fare > 1000)
premium_bookings = bookings_typed[bookings_typed["fare"] > 1000]
premium_bookings.to_csv("irctc_premium_bookings.csv", index=False)
print("Saved irctc_premium_bookings.csv with", len(premium_bookings), "rows")
# Output: Saved irctc_premium_bookings.csv with 3 rows

# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# 1. Build a DataFrame `zomato_orders` with columns:
#      "restaurant" -> ["Paradise Biryani", "Truffles", "Empire"]
#      "city"       -> ["Hyderabad", "Bengaluru", "Bengaluru"]
#      "rating"     -> [4.3, 4.6, 4.1]
# 2. Save it to "zomato_orders.csv" without the index column
# 3. Read it back in and print only restaurants with rating >= 4.3

# YOUR CODE HERE
zomato_orders = pd.DataFrame({
    "restaurant": ["Paradise Biryani", "Truffles", "Empire"],
    "city": ["Hyderabad", "Bengaluru", "Bengaluru"],
    "rating": [4.3, 4.6, 4.1],
})
zomato_orders.to_csv("zomato_orders.csv", index=False)
zomato_reloaded = pd.read_csv("zomato_orders.csv")
print("\n── Mini-Challenge: Zomato Orders (rating >= 4.3) ──")
print(zomato_reloaded[zomato_reloaded["rating"] >= 4.3])
# Expected output:
#           restaurant       city  rating
# 0  Paradise Biryani  Hyderabad     4.3
# 1          Truffles  Bengaluru     4.6

# ════════════════════════════════════════════════════════════
# CLEANUP (keeps the folder tidy when re-running this script)
# ════════════════════════════════════════════════════════════
for temp_file in [
    "irctc_bookings.csv", "irctc_bookings_messy.csv",
    "irctc_premium_bookings.csv", "zomato_orders.csv",
]:
    if os.path.exists(temp_file):
        os.remove(temp_file)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# - df.to_csv("file.csv", index=False) writes without the row index
# - pd.read_csv("file.csv") reads a CSV into a DataFrame
# - dtype={} forces specific column types (protects IDs like PNR numbers)
# - index_col= sets a column as the row label
# - usecols= reads only the columns you need (faster on big files)
# - na_values=[] tells Pandas which strings mean "missing"
# - .isna(), .fillna(), .dropna() handle missing data
#
# Next: File 3 covers groupby() aggregations for summarizing data.
