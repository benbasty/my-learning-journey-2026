import pandas as pd
import numpy as np

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding:10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}{1}"""
    def __init__(self, *args):
        self.args = args
    def repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_()) 
                         for a in self.args)
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

# Categories of joins

# One-to-one joins
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake','Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
ddf12 = display('df1', 'df2')
df3 = pd.merge(df1, df2)

# Many-to-One Joins
df4 = pd.DataFrame({'group': ['Accounting',
'Engineering', 'HR'], 'supervisor': ['Carly', 'Guido', 'Steve']})
ddfm34 = display('df3', 'df4', 'pd.merge(df3, df4)')

# Many-to-Many Joins
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets','software', 'math','spreadsheets','organization']})

dmmdf15 = display('df1', 'df5', "pd.merge(df1, df5)")

# Specification of the Merge Key

# The on Keyword
# you can specify the name of the key column using the on keyword, which takes a column name or a list of column names
don = display('df1', 'df2', "pd.merge(df1, df2, on='employee')")

# The left_on and right_on Keywords
# sometimes we may want to merge two datasets with different column names;
# for example, we may have a dataset in which the employee name is labeled as “name” rather than “employee”.
# In this case, we can use the left_on and right_on keywords to specify the two column names

df6 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa','Sue'], 'salary': [70000, 80000, 120000, 90000]})
dlron = display('df1', 'df6', 'pd.merge(df1, df6, left_on="employee", right_on="name")')
# simply means we display employee on the left, and display name on the right

# The left_index and right_index Keywords
    # rather than merging on a column, we would instead like to merge on an index.
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
df12a = display('df1a', 'df2a')

# we can use the index as the key for merging by specifying the left_index and/or right_index flags in pd.merge()
dfliri = display('df1a', 'df2a', "pd.merge(df1a, df2a, left_index=True, right_index=True)")

# Specifying Set Arithmetic for Joins
    # one important to consider in performing a join is to decide the type of set arithmetic used in the join.
    # this usually happens when a value appears in one column, but not in the other
    # inner join when the result contains the intersection of two sets of input (how='inner')
    # an outer join returns a join over the union of the input columns and fills the missings values with NAs (how='outer')
    # the left and right join returns joins over the left and the right entries (how = 'left'), (how= 'right')