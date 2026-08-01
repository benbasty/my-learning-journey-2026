import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import numpy as np

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

ax.legend(loc='upper left', frameon=True)
fig

# Plot legends give meaning to a visualization, assigning meaning to the various plot elements.
# The simplest legend can be created with the plt.legend command

ax.legend(loc='lower center', ncol=2)
fig
# We can use the ncol command to specify the number of columns in the legend


ax.legend(frameon=True, fancybox=True, framealpha=1, shadow=True, borderpad=1)
fig

# we can use a rounded box (fancybox) or add a shadow, 
# change the transparency (alpha value) of the frame, 
# or change the padding around the text

# Choosing Elements for the Legend
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)
pll = plt.legend(lines[:2], ['first', 'second'], frameon=True);

# Multiple Legends

# via the standard legend interface, we can only create a single legend for the entire plot.
# creating a second legend with plt.legend or ax.legend will simply override the first one.
# a better solution is to use Artist (the base class Matplotlib uses for visual attributes)
# then using the lower-level ax.add_artist method to manually add the second artist to the plot

fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)
for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2), 
                     styles[i], color='black')
ax.axis('equal')
# Specify the lines and labels of the first legend
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right')
# Create the second legend and add the artist manually
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right')
ax.add_artist(leg);
