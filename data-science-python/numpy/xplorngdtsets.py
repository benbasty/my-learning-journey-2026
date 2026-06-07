# to explore any dataset, we can compute various summary statistics.
# the most common summary statistics are the mean and standard deviation
# with which we can summarize the “typical” values in a dataset
# but other aggregations such as : the sum, product, median, minimum and maximum, quantiles ... are useful
# NumPy has fast built-in aggregation functions for working on arrays
# Let's Go.

# SUMMING THE VALUES IN AN arrays
import numpy as np
rng = np.random.default_rng() #This function constructs a new instance of a NumPy Generator, random number generator
L = rng.random(100) # This method pulls random values from a continuous uniform distribution
S = np.sum(L)

# MINIMUM AND MAXIMUM
big_array = rng.random(1000000)
mm = np.min(big_array), np.max(big_array)

# Multidimensional Aggregates
# a common type of aggregation is an aggregation along a row or column.

M = rng.integers(0, 10, (3,4)) # creates a 3-row, 4-column table populated with whole numbers between 0 and 9.
MS = M.sum()
MMIN = M.min(axis=0)
MMMIN = M.min(axis=1)

# The axis keyword specifies the dimension of the array that will be collapsed, ???
# rather than the dimension that will be returned.
# So, specifying axis=0 means that axis 0 will be collapsed:
# for two- dimensional arrays, values within each column will be aggregated.