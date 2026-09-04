import pandas as pd
# --- Create Two Monthly DataFrames ---
jan = pd.DataFrame({"id": [1, 2], "value": [10, 12]})
feb = pd.DataFrame({"id": [3, 4], "value": [9, 15]})

print("=== January Data ===")
print(jan)
print("\n=== February Data ===")
print(feb)
print()

# --- Method 1: Concatenate with Keys (MultiIndex) ---
all_months = pd.concat(
    {"2025-01": jan, "2025-02": feb},  # Dictionary: keys become index level
    names=["month", "row"],             # Name both index levels
)

print("=== All Months (with MultiIndex) ===")
print(all_months)
print()
print(f"Shape: {all_months.shape}")
print(f"Index levels: {all_months.index.names}")
print()

# --- Assert: Total rows equal sum of parts ---
assert len(all_months) == len(jan) + len(feb)
print("✅ Assertion passed! Total rows:", len(all_months))
print()

# --- Method 2: Flat Concatenation (No MultiIndex) ---
flat = pd.concat(
    [jan, feb],              # List of DataFrames
    ignore_index=True,       # Reset index to 0, 1, 2, 3
    verify_integrity=False   # Don't check for duplicate indices
)

print("=== Flat Concatenation (ignore_index=True) ===")
print(flat)
print()
