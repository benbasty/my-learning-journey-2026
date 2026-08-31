# Create two Series of inventory with overlapping but differently ordered product labels.
# Add them once normally and once with add(fill_value=0).
# Deliverable: Two results and a short explanation of missing labels.
# Hint: Pandas aligns by label, not by visible row position.

# Pandas = not about positions but labels
# automatic alignment by index label.

import pandas as pd
import numpy as np

# --- Create Two Series with Overlapping but Differently Ordered Labels ---
# System A: Inventory report from Warehouse A
inv_a = pd.Series({
    "Apples": 50,
    "Bananas": 30,
    "Cherries": 20,
    "Dates": 15
})

# System B: Inventory report from Warehouse B (different order, some overlap)
inv_b = pd.Series({
    "Bananas": 25,     # Overlap with A
    "Dates": 10,       # Overlap with A
    "Apples": 45,      # Overlap with A
    "Elderberries": 5  # Only in B!
})

print("=== Series A (Warehouse A) ===")
print(inv_a)
print("\n=== Series B (Warehouse B) ===")
print(inv_b)
print()

# --- Method 1: Normal Addition (Aligns by Label, Missing = NaN) ---
result_normal = inv_a + inv_b

print("=== Normal Addition (Missing values become NaN) ===")
print(result_normal)
print()

# --- Method 2: Addition with fill_value=0 (Missing values become 0) ---
result_filled = inv_a.add(inv_b, fill_value=0)

print("=== Addition with fill_value=0 (Missing values treated as 0) ===")
print(result_filled)
print()

# --- Let's see the actual calculation step-by-step ---
print("=== What's Happening Behind the Scenes ===")
print("Products in A only: Cherries (20) - B has none, so NaN or 0")
print("Products in B only: Elderberries (5) - A has none, so NaN or 0")
print("Products in both: Apples (50+45=95), Bananas (30+25=55), Dates (15+10=25)")
print()

# --- Bonus: Show the labels explicitly ---
print("=== Labels in A ===")
print(inv_a.index.tolist())
print("=== Labels in B ===")
print(inv_b.index.tolist())
print("=== Combined Labels (Union) ===")
print(inv_a.index.union(inv_b.index).tolist())