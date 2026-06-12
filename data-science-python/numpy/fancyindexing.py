# Fancy indexing is means passing an array of indices 
# to access multiple array elements at once.

import numpy as np
rng = np.random.default_rng(seed=1701)
# we have an array x
x = rng.integers(100, size=10)

# we want to access 3 differents elements
a = [x[2], x[4], x[6]]

# alternatively, we can pass a single list 
# or array of indices to obtain the same result.

ind = [2, 4, 6]
b = x[ind]
# this right there is called fancy indexing

# same method works with multidimensional arrays

# comibed indexing
# fancy indexing can be combined with the other 
# indexing schemes we’ve seen.

X = np.arange(12).reshape((3, 4))
# combine fancy and simple indices

Y = X[2, [2, 0, 1]] 
#second row, 
# 3rd index(10), first index(8), second index(9)
# returns array[][10, 8, 9]

# can also combine fancy indexing with slicing
Z = X[1:, [2, 0, 1]]

# can combine fancy indexing with masking
mask = np.array([True, False, True, False])
row = np.array([0, 1, 2]) 
col = np.array([2, 1, 3])
W = X[row[:, np.newaxis], mask]