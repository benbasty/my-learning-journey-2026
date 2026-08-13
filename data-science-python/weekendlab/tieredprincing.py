# Replace a loop that charges each usage value at tiered rates
# first 100 units at 0.12, next 200 at 0.18
# and all remaining units at 0.25.
# Input is a 1D array of nonnegative usage values.
# Deliverable: A vectorized function, tests at 0/100/300/450
# and a %timeit comparison on 100,000 values.
# Hint: Combine np.minimum and np.clip
# calculate each tier separately.

# instead of using loops
# we can use np.minimum and np.clip
# we can slice-and-dice the quantities
# into their respective tiers simultaneously
# for all 100,000 customers in a single blazing-fast operation.

# concept: imagine you run a water company with 500 gallons
# you habe 100000 customers
# and each customer use a certain amount of water from 0 to 500 gallons
# tier 1 = cheap, first 100 gallons valued at 0.12$ per gallon
# tier 2 = medium, 200 gallons, 0.18$/gallon
# tier 3 = expensive, more than 200 gallons, 0.25$ per gallons

# tier 1 quantity: min(usage, 100)
# tier 2 quantity: usage - 100
# tier 3 quantity: max(usage - 300, 0)


import numpy as np
def tiered_pricing(usage):
    tier1_qty = np.minimum(usage, 100) * 0.12 # Tier 1: Up to 100 units. np.minimum takes element-wise min.
    tier2_qty = np.clip(usage - 100, 0, 200) * 0.18 # Tier 2: Units between 100 and 300. # First subtract 100 (so 101 becomes 1), then clip between 0 and 200.
    tier3_qty = np.clip(usage - 300, 0, None) * 0.25 # Tier 3: Units above 300. # Subtract 300, and clip negative values to 0.
    return tier1_qty + tier2_qty  + tier3_qty



