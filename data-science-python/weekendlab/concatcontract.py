import pandas as pd
import numpy as np

# --- Create Three Monthly DataFrames with Different Columns ---
jan = pd.DataFrame({
    "product": ["A", "B", "C"],
    "sales": [100, 150, 120],
    "quantity": [10, 15, 12]
})

feb = pd.DataFrame({
    "product": ["A", "B", "D"],
    "sales": [110, 130, 90],
    "returns": [5, 2, 1]  # New column!
})

mar = pd.DataFrame({
    "product": ["B", "C", "D"],
    "sales": [140, 115, 95],
    "quantity": [14, 11, 9],
    "promo": [True, False, True]  # Another new column!
})

print("=== January Data ===")
print(jan)
print("\n=== February Data ===")
print(feb)
print("\n=== March Data ===")
print(mar)
print()

# --- Method 1: Concatenate with Outer Join (Default) ---
# Keeps ALL columns, fills missing with NaN
combined_outer = pd.concat(
    [jan, feb, mar],
    keys=["Jan", "Feb", "Mar"],
    names=["month", "row"],
    join="outer"  # This is the default behavior
)

print("=== Combined Data (OUTER JOIN - Keeps All Columns) ===")
print(combined_outer)
print()
print(f"Shape: {combined_outer.shape}")
print(f"Columns: {combined_outer.columns.tolist()}")
print()

# --- Method 2: Concatenate with Inner Join ---
# Keeps ONLY columns that appear in ALL DataFrames
combined_inner = pd.concat(
    [jan, feb, mar],
    keys=["Jan", "Feb", "Mar"],
    names=["month", "row"],
    join="inner"  # Only columns common to ALL DataFrames
)

print("=== Combined Data (INNER JOIN - Common Columns Only) ===")
print(combined_inner)
print()
print(f"Shape: {combined_inner.shape}")
print(f"Columns: {combined_inner.columns.tolist()}")
print()

# --- Step 3: Identify What Was Discarded ---
all_columns = set(jan.columns) | set(feb.columns) | set(mar.columns)
common_columns = set(jan.columns) & set(feb.columns) & set(mar.columns)
discarded_columns = all_columns - common_columns

print("=== Column Comparison ===")
print(f"All columns across all months: {sorted(all_columns)}")
print(f"Common columns (in ALL months): {sorted(common_columns)}")
print(f"Discarded columns (inner join removes): {sorted(discarded_columns)}")
print()

# --- Step 4: Show What Data Gets Discarded ---
print("=== What Inner Join Discards ===")
for col in discarded_columns:
    months_with_col = [name for name, df in [("Jan", jan), ("Feb", feb), ("Mar", mar)] 
                       if col in df.columns]
    print(f"  - '{col}' exists only in: {', '.join(months_with_col)}")
print()

# --- Step 5: Demonstrate How to Access Data ---
print("=== Accessing Data by Month ===")
print("January sales (all columns):")
print(combined_outer.loc["Jan"])
print()

print("February sales with returns (outer join preserves returns):")
print(combined_outer.loc["Feb", ["sales", "returns"]])
print()

print("March sales with promo (outer join preserves promo):")
print(combined_outer.loc["Mar", ["sales", "promo"]])
print()

# --- Step 6: Assertions to Verify ---
# Outer join should have more columns than inner join
assert len(combined_outer.columns) > len(combined_inner.columns)
print(f"✅ Outer join has {len(combined_outer.columns)} columns, inner has {len(combined_inner.columns)}")

# Outer join should preserve all rows
assert len(combined_outer) == len(jan) + len(feb) + len(mar)
print(f"✅ Both joins preserve all rows: {len(combined_outer)} total rows")

# The common columns should be present in both
common_cols = ["product", "sales"]
for col in common_cols:
    assert col in combined_outer.columns
    assert col in combined_inner.columns
print(f"✅ Common columns '{', '.join(common_cols)}' present in both")

print("\n✅ All assertions passed!")