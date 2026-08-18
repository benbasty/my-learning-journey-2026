import numpy as np
price = np.array([50, 25, 100, 75, 30, 200, 15, 80])
units = np.array([10, 5, 3, 20, 40, 6, 100, 8])
category = np.array(["A", "C", "B", "A", "C", "B", "A", "D"])

revenue = price * units

# Revenue > 1000
cond_revenue = revenue > 1000

# category is 'A' or 'B'
cond_category = np.isin(category, "A", "B")

# both connditions must be true
mask = cond_revenue & cond_category

# Extract the actual data rows using fancy indexing
actual_data = np.column_stack([
    price[mask],
    units[mask],
    category[mask],
    revenue[mask]
])




