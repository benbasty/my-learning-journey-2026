#create 5 random 2d points
# difference cube
# distance formula
# sanity check

import numpy as np
points = np.random.randn(5,2)

diffs = points[:, None, :] - points[None, :, :]
# original shape is (5, 2)
# points[:, None, :] => (5, 1, 2)
# points[None, :, :] => (1, 5, 2)
# diffs = (5, 1, 2) - (1, 5, 2)
    # element-by-element subtraction occurs across every combination of rows and columns.
    # The maximum size along each axis determines the final layout:
    # max(5, 1) = 5
    # max(1, 5) = 5
    # max(2, 2) = 2
    # final result (5, 5, 2)

distances = np.sqrt(np.sum(diffs ** 2, axis=-1))
# diffs ** 2: Squares every single number in our 5×5×2 cube.
# np.sum(..., axis=-1) : Adds the squared values together along the very last axis (axis=-1)
# axis=-1 means "the last axis"
# In our (5, 5, 2) array, the last axis is the "coordinate axis" (X and Y).
# Summing along it squashes the 2 into a single number, leaving us with shape (5, 5).