import numpy as np

# --- Step 1: Create 30 Synthetic Incidents ---
np.random.seed(42)

# Field definitions for our structured array
dtype = [
    ("id", "U7"),           # Unicode string, max length 7 (e.g., "INC-001")
    ("service", "U10"),     # Service name
    ("severity", "i1"),     # 8-bit integer (1-5)
    ("latency_ms", "i4"),   # 32-bit integer
    ("resolved", "bool"),   # Boolean
]

# Generate random data
incidents = np.zeros(30, dtype=dtype)

# IDs: INC-000 to INC-029
incidents["id"] = [f"INC-{i:03d}" for i in range(30)]

# Services: randomly choose from 5 services
services = ["auth", "payment", "database", "api", "cache"]
incidents["service"] = np.random.choice(services, size=30)

# Severity: 1-5, weighted towards lower values
incidents["severity"] = np.random.choice([1, 2, 3, 4, 5], size=30, p=[0.3, 0.25, 0.2, 0.15, 0.1])

# Latency: some outliers (0-3000ms, with occasional huge spikes)
incidents["latency_ms"] = np.random.randint(0, 3000, size=30)
# Inject a few extreme outliers
incidents["latency_ms"][[5, 12, 23]] = [8000, 12000, 5000]

# Resolved: most False, some True
incidents["resolved"] = np.random.choice([True, False], size=30, p=[0.2, 0.8])

print("=== Raw Incidents (first 5) ===")
print(incidents[:5])
print()


# --- Step 2: Build the Filter Mask ---
# Condition 1: Not resolved
unresolved = incidents["resolved"] == False

# Condition 2: Severity >= 3
high_severity = incidents["severity"] >= 3

# Combined mask
mask = unresolved & high_severity

print(f"Filtered {mask.sum()} incidents (unresolved, severity >= 3)")
print()


# --- Step 3: Copy Filtered Records BEFORE Mutation ---
# IMPORTANT: We filter BEFORE clipping to avoid modifying the original data
filtered = incidents[mask].copy()

print("=== Filtered Incidents (before clipping) ===")
print(filtered)
print()


# --- Step 4: Clip Latency Outliers at 95th Percentile ---
# Calculate 95th percentile from the filtered data
p95 = np.percentile(filtered["latency_ms"], 95)

print(f"95th percentile latency: {p95:.0f} ms")

# Clip: replace values above p95 with p95
filtered["latency_ms"] = np.clip(filtered["latency_ms"], None, p95)

print("Outliers clipped!")
print()


# --- Step 5: Rank by Severity (descending) then Latency (descending) ---
# We need to sort by multiple columns, but NumPy's sort with order handles this perfectly!
# We sort ascending first, then reverse for descending
ranked = np.sort(filtered, order=["severity", "latency_ms"])[::-1]

print("=== Prioritized Incidents (Severity desc, Latency desc) ===")
print(ranked)
print()


# --- Step 6: Count Incidents by Service ---
# Use np.unique with return_counts=True on the ranked (or filtered) data
services_in_priority = ranked["service"]
unique_services, service_counts = np.unique(services_in_priority, return_counts=True)

print("=== Incident Counts by Service ===")
for service, count in zip(unique_services, service_counts):
    print(f"  {service}: {count} incidents")
print()


# --- Step 7: Bonus - Quick Stats ---
print("=== Summary Stats ===")
print(f"Total unresolved high-severity incidents: {len(ranked)}")
print(f"Average latency (after clipping): {ranked['latency_ms'].mean():.0f} ms")
print(f"Max severity: {ranked['severity'].max()}")
print(f"Min severity: {ranked['severity'].min()}")