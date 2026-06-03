# data manipulation in Python is the same thing as Numpy array manipulation
# we use numpy array manioulation to access data and subarrays, split, reshape and join them

import numpy as np

# Attributes of array: size, shape, memory consumption, and data types of arrays

rng = np.random.default_rng(seed=1701) #seed for reproductivity
x1 = rng.integers(10, size=6) #one-dimensional array
x2 = rng.integers(10, size=(3,4)) #two-dimensional array
x3 = rng.integers(10, size=(3,4,2)) #three-dimensional array
#attributes include ndim (the number of dimensions), shape (the size of each dimension),
# size (the total size of the array), and dtype (the type of each element):
dx3 = print("x3 ndim: ", x3.ndim)
shx3 = print("x3 shape: ", x3.shape)
six3 = print("x3 size: ", x3.size)
dtx3 = print("x3 type: ", x3.dtype)




# indexing of arrays: getting and setting the values of individual array elements
ax1 = print(x1) #printing x1 array
ix1 = print(x1[0]) #printing x1 array first index
nix1 = print(x1[-1]) # we can also print negative index
ax2 = print(x2) #printing x2 array
ix2 = print(x2[0, 0]) #printing x2 array first index
x2[0, 0] = 10 #we can also modify array's index value
# unlike Python lists, NumPy arrays have a fixed type
# if you attempt to insert a floating-point value into an integer array,
# the value will be silently truncated:  x1[0] = 3.14159 => x1[0] = 3


# slicing of arrays: getting and setting smaller subarrays within a larger array
# The NumPy slicing syntax follows that of the standard Python list x[start:stop:step]
# if value is unspecified, they default to the values start=0, stop=<size of dimension>, step=1.
x4 = [3, 4, 5, 6, 7, 8, 9]
ax4 = print('x4 first three elements', x4[:3])
bx4 = print('x4 elements after index 3', x4[3:])
cx4 = print(x4[1:4]) # middle subarray
dx4 = print(x4[::2]) # every second element
ex4 = print(x4[1::2]) # every second element, starting at index 1
# when the step value is negative, the defaults for start and stop are swapped.
fx4 = print(x4[::-1]) # all elements, reversed
ex4 = print(x4[4::-2]) # every second element from index 4, reversed
# Multidimensional Subarrays slicing













# reshaping of arrays: changing the shape of a given array
# joining and splitting arrays: combining multiple arrays into one, and splitting one array into many