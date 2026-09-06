import pandas as pd
import numpy as np

# --- Step 1: Create Synthetic Operations Data ---
# Use modern random number generator (preferred over np.random.seed)
rng = np.random.default_rng(9)  # Reproducible results with seed 9
n = 120

ops = pd.DataFrame({
    "region": rng.choice(["North", "South", "West"], n),
    "team": rng.choice(["Core", "Edge", "Data"], n),
    "channel": rng.choice(["email", "chat", "web"], n),
    "minutes": rng.gamma(4, 10, n).round(1),  # Gamma distribution (skewed right)
    "satisfaction": rng.normal(4.2, 0.45, n).clip(1, 5),  # Normal, clipped to 1-5
    "resolved": rng.random(n) > 0.18,  # 82% resolved, 18% unresolved
})

print("=== Sample Data (First 5 Rows) ===")
print(ops.head())
print()
print("=== Data Info ===")
print(ops.info())
print()

# --- Step 2: Region-Level Summary ---
summary = ops.groupby("region", observed=True).agg(
    tickets=("minutes", "size"),           # Count of tickets per region
    median_minutes=("minutes", "median"),  # Median resolution time
    resolution_rate=("resolved", "mean"),  # Proportion resolved
).sort_values("resolution_rate")           # Sort by best performing region

print("=== Region Summary (Sorted by Resolution Rate) ===")
print(summary)
print()

# --- Step 3: Calculate Z-Score Within Each Region ---
# Transform creates a new column with the same length as original
ops["region_minutes_z"] = ops.groupby("region")["minutes"].transform(
    lambda s: (s - s.mean()) / s.std(ddof=0)  # Population standard deviation
)

print("=== Data with Z-Score Column (First 5 Rows) ===")
print(ops[["region", "minutes", "region_minutes_z"]].head())
print()

# --- Step 4: Filter Teams with at Least 35 Tickets ---
large_teams = ops.groupby("team").filter(lambda g: len(g) >= 35)

print("=== Large Teams Filtered (>= 35 tickets) ===")
print("Original size:", len(ops))
print("Filtered size:", len(large_teams))
print("\nTeam counts in filtered data:")
print(large_teams["team"].value_counts())
print()

# --- Step 5: Verify Data Quality ---
# Check that z-score mean is approximately 0 for each region
z_means = ops.groupby("region")["region_minutes_z"].mean()
print("=== Z-Score Means by Region (should be ~0) ===")
print(z_means)
print()

# Check that z-score std is approximately 1 for each region
z_stds = ops.groupby("region")["region_minutes_z"].std()
print("=== Z-Score Std Devs by Region (should be ~1) ===")
print(z_stds)
print()

# --- Step 6: Additional Insights ---
# Top 5 slowest tickets within each region
slowest = ops.groupby("region").apply(
    lambda g: g.nlargest(3, "minutes")[["team", "channel", "minutes", "region_minutes_z"]]
)
print("=== Top 3 Slowest Tickets by Region ===")
print(slowest)
print()

# --- Assertions ---
# Summary should have exactly 3 rows (one per region)
assert len(summary) == 3
print("✅ Assertion 1: Summary has 3 regions")

# Z-score column should have no missing values
assert ops["region_minutes_z"].notna().all()
print("✅ Assertion 2: All z-scores are calculated")

# Large teams should only include teams with >= 35 rows
team_counts = large_teams["team"].value_counts()
assert (team_counts >= 35).all()
print("✅ Assertion 3: All teams in filtered data have >= 35 tickets")

print("\n✅ All assertions passed!")