import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import numpy as np

# Visualizing a Three-Dimensional Function
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black');
plt.contour(X, Y, Z, 20, cmap='RdGy');
# creates an additional axis with labeled color information
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', interpolation='gaussian', aspect='equal')
# plt.imshow offers the interpolation argument 
# to generate a smooth two-dimensional representation of the data
# RdGy (short for Red–Gray) colormap
plt.colorbar();
