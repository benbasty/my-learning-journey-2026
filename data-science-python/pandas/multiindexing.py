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
