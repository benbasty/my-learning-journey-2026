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

# Series objects

# we can construct a series using an entity as a list or NumPy array

import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
dvalues = data.values
dindex = data.index
d1 = data[1]
d13 = data[1:3]
data2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
db2 = data2['b']
data3 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
d35 = data3[5]

population_dict = {'California': 39538223, 'Texas':29145505, 'Florida': 21538187, 'New York': 20201249, 'Pennsylvania': 13002700}
population = pd.Series(population_dict)
pc = population['California']
pcf = population['California':'Florida']

newArLi = pd.Series([2, 4, 6])
newArLi2 = pd.Series(5, index=[100, 200, 300])
newDict = pd.Series({2:'a', 1:'b', 3:'c'})


# the index can be explicitly set to control the order or the subset of keys used

newDict2 = pd.Series({2:'a', 1:'b', 3:'c'}, index=[1, 2])
#since we only mentionned 2 index, we only get 2 elements and their equivalent values.

# DATAFRAME OBJECT
# Like the Series object discussed in the previous section,
# the DataFrame can be thought of either as a generalization of a NumPy array, 
# or as a specialization of a Python dictionary.

# If a Series is an analog of a one-dimensional array with explicit indices, 
# a DataFrame is an analog of a two-dimensional array with explicit row and column indices.

area_dict = {'California': 423967, 'Texas': 695662, 'Florida': 170312,
                'New York': 141297, 'Pennsylvania': 119280}

area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area': area})

statesid = states.index
states['area']

# Constructing DataFrame Objects from a single Series object
ap = pd.DataFrame(population, columns=['population'])

# Constructing DataFrame Objects from a list of dicts
data4 = [{'a': i, 'b': 2 * i} for i in range(3)]
dd4 = pd.DataFrame(data)

# Constructing DataFrame Objects from a dictionnary of Series Objects
st = pd.DataFrame({'population':population, 'area': area})

# Constructing DataFrame Objects From a two-dimensional Numpy array
ci = pd.DataFrame(np.random.rand(3,2),
                  columns=['foo','bar'],
                  index=['a','b','c'])

# Constructing DataFrame Objects From a NumPy structured array
A = np.zeros(3, dtype=[('A','i8'), ('B', 'f8')])
AD = pd.DataFrame(A)

# PANDAS INDEX OBJECT

# The Index object is either as an immutable array or as an ordered set
# (technically a multiset, as Index objects may contain repeated values)

ind = pd.Index([2, 3, 5, 7, 11])
i1 = ind[1]
i02 = ind[::2]
ssnd = print(ind.size, ind.shape, ind.ndim, ind.dtype)

#index does not support mutable operations

# Index object as ordered set
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

# Pandas can help facilitate your operations such as
# joins accross datasets
# the many conventions that the Index Object follows such as
# unions, intersections, differences and others can be computed in the same way

inter = indA.intersection(indB) #returns a new set of index common to the index objects
unio = indA.union(indB) #form the union of two index objects
symm = indA.symmetric_difference(indB) #compute the symmetric difference of two Index objects

