# Select unresolved tickets with minutes above the median,
# returning only team, channel, and minutes.
# Sort descending by minutes.
# Deliverable: A DataFrame and an assertion that
# every returned row meets both conditions.
# Hint: Build the mask first, then use loc.

import pandas as pd
import numpy as np
from io import StringIO

# --- Load the Data ---
raw = """ticket_id,team,channel,minutes,satisfaction,resolved
T101,Core,email,35,4.6,True
T102,Edge,chat,18,4.9,True
T103,Core,web,72,4.6,False
T104,Data,email,51,3.8,True
T105,Edge,web,44,4.1,False
T106,Data,chat,29,4.7,True
"""

tickets = pd.read_csv(StringIO(raw))

print("=== Raw Data ===")
print(tickets)
print()

# --- Step 1: Calculate the Median of Minutes ---
median_minutes = tickets["minutes"].median()
print(f"Median minutes: {median_minutes}")
print()

# --- Step 2: Build the Filter Mask ---
# Condition 1: Unresolved tickets (resolved == False)
unresolved_mask = tickets["resolved"] == False

# Condition 2: Minutes above the median
above_median_mask = tickets["minutes"] > median_minutes

# Combined mask: BOTH conditions must be True
mask = unresolved_mask & above_median_mask

print(f"Rows that meet both conditions: {mask.sum()}")
print(f"Mask:\n{mask}")
print()

# --- Step 3: Use .loc to Select Rows and Columns ---
# Select rows where mask is True, and only specific columns
result = tickets.loc[mask, ["team", "channel", "minutes"]]

# --- Step 4: Sort Descending by Minutes ---
result = result.sort_values("minutes", ascending=False)

print("=== Result: Unresolved Tickets Above Median Minutes ===")
print(result)
print()

# --- Step 5: Assertion to Verify Both Conditions ---
# Verify all returned rows are unresolved
assert (result["minutes"] > median_minutes).all(), "All rows should have minutes above median"
assert (tickets.loc[result.index, "resolved"] == False).all(), "All rows should be unresolved"

print("✅ All assertions passed! Data is valid.")

# --- Bonus: Show the Complete Verification ---
print("\n=== Verification Details ===")
print(f"All minutes > {median_minutes}? {(result['minutes'] > median_minutes).all()}")
print(f"All unresolved? {(tickets.loc[result.index, 'resolved'] == False).all()}")
print(f"Result shape: {result.shape}")
