import pandas as pd
import numpy as np

# we'll define a function that makes a dataframe
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)
#explain this
#try this
#make a class

# concatenation
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pdc = pd.concat([ser1, ser2])



