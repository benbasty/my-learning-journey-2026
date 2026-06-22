# pandas is a newer package built on top of Numpy that provides
# an efficient implementation of a DataFrame
# DataFrames are essentially multidimensional arrays with attached row and column labels
# often with heterogeneous types and/or missing data

# numpy limitations come to light when we need more flexibility
# and when attempting operations that do not map well to element-wise broadcasting
# pandas is built on its Series and DataFrame objects
# and builds on the NumPy array structure and provides efficient access to these sorts of “data munging” tasks that occupy much of a data scientist’s time.

# A Pandas Series is a one-dimensional array of indexed data.

# The Series combines a sequence of values with an explicit sequence of indices, which we can access with the values and index attributes.

# we can change the index with pandas
# but the index need not be an integer, but can consist of values of any desired type. 
# So, if we wish, we can use strings as an index:

# you can think of a Pandas Series a bit like a specialization of a Python dictionary
