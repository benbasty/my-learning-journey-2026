import pandas as pd

# --- Orders Table ---
orders = pd.DataFrame({
    "order_id": [11, 12, 13, 14],
    "customer_id": [1, 2, 1, 4],
    "amount": [80, 55, 120, 40],
})

print("=== Orders Table ===")
print(orders)
print()

# --- Customers Table ---
customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "segment": ["Growth", "Core", "Core"],
})

print("=== Customers Table ===")
print(customers)
print()

# --- LEFT JOIN: Enrich orders with customer segment ---
enriched = orders.merge(
    customers,
    on="customer_id",         # Column to join on
    how="left",               # Keep ALL orders (even if no customer match)
    validate="many_to_one",   # Enforce that customers have unique IDs
    indicator=True,           # Add a column showing join status
)

print("=== Enriched Orders (LEFT JOIN) ===")
print(enriched)
print()

# --- Analyze the join status ---
print("=== Join Status Distribution ===")
print(enriched["_merge"].value_counts())
print()

# --- Assertions: Verify data quality ---
assert len(enriched) == len(orders)
print("✅ Assertion 1 passed: All orders preserved (same length)")

assert enriched["order_id"].is_unique
print("✅ Assertion 2 passed: No duplicate orders")

print("\n✅ All assertions passed! Data is clean and correctly joined.")