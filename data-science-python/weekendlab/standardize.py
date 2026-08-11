# Generate a (100, 4) normal array. Standardize each column to mean 0 and standard deviation 1 without a loop.
import numpy as np

arr = np.random.normal(size=(100,4))
stdrd_arr = (arr - arr.mean(axis=0)) / arr.std(axis=0)
