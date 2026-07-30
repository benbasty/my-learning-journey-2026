# Another used plot type is the simple scatter plot,
# a close cousin of the line plot.
# Instead of points being joined by line segments,
# here the points are represented
# with a dot, circle, or other shape.

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot('x', 'y', 'o', color='black')
rng = np.random.default_rng(0)

for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<','>', 's', 'd']:
    plt.plot(rng.random(2), rng.random(2), marker, color='black', 
             label="marker='{0}'".format(marker))
    plt.legend(numpoints=1, fontsize=13)
    plt.xlim(0, 1.8);

plt.scatter(x, y, marker='o');
#Scatter Plots with plt.scatter

