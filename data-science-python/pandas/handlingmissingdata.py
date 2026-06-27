# to track the presence of missing data in a table or DataFrame.to track the presence of missing data in a table or DataFrame.
# we can use a mask that globally indicates missing values, or choosing a sentinel value that indicates a missing entry.

# In the masking approach, the mask might be an entirely separate Boolean array, or it might involve 
# appropriation of one bit in the data representation to locally indicate the null status of a value.

# In the sentinel approach, the sentinel value could be some data-specific convention, 
# such as indicating a missing integer value with –9999 
# or some rare bit pattern, or it could be a more global convention, 
# such as indicating a missing floating-point value with NaN (Not a Number), 
# a special value that is part of the IEEE floating-point specification.


# Missing Data in Pandas

# None as sentinel value

import numpy as np
import pandas as pd

vals1 = np.array([1, None, 2, 3])
# This dtype=object means that the best common type representation NumPy could infer for the contents of the array is that they are Python objects.

# NaN: Missing Numerical Data
vals2 = np.array([1, np.nan, 3, 4])

# NaN is a bit like a data virus—it infects any other object it touches.
# Regardless of the operation, the result of arithmetic with NaN will be another NaN

# But NumPy does provide NaN-aware versions of aggregations that will ignore these missing values

nsum = np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)

# The main downside of NaN is that it is specifically a floating-point value; there is no equivalent NaN value for integers, strings, or other types.

# NaN and None in Pandas
# Pandas is built to handle NaN and None nearly interchangeably
# np.nan and None will become Nan with Pandas
nnp = pd.Series([1, np.nan, 2, None])

# For types that don’t have an available sentinel value, 
# Pandas automatically typecasts when NA values are present.

# Pandas Nullable Dtypes <NA>

# In early versions of Pandas, NaN and None as sentinel values were the only missing data representations available.
# Pandas later added nullable dtypes, which are distinguished from regular dtypes by capitalization of their names 
# (e.g., pd.Int32 versus np.int32).

ndp = pd.Series([1, np.nan, 2, None, pd.NA], dtype='Int32')

# Operating on Null values

# Pandas treats None, NaN, and NA as essentially interchangeable for indicating missing or null values

# To facilitate this convention, Pandas provides several methods for 
# detecting, removing, and replacing null values in Pandas data structures.

# isnull => Generates a Boolean mask indicating missing values
# notnull => Opposite of isnull
# dropna => Returns a filtered version of the datav
# fillna => Returns a copy of the data with missing values filled or imputed

# Detecting Null Values
data = pd.Series([1, np.nan, 'hello', None])
ddatain = data.isnull()
    # Boolean masks can be used directly as a Series or DataFrame index
ddatann = data[data.notnull()]

# Dropping Null Values
# there are the convenience methods 
# dropna (which removes NA values) 
# and fillna (which fills in NA values).

ddatadn = data.dropna()

# We cannot drop single values from a DataFrame; 
# we can only drop entire rows or columns.

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])

dfdn = df.dropna()
dfda = df.dropna(axis='columns')

# we can also use the the how or thresh parameters, 
# which allow fine control of the number of nulls to allow through.

df[3] = np.nan
dfah = df.dropna(axis='columns', how='all')
dfat = df.dropna(axis='rows', thresh=3)

# Filling Null Values

# Sometimes rather than dropping NA values, you’d like to replace them with a valid value.

data2 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'), dtype='Int32')
data2.fillna(0) # We can fill NA entries with a single value, such as zero
data22 = data2.fillna(method='ffill') # We can specify a forward fill to propagate the previous value forward
data222 = data2.fillna(method='bfill') # we can specify a backward fill to propagate the next values backward









