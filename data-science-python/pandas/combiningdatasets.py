import pandas as pd
import numpy as np

# we'll define a function that makes a dataframe
# a quick shortcut to build a pandas DataFrame (a 2D table like a spreadsheet or SQL table)
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)
# lets make an example of a dataframe
mdf = make_df('ABC', range(3))

#we'll create a quick class that allows to display multiple dataframes side by side
# we use the special method _repr_html to implement its rich object display
# it's The Jupyter Magic Method

class display(object):
    """Display multiple DataFrames side by side in Jupyter."""
    template = """<div style="float: left; padding:10px;">
    <p style='font-family:"Courier New", Courier,
    monospace'>{0}{1}"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        try:
            # Build the HTML string
            html_parts = []
            for a in self.args:
                # Safely get the HTML representation of each object
                html_parts.append(self.template.format("", a._repr_html_()))
            return '\n'.join(html_parts)
        except Exception as e:
            # If it crashes, return an HTML paragraph showing the exact error!
            return f"<p style='color:red;'>ERROR in display: {repr(e)}</p>"

    def __repr__(self):
        # This is for standard Python terminals.
        # It will show what objects are inside, instead of a memory address.
        return f"<display object containing {len(self.args)} items: {[type(a).__name__ for a in self.args]}>"


#concatenation of numpy arrays

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
npcxyz = np.concatenate([x, y, z])

# concatenation with pd.concat

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pdc = pd.concat([ser1, ser2])

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
# dspdfs = display('df1', 'df2', 'pd.concat([df1, df2])')
dspdfs = display(df1, df2, pd.concat([df1, df2]))

#duplicate indices

x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index # make indices match
dspxy = display('x', 'y', 'pd.concat([x, y])')

