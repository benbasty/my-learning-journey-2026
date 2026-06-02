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