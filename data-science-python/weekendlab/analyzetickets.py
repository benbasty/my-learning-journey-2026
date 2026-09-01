import pandas as pd
import numpy as np
from io import StringIO

# --- Step 1: Create Extended CSV with Deliberate Errors ---
raw = """ticket_id,team,channel,minutes,satisfaction,resolved
T101,Core,email,35,4.6,True
T102,Edge,chat,18,4.9,True
T103,Core,web,72,,False
T104,Data,email,51,3.8,True
T105,Edge,web,44,4.1,False
T106,Data,chat,29,4.7,True
T107,Core,email,91,4.2,False
T108,Edge,web,67,5.5,True
T109,Data,chat,38,,False
T110,Core,email,82,2.0,False
T111,Data,web,55,4.0,True
T112,Edge,chat,101,4.8,False
T113,Core,email,101,4.8,False
T114,Data,web,47,3.5,False
T115,Edge,chat,29,4.9,True
T116,Core,web,46,8.2,True
T117,Data,email,67,4.0,False
"""

tickets_raw = pd.read_csv(StringIO(raw))
print("=== RAW DATA (Full) ===")
print(tickets_raw)
print()

# --- Step 2: Preserve Original ---
tickets = tickets_raw.copy()

# --- Step 3: Build the Audit ---
audit = {}

# Check 1: Duplicate ticket_ids
duplicate_ids = tickets["ticket_id"].duplicated()
audit["duplicate_rows"] = duplicate_ids.sum()
audit["duplicate_ids"] = tickets.loc[duplicate_ids, "ticket_id"].tolist()

# Check 2: Impossible satisfaction scores (should be between 1 and 5)
invalid_satisfaction = ~tickets["satisfaction"].between(1, 5, inclusive="both")
audit["invalid_satisfaction_rows"] = invalid_satisfaction.sum()
audit["invalid_satisfaction_values"] = tickets.loc[invalid_satisfaction, "satisfaction"].tolist()

# Check 3: Missing values
missing_count = tickets.isna().sum()
audit["missing_values"] = missing_count.to_dict()

# Check 4: Out of range minutes (should be between 0 and 8*60 = 480)
invalid_minutes = ~tickets["minutes"].between(0, 480)
audit["invalid_minutes_rows"] = invalid_minutes.sum()

print("=== AUDIT SUMMARY ===")
for key, value in audit.items():
    print(f"{key}: {value}")
print()

# --- Step 4: Create Clean Copy with Explicit Rules ---
clean = tickets.copy()

# Rule 1: Remove duplicate ticket_ids (keep first occurrence)
clean = clean[~clean["ticket_id"].duplicated(keep="first")]

# Rule 2: Fix impossible satisfaction scores by setting to NaN
clean.loc[~clean["satisfaction"].between(1, 5, inclusive="both"), "satisfaction"] = np.nan

# Rule 3: Drop rows with missing satisfaction (since we can't impute reliably)
clean = clean[clean["satisfaction"].notna()]

# Rule 4: Fix missing minutes by replacing with team median
# We need to be careful: some teams might only have 1 row, so handle gracefully
team_medians = clean.groupby("team")["minutes"].median()
clean["minutes"] = clean["minutes"].fillna(clean["team"].map(team_medians))

# Rule 5: Drop rows with invalid minutes (beyond reasonable range)
clean = clean[clean["minutes"].between(0, 480)]

print("=== AFTER CLEANING ===")
print(clean)
print()

# --- Step 5: Team-Level Medians ---
team_medians = clean.groupby("team")["minutes"].median().reset_index()
team_medians.columns = ["team", "median_minutes"]

print("=== TEAM-LEVEL MEDIANS ===")
print(team_medians)
print()

# --- Step 6: Final Audit Summary (Three-Row Summary) ---
audit_summary = pd.DataFrame({
    "metric": ["Total Raw Rows", "Rows Removed", "Rows Kept"],
    "count": [len(tickets_raw), len(tickets_raw) - len(clean), len(clean)]
})

print("=== THREE-ROW AUDIT SUMMARY ===")
print(audit_summary)
print()

# --- Step 7: Verification ---
print("=== VERIFICATION ===")
print(f"All ticket_ids unique? {clean['ticket_id'].is_unique}")
print(f"All satisfaction between 1-5? {clean['satisfaction'].between(1, 5).all()}")
print(f"No missing minutes? {clean['minutes'].notna().all()}")
print(f"All minutes between 0-480? {clean['minutes'].between(0, 480).all()}")