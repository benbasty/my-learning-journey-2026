from io import StringIO #reading strings as files
import pandas as pd

# NumPy is like a Swiss Army knife for numbers.
# Pandas is like a full Excel spreadsheet
# with a built-in SQL query engine and a calculator
# that understands text, dates, and missing values all at once!

#datasetload
#This is a CSV (Comma-Separated Values) file in text form.
raw = """ticket_id, team, channel, minutes, satisfaction, resolved
T101,Core,email,35,4.6,True
T102,Edge,chat,18,4.9,True
T103,Core,web,72,,False
T104,Data,email,51,3.8,True
T105,Edge,web,44,4.1,False
T106,Data,chat,29,4.7,True
"""

tickets = pd.read_csv(StringIO(raw)) #  parses CSV data and automatically read it
print(tickets.shape) #rows annd columns
print(tickets.dtypes) #data types
print(tickets.isna().sum()) #sum of missing values
assert tickets["ticket_id"].is_unique #checks if there is duplicate ids

#selectbbylabelorposition
tickets = tickets.set_index("ticket_id")
# labeled indexing with .loc vs. position-based indexing with .iloc
# Label-based; the label slice includes both endpoints.
core_cols = tickets.loc[tickets["team"].eq("Core"),
                        ["channel", "minutes", "resolved"]]
# .loc: Stands for "Location": ou use it when you want to select by column names and row labels or conditions.
# .eq("Core") is the Pandas method for element-wise equality. It's the same as tickets["team"] == "Core" but more explicit.



# Position-based; the stop is excluded as in normal Python slicing.
preview = tickets.iloc[:3, :4]
# .iloc: Stands for "Integer Location". 
# This is position-based indexing—exactly like NumPy slicing!

# assign with .loc to make target rows and columns explicit
median_score = tickets["satisfaction"].median()
tickets.loc[:, "satisfaction"] = tickets["satisfaction"].fillna(median_score) 
assert tickets["satisfaction"].notna().all()

#inspect before transforming
tickets.info()
print(tickets.describe(include="all").T)
print(tickets.nunique(dropna=False))

valid_minutes = tickets["minutes"].between(0, 8 * 60)
valid_score = tickets["satisfaction"].between(1, 5)

assert valid_minutes.all() and valid_score.all()
tickets = tickets.assign(
    hours=tickets["minutes"] / 60,
    fast=tickets["minutes"].lt(40),
)