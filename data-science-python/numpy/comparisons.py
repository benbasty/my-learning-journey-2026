# comparisons operators as ufuncs
# NumPy also implements comparison operators 
# such as < (less than) and > (greater than) as element-wise ufuncs.

import numpy as np

x = np.array([1, 2, 3, 4, 5])

a = x > 3 # greater thann
b = x < 3 # less than
c = x >= 3 # greater than or equal
d = x <= 3 # less than or equal
e = x != 3 # not equal
f = x == 3 # equal

# we can also do an element-wise comparison of two arrays, and to include compound expressions

g = (2 * x) == (x ** 2)
# **: exponentiation operator

# equivalents ufuncs of comparisons operators


# < np.less
# > np.greater
# == np.equal 
# != np.not_equal
#  <= np.less_equal
#  >= np.greater_equal

# these will also work on arrays of any size and shape.
rng = np.random.default_rng(seed=1701)
y = rng.integers(10, size = (3,4))
h = y < 3

# boolean arrays

# let's count the number of True entries in a Boolean array
i = np.count_nonzero(y < 9)
j = np.sum(y < 6)
k = np.sum(y < 6, axis = 1)

# are there any values greater than 8? 
l = np.any(y > 8)

# are there any values less than zero? 
m = np.any(y < 0)

# are all values less than 10? 
n = np.all(y < 10)

# are all values equal to 6? 
o = np.all(y == 6)

# np.all and np.any can be used along particular axes as well. 

# BOOLEAN OPERATORS
# Python’s bitwise logic operators are needed here but this time with numpy
# &, |, ^, and ~

# & np.bitwise_and
# | np.bitwise_or
# ^ np.bitwise_xor
# ~ np.bitwise_not


# BOOLEAN ARRAYS AS MASKS

# suppose we have y
# and we want an array of all values in the array that are less than 5
p = y < 5
# to select these values from the array, we can simply index on this Boolean array
# this is called MASKING OPERATION
q = y[p]
# this will return a one-dimensional array filled with all the values that meet this condition
# all the values in positions at which the mask array is True.