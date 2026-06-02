# For larger arrays, it is more efficient to create arrays from scratch
# using routines built into NumPy.

import numpy as np

# Create a length-10 integer array filled with 0s
A0 = np.zeros(10, dtype = int)

# Create a 3x5 floating-point array filled with 1s
A1 = np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with 3.14
A2 = np.full((3, 5), 3.14)

# Create an array filled with a linear sequence
# starting at 0, ending at 20, stepping by 2
A3 = np.arange(0, 20, 2)

# Create an array of five values evenly spaced between 0 and 1
A4 = np.linspace(0, 1, 5)

# Create a 3x3 array of uniformly distributed pseudorandom values between 0 and 1 ???
A5 = np.random.random((3, 3))

# Create a 3x3 array of normally distributed pseudorandom
# values with mean 0 and standard deviation 1
A6 = np.random.normal(0, 1, (3, 3))

# Create a 3x3 array of pseudorandom integers in the interval [0, 10)
A7 = np.random.randint(0, 10, (3,3))

# Create a 3x3 identity matrix
A8 = np.eye(3)

# Create an uninitialized array of three integers; the values will be
# whatever happens to already exist at that memory location
A9 = np.empty(3)

#Numpy standard data types
# NumPy arrays contain values of a single type,
# so it is important to have detailed knowledge of those types and their limitations.

