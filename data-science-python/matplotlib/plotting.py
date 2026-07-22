#importing Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# the plt interface will be used often

# setting styles
# the plt.style directive is used to choose
# appropriate aesthetic styles for our figures

plt.style.use('classic') # classic Matplotlib style

# display my plots

# Plotting from a script => plt.show
# Plotting from an IPython Shell => %matplotlib
    # ipython works well when you specify Matplotlib mode.
    # To enable this mode, you can use the %matplotlib
        #%matplotlib
        #import matplotlib.pyplot as plt
        #any plt plot command will cause a figure window to open, and further commands can be run to update the plot.
        #to force an update, use plt.draw.
# Plotting from a Jupyter Notebook
    # %matplotlib inline: will lead to static images of your plot embedded in the notebook.
    # %matplotlib notebook: will lead to interactive plots embedded within the notebook.

x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

# Saving Figures to File
fig.savefig('my_figure.png')