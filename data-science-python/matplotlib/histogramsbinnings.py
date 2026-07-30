import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
rng = np.random.default_rng(1701)
data = rng.normal(size=1000)
phd = plt.hist(data);
phds = plt.hist(data, bins=30, density=True, alpha=0.5, 
                histtype='stepfilled', color='steelblue', 
                edgecolor='none');