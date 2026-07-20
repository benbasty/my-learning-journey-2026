# Aggregations in Pandas
# we’ll explore aggregations in Pandas,
# from simple operations akin to what we’ve seen on NumPy arrays
# to more sophisticated operations based on the concept of a groupby

import numpy as np
import pandas as pd

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding:10px;">
    <p style='font-family:"Courier New", Courier,monospace'>{0}{1}"""
    def __init__(self, *args):
        self.args = args
    def _repr_html_(self):
        return '\n'.join(self.template.format(a,eval(a)._repr_html_())
                         for a in self.args)
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

# Simple Aggregation in Pandas
# sum, mean, median, min, and max

# for a Pandas Series the aggregates return a single value
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ss = ser.sum()
sm = ser.mean()
df = pd.DataFrame({'A': rng.rand(5), 'B': rng.rand(5)})
dfm = df.mean()
dfma = df.mean(axis='columns') # By specifying the axis argument, you can instead aggregate within each row

# groupby: Split, Apply, Combine

# if we would like to aggregate conditionally on some label or index, we can implement it with the groupby operation
# think split, apply, combine

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'data': range(6)}, columns=['key', 'data'])
dfgb = df1.groupby('key')
dfgbs = df1.groupby('key').sum()

# The GroupBy Object
    # Column indexing: planets.groupby('method')['orbital_period'].median()
    # Iteration over groups:
        # for (method, group) in planets.groupby('method'):
            # print("{0:30s} shape={1}".format(method,group.shape))
    # Dispatch methods
        # planets.groupby('method')['year'].describe().unstack()

# Aggregate, Filter, Transform, Apply
# GroupBy objects have aggregate, filter, transform, and apply methods
# that efficiently implement a variety of useful operations before combining the grouped data.

    # Aggregation: df.groupby('key').aggregate(['min', np.median, max])
    # this method is more powerful, the aggregate method allows for even more flexibility. 
    # It can take a string, a function, or a list thereof, and compute all the aggregates at once. 
    # we can also pass a dictionary mapping column names to operations to be applied on that column
    # df.groupby('key').aggregate({'data1': 'min', 'data2': 'max'})

    # Filtering
        # A filtering operation allows you to drop data based on the group properties.
        # def filter_func(x):
            #return x['data2].std() > 4
        # display('df', "df.groupby('key').std()","df.groupby('key').filter(filter_func)")

    # Transformation
        # While aggregation must return a reduced version of the data, 
        # transformation can return some transformed version of the full data to recombine.
        # def center(x):
            # return x - x.mean()
        # df.groupby('key').transform(center)

    # apply method
        # The apply method lets you apply an arbitrary function to the group results.
        # The function should take a DataFrame and returns either a Pandas object (e.g., DataFrame, Series) or a scalar
        # def norm_by_data2(x):
            # x is a DataFrame of group values
                # x['data1'] /= x['data2'].sum()
                # return x
                # df.groupby('key').apply(norm_by_data2)

# Specifying the Split Key
    # A list, array, series, or index providing the grouping keys
    # A dictionary or series mapping index to group
    # Any Python function
    # A list of valid keys


# Grouping Example







