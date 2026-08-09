import numpy as np

# Build a (2 days, 3 stores, 4 products) revenue cube from values 100 through 123. 
# Produce daily totals, store totals across both days, 
# and a copy containing only products 1 and 3. Swap the day and store axes.

revenue = np.arange(100,124).reshape(2, 3, 4) # days, store, products
# axis 0: day, axis 1: store, axis 2: products

# KEEP day, REMOVE store + product
dailytotals = revenue.sum(axis=(1, 2))

# keep store, remove day + product
storetotals = revenue.sum(axis=(0, 2))

# Swap the day and store axes.
finalrevenue = revenue.swapaxes(0, 1)

print(dailytotals)
print(storetotals)
print(finalrevenue)