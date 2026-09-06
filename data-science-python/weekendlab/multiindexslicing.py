import pandas as pd
import numpy as np

# --- Step 1: Create Sample Monthly Revenue Data ---
np.random.seed(42)  # For reproducibility

# Generate data with a MultiIndex of (region, product)
regions = ["North", "South", "East", "West"]
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# MultiIndex from product combination
idx = pd.MultiIndex.from_product(
    [regions, products],
    names=["region", "product"]
)

# Generate random monthly revenue (100-500 per combination)
data = np.random.randint(100,500, size=len(idx))

# Create the Series with revenue data
revenue = pd.Series(data, index=idx, name="revenue")
print("=== Original Tidy Series (MultiIndex) ===")
print(revenue)
print()
print(f"Shape: {revenue.shape}")
print(f"Index levels: {revenue.index.names}")
print()

# --- Step 2: Unstack product to columns ---
# This creates a wide table: regions as rows, products as columns
revenue_wide = revenue.unstack("product")

print("=== Wide Table (Regions × Products) ===")
print(revenue_wide)
print()

# --- Step 3: Select one region's data ---
north_revenue = revenue_wide.loc["North"]
print("=== North Region Revenue by Product ===")
print(north_revenue)
print()

# --- Step 4: Calculate Region Shares of Total Revenue ---
# Method 1: Calculate share using the wide table
region_total = revenue_wide.sum(axis=1)  # Sum across products for each region
total_revenue = region_total.sum()       # Total company revenue
region_share = region_total / total_revenue

print("=== Region Totals ===")
print(region_total)
print()
print("=== Region Share of Total Revenue ===")
print(region_share)
print(f"Sum of shares: {region_share.sum():.2f} (should equal 1.0)")
print()

# --- Step 5: Alternative - Using the tidy Series directly ---
# Group by region and sum, then calculate share
region_totals_tidy = revenue.groupby("region").sum()
region_share_tidy = region_totals_tidy / region_totals_tidy.sum()

print("=== Region Shares (from Tidy Series) ===")
print(region_share_tidy)
print()

# --- Step 6: Sort the region share Series for better visualization ---
sorted_region_share = region_share.sort_values(ascending=False)

print("=== Sorted Region Shares (Descending) ===")
print(sorted_region_share)
print()

# --- Step 7: Add product share within each region ---
# Calculate percentage each product contributes within each region
product_share_by_region = revenue_wide.div(revenue_wide.sum(axis=1), axis=0) * 100

print("=== Product Share Within Each Region (%) ===")
print(product_share_by_region.round(2))
print()

# --- Step 8: Assertions to verify data quality ---
# Assert total revenue equals sum of all values
assert revenue.sum() == revenue_wide.sum().sum()
print("✅ Assertion 1 passed: Total revenue matches across formats")

# Assert region shares sum to 1 (within floating point tolerance)
assert np.isclose(region_share.sum(), 1.0)
print("✅ Assertion 2 passed: Region shares sum to 1")

# Assert revenue is positive (all revenue should be > 0)
assert (revenue > 0).all()
print("✅ Assertion 3 passed: All revenue is positive")

print("\n✅ All assertions passed! Data is clean and correctly calculated.")