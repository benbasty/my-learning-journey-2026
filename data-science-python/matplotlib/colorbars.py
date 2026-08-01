import matplotlib.pyplot as plt
# plt.style.use('seaborn-v0_8-whitegrid')
plt.style.use('classic')
import numpy as np

# a colorbar is drawn as a separate axes 
# that can provide a key for the meaning of colors in a plot.

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

plt.imshow(I)
plt.colorbar();

# Customizing Colorbars
plt.imshow(I, cmap='Blues');
plt.imshow(I, cmap='gray');

## Choosing the Colormap

## We should be aware of three different categories of colormaps:

# Sequential colormaps: These are made up of one continuous sequence of colors (e.g., binary or viridis).
# Divergent colormaps: These usually contain two distinct colors, which show positive and negative deviations from a mean (e.g., RdBu or PuOr).
# Qualitative colormaps: these mix colors with no particular sequence (e.g., rainbow or jet).


## Color limits and extensions
# The colorbar itself is simply an instance of plt.Axes
# we can narrow the color limits and indicate the out-of-bounds values 
# with a triangular arrow at the top and bottom by setting the extend property.

# make noise in 1% of the image pixels
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

plt.figure(figsize=(10, 3.5))

plt.subplot(1, 2, 1)
plt.imshow(I, cmap='RdBu')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(I, cmap='RdBu')
plt.colorbar(extend='both')
plt.clim(-1, 1);

## Discrete Colorbars

plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1);

# Handwritten digits

# load images of the digits 0 through 5 and visualize several of them
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)

fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

# project the digits into 2 dimensions using IsoMap
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)

# plot the results
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
            c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
plt.colorbar(ticks=range(6), label='digit value')
plt.clim(-0.5, 5.5)