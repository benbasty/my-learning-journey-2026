import pandas as pd
import numpy as np

# --- FIXED: Double brackets for the iterables ---
idx = pd.MultiIndex.from_product(
    [["North", "South"], ["Basic", "Pro"]],  # List of two lists
    names=["region", "plan"]
)

quarterly = pd.DataFrame(
    {"q1": [120, 85, 110, 92],
     "q2": [128, 91, 116, 99]},
    index=idx,
)

print("=== Original MultiIndex DataFrame ===")
print(quarterly)
print()

# --- The rest of the code works perfectly ---
north = quarterly.loc["North"]
print("=== North Region Only ===")
print(north)
print()

by_quarter = quarterly.stack(future_stack=True).rename("accounts")
by_quarter.index.names = ["region", "plan", "quarter"]

print("=== Stacked (Tidy) Format ===")
print(by_quarter)
print()

wide_again = by_quarter.unstack("quarter")
print("=== Unstacked Back to Original ===")
print(wide_again)
print()

# --- Verify the round-trip ---
# pd.testing.assert_frame_equal(quarterly, wide_again)
assert quarterly.equals(wide_again)
print("✅ Perfect round-trip!")