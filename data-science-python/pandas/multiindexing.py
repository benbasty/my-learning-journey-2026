# hierarchical indexing is also known as multi-indexing
# to incorporate multiple index levels within a single index

import pandas as pd
import numpy as np

index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020),
         ('Texas', 2010), ('Texas', 2020)]

populations = [37253956, 39538223,
               19378102, 20201249,
               25145561, 29145505]

pop = pd.Series(populations, index=index)

# We can create a multi- index from the tuples as follows
index2 = pd.MultiIndex.from_tuples(index)
pop2 = pop.reindex(index2)

pop2_df = pop2.unstack() # The unstack method will quickly convert a multiply indexed Series into a conventionally indexed
pop2_st = pop2_df.stack() # the stack method provides the opposite operation

# Methods of Multiindex creation

df = pd.DataFrame(np.random.rand(4,2), index =[['a','a','b','b'],[1,2,1,2]], columns=['data1', 'data2'])

# The work of creating the MultiIndex is done in the background.

# Explicit MultiIndex Constructors

    # For more flexibility in how the index is constructed, you can instead use the constructor methods available in the pd.MultiIndex class.
dfmfa = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
    # from a list of tuples giving the multiple index values of each point
dfmft = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
    # from a Cartesian product of single indices
dfmfp = pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
    # passing levels (a list of lists containing available index values
    # for each level) and codes (a list of lists that reference these labels)
dfmlc = pd.MultiIndex(levels=[['a', 'b'], [1, 2]], codes=[[0, 0, 1, 1], [0, 1, 0, 1]])

    # MultiIndex Level Names
    # Sometimes it's convenient to name multiindex levels
pop2.index.names = ['state', 'year']

    # MultiIndex For Columns
    # just as the rows can have multiple levels of indices,
    # the columns can have multiple levels as well.

# hierarchical indices and columns
index6 = pd.MultiIndex.from_product([[2013, 2014], [1,2]],
                                   names=['year','visit'])
columns6 = pd.MultiIndex.from_product([['Bob', 'Guido','Sue'],['HR', 'Temp']],
                                      names=['subject','type'])

# mock some data
data6 = np.round(np.random.randn(4, 6), 1)
data6[:, ::2] *= 10
data6 += 37

# create the DataFrame
health_data = pd.DataFrame(data6, index=index6, columns=columns6)


# Indexing and Slicing a MultiIndex

    # Multiply Indexed Series

        #we can access pop2's single elements by indexing with multiple terms:
pop2ca = pop2['California', 2010]
        #partial slicibg is also supported

    # Multiply Indexed DataFrames
hdgh = health_data['Guido', 'HR']

# Rearranging Multi-Indexes

    # Sorted and Unsorted Indices
    # you can't perform multiindex slicing operations if the index is not sorted
    # you need sort data first. data = data.sort_index(), then u can data['a':'b']

    # Stacking and Unstacking Indices
    # it is possible to convert a dataset from a stacked multi-index to a simple 
    # two-dimensional representation, optionally specifying the level to use:
pop2.unstack(level=0)
pop2.unstack(level=1)
pop2.unstack.stack()

    # Index Setting and Resetting
pop_flat = pop2.reset_index(name='population')
# we can build a multiindex from the column values
# by using set_index method which returns a multiply indexed DataFrame
pfsi = pop_flat.set_index(['state','year'])