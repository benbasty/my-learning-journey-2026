import numpy as np

# Create three shape-(4,) site arrays. Stack them as rows, append a fifth hour as a column, then split the result after rows 1 and 2.

#create a modern generator
rng = np.random.default_rng()

row1 = np.array(rng.choice(10, size=4, replace=False))
row2 = np.array(rng.choice(10, size=4, replace=False))
row3 = np.array(rng.choice(10, size=4, replace=False))

sitearrays = np.vstack((row1, row2, row3))

fifth_hour = rng.choice(10, size=3, replace=False)
sitearraysappended = np.column_stack((sitearrays, fifth_hour))

# split the result after rows 1 and 2.
split_sitearrays = np.split(sitearraysappended, [1, 2])




