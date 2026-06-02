# Fixed-type NumPy-style arrays are much more efficient for storing and manipulating data.
# we can store data in efficient, fixed-type data buffers.
# The built-in array module can be used to create dense arrays of a uniform type

import array
import numpy as np
L = list(range(10))
A = array.array('i', L)
# 'i' is a type code indicating the contents are integers.

# creating arrays from python lists
L2 = list(range(5))
A2 = np.array(L2)

# unlike Python lists, NumPy arrays can only contain data of the same type.
A3 = np.array([2.34, 1, 2, 3])

# unlike Python lists, which are always one-dimensional sequences, NumPy arrays can be multidimensional.
A4 = np.array([range(i, i+3) for i in [2, 4, 6]])