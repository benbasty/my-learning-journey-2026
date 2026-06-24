# Data Selection in Series

# Series as Dictionary
import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
db = data['b']
a = 'a' in data
dk = data.keys()
dl = list(data.items())
# series objects can also be modified.
# Just as you can extend a dictionary by assigning it to a new key
# you can extend Series by assigning to a new index value

data2 = data
data2['e'] = 1.25

#Series as One-Dimensional Array

# slicing by explicit index
dac = data['a':'c']
# slicing by implicit integer index
d02 = data[0:2]
# masking
dm = data[(data > 0.3) & (data < 0.8)]
# fancy indexing
dae = data[['a', 'e']]


# Indexers: loc and iloc

# Pandas provides some special indexer attributes that 
# explicitly expose a particular slicing interface to the data in the Series.

data3 = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
dt31 = data3[1]
dt313 = data[1:3]

# the loc attribute allows indexing and slicing that always references the explicit index
dlc1 = data3.loc[1] # focus on the index itself and returns its corresponding index's value
dlc13 = data3.loc[1:3] # returns the corresponding values of index 1 and 3

# The iloc attribute allows indexing and slicing 
# that always references the implicit Python-style index

dil1 = data3.iloc[1] # starts counting the index from 0 and returns the value at index 1
dil13 = data3.iloc[1:3] #returns the values at index 1 and 2 (not 3)


# Data Selection in DataFrames