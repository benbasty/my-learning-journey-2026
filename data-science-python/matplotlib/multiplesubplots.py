import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import numpy as np

# plt.axes: Subplots by Hand

# create an inset axes at the top-right corner of another axes
# x and y set to position to 0.65: starting at 65% of the width and 65% of the height of the figure
# x and y extents to 0.2: size of the axes is 20% of the width and 20% of the height of the figure
ax1 = plt.axes()  # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

# The equivalent of this command within the object-oriented interface is fig.add_axes()
# now lets create two vertically stacked axes

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x));

# plt.subplot: Simple Grids of Subplots
# plt.subplot()is used to create a single subplot within a grid.
# this command takes three integer arguments—the number of rows, 
# the number of columns, and the index of the plot to be created in this scheme, 
# which runs from the upper left to the bottom right

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

# The command plt.subplots_adjust can be used to adjust the spacing between these plots.

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
           fontsize=18, ha='center')

# plt.subplots: The Whole Grid in One Go
# this function creates a full grid of subplots in a single line, 
# returning them in a NumPy array. 
# The arguments are the number of rows and number of columns, 
# along with optional keywords sharex and sharey, 
# which allow you to specify the relationships between different axes.

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# we'll create a $2 \times 3$ grid of subplots, 
# where all axes in the same row share their y-axis scale, 
# and all axes in the same column share their x-axis scale

# by specifying sharex and sharey, we've automatically 
# removed inner labels on the grid to make the plot cleaner. 

# axes are in a two-dimensional array, indexed by [row, col]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
fig

# plt.GridSpec: More Complicated Arrangements
# here is a gridspec for a grid of two rows and three columns 
# with some specified width and height space looks like this

grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2]);

# Create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='gray')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='gray')
y_hist.invert_xaxis()