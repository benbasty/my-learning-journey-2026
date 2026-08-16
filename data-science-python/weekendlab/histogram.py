import numpy as np
#random_clicks = np.random.randint(0, 5, size=20)
random_clicks = np.array([0, 3, 4, 4, 2, 0, 0, 2, 1, 2, 4, 2, 3, 0, 0, 2, 2, 0, 3, 4])
hist = np.zeros(5, dtype=int)
np.add.at(hist, random_clicks, 1)
print(hist)