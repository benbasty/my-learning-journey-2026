# One of the strengths of NumPy is that it allows us
# to perform quick element-wise operations,
# both with basic arithmetic and with more complicated operations

# Pandas inherits much of this functionality from NumPy,
# and the ufuncs are key to this.

# for unary operations like negation and trigonometric functions,
# these ufuncs will preserve index and column labels in the output,
# and for binary operations such as addition and multiplication,

# Pandas will automatically align indices when passing the objects to the ufunc.

# Ufuncs: Index Preservation

import pandas as pd
import numpy as np

rng = np.random.default_rng(42)
ser = pd.Series(rng.integers(0, 10, 4))
df = pd.DataFrame(rng.integers(0, 10, (3,4)), columns=['A', 'B', 'C', 'D'])
nes = np.exp(ser)
nps = np.sin(df * np.pi / 4)

# Ufuncs: Index Alignment
    # Index Alignment in Series
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 39538223, 'Texas': 29145505,
                        'Florida': 21538187}, name='population')
ap = population / area

aiup = area.index.union(population.index)

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
AB = A + B

AB2 = A.add(B, fill_value=0)

# Index Alignment in DataFrames

C = pd.DataFrame(rng.integers(0, 20, (2, 2)), columns=['a', 'b'])
D = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=['b', 'a', 'c'])

CD = C + D

CD2 = C.add(D, fill_value=C.values.mean())

# Ufuncs: Operations Between DataFrames and Series

E = rng.integers(10, size=(3, 4))

E2 = E - E[0]