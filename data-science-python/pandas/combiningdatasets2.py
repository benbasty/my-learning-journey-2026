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