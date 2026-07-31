import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
rng = np.random.default_rng(1701)
data = rng.normal(size=1000)
phd = plt.hist(data);
phds = plt.hist(data, bins=30, density=True, alpha=0.5, 
                histtype='stepfilled', color='steelblue', 
                edgecolor='none');

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T

# plt.hist2d: Two-Dimensional Histogram

ph2 = plt.hist2d(x, y, bins=30)
cb = plt.colorbar()
cb.set_label('counts in bin')

# plt.hexbin: Hexagonal Binnings

phhb = plt.hexbin(x, y, gridsize=30)
