import numpy as np

# Create the integers 1 through 24, reshape them into (2, 3, 4), and extract the second day, first site, last two hours.

# create integers 1 through 24
numbers = np.arange(1, 25)
# reshape them into (2, 3, 4)
numberscube = numbers.reshape(2, 3, 4) #days, site, hours
#extract second day, first site, last two hours
# -2: with a colon after means "start at the last two items and go to the end"
day_two = numberscube[1][0][-2:]

