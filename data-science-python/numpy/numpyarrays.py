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
dx3 = "x3 ndim: ", x3.ndim
shx3 = "x3 shape: ", x3.shape
six3 = "x3 size: ", x3.size
dtx3 = "x3 type: ", x3.dtype




# indexing of arrays: getting and setting the values of individual array elements

ix1 = x1[0] #x1 array first index
nix1 = x1[-1] # x1 array negative index
ix2 = x2[0, 0] #x2 array first index
x2[0, 0] = 10 #modify x2 array's first index value
# unlike Python lists, NumPy arrays have a fixed type
# if you attempt to insert a floating-point value into an integer array,
# the value will be silently truncated:  x1[0] = 3.14159 => x1[0] = 3


# slicing of arrays: getting and setting smaller subarrays within a larger array
# The NumPy slicing syntax follows that of the standard Python list x[start:stop:step]
# if value is unspecified, they default to the values start=0, stop=<size of dimension>, step=1.
x4 = [3, 4, 5, 6, 7, 8, 9]
ax4 = 'x4 first three elements', x4[:3]
bx4 = 'x4 elements after index 3', x4[3:]
cx4 = x4[1:4] # x4 middle subarray
dx4 = x4[::2] # every second element of x4
ex4 = x4[1::2] # every second element, starting at index 1 of x4
# when the step value is negative, the defaults for start and stop are swapped.
fx4 = x4[::-1] # all elements, reversed
ex4 = x4[4::-2] # every second element from index 4, reversed
# Multidimensional Subarrays slicing
# Multidimensional slices work in the same way, with multiple slices separated by commas.
bx2 = x2[:2, :3] #first two rows and first 3 columns
cx2 = x2[:2, ::3] #first 3 rows annd every third columns
dx2 = x2[::-1, ::-1] #all rows and columns reversed
# we can access single rows or columns of an array by
# combining indexing and slicing, using an empty slice marked by a single colon (:)
fx2 = x2[:, 0] # first column of x2
gx2 = x2[0, :] # first row of x2
# in case of row access, the empty slice can be omitted
hx2 = x2[0] # equivalent to x2[0, :]
# subarrays as no copy views: we can access and process pieces of datasets without
# the need to copy the underlying data buffer.
#creating copies of arrays
# it’s sometimes useful to instead explicitly copy the data within an array or a subarray
# x2[:2, :2].copy() # then when we modify the arrayy the original is untouched


# reshaping of arrays: changing the shape of a given array
# reshaping arrays can be done with the reshape method.
# put the numbers 1 through 9 in a grid
grid = np.arrange(1, 10).reshape(3, 3)
# the size of the initial array must match the size of the reshaped array
# the reshape method will return a no-copy view of the initial array.
# converting a one-dimensional array into a two-dimensional row
x = np.array([1, 2, 3]) # Initialize the 1D Array
rx = x.reshape((1, 3)) #Reshape into a Matrix Row #1 row, 3 columns
cx = x.reshape((3, 1)) #Reshape into a Matrix column #3 rows, 1 column
# A convenient shorthand for this is to use np.newaxis in the slicing syntax
rnx = x[np.newaxis, :] # row vector via newaxis
cnx = x[:, np.newaxis] # column vector via newaxis
# If you hate typing reshape all the time, you can use NumPy's np.newaxis shortcut
# to inject the missing dimension on the fly


# joining and splitting arrays: combining multiple arrays into one, and splitting one array into many
# concatenation or joining two arrays together is done with np.concatenate, np.vstack, and np.hstack. np.concatenate

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate([a, b])
# you can as well concatenate more than 2 arrays
# and also can be used for 2-dimentional array
grid2 = np.array([[1,2,3],
                  [4,5,6]])
# concatenate along the first axis
allgrids2 = np.concatenate([grid2, grid2])

# concatenate along the second axis (zero-indexed)
allgrid3 = np.concatenate([grid2, grid2], axis=1)

# For working with arrays of mixed dimensions, it can be clearer to use
# the np.vstack (vertical stack) and np.hstack (horizontal stack) functions
#vertically stacking the array
vg = np.vstack([x, grid2])

#horizontally stacking the array
y = np.array([[99],
              [99]])
hg = np.hstack([grid2, y])
# for higher-dimensional arrays, np.dstack will stack arrays along the third axis.

# splitting arrays
# The opposite of concatenation is splitting, implemented by the functions
# np.split, np.hsplit, and np.vsplit.

sp = [1, 2, 3, 99, 99, 3, 2, 1]
sp1, sp2, sp3 = np.split(sp, (3, 5))
# N split points leads to N + 1 subarrays.
# The related functions np.hsplit and np.vsplit are similar

grid3 = np.arrange(16).reshape((4,4))
upper, lower = np.vsplit(grid3, [2])
left, right = np.hsplit(grid3, [2])
# Similarly, for higher-dimensional arrays, np.dsplit will split arrays along the third axis.