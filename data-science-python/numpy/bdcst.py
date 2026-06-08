# broadcasting: a set of rules by which NumPy lets you apply binary operations 
# (e.g., addition, subtraction, multiplication, etc.) 
# between arrays of different sizes and shapes.

import numpy as np
a = np.array([1,6,8])
b = np.array([7,4,3])
c = a + b

# Broadcasting allows these types of binary operations to be performed on arrays of different sizes
d = a + 5

# We can similarly extend this idea to arrays of higher dimension.
# For example add a one-dimensional array to a two-dimensional array

M = np.ones((3, 3))
N = M + a
# here, the one-dimensional array a is stretched, or broadcasted,
# across the second dimension in order to match the shape of M.

# lets broadcast two arrays.

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
e = a + b
# we’ve stretched both a and b to match a common shape, and the result is a two-dimensional array!

# RULES OF BROADCASTING
# 1 If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
# 2 If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
# 3 If in any dimension the sizes disagree and neither is equal to 1, an error is raised.


