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

# Choosing Elements for the Legend #365 chap 29

# Legend for Size of Pointsv

# Multiple Legends

