# Generate a (100, 4) normal array. Standardize each column to mean 0 and standard deviation 1 without a loop.
import numpy as np
arr = np.random.randn(size=(100,4))
col_means = arr.mean(axis=0, keepdims=True)
col_stdts = arr.std(axis = 0, keepdims=True)

standardized = (arr - col_means) / col_stdts

# calculate the average(mean) 0 => arr.mean((axis = 0))
# calculate the standard deviation 1 => arr.std((axis=0))
# keepDims = true => keeps the dimension! we get the shape (1, 4) instead of (4,)
