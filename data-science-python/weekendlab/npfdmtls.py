# Session 1.1: building arrays
# NumPy arrays are like supercharged Excel grids that Python can do math with at lightning speed.

# Brings the NumPy toolbox into Python so we can use it.
import numpy as np

#Creates a 2d array of a 3-row by 4-column grid of numbers
readings = np.array([
    [18.2, 18.7, 19.1, 19.5],
    [21.0, 20.8, 20.4, 20.1],
    [16.8, 17.2, 17.9, 18.4]
], dtype=np.float64)

# Checks that the grid is exactly the right size.
# Uses an assert statement to double-check our grid is 3x4.
assert readings.shape == (3, 4)
# Prints out that grid (its shape(dimension), size(total counts), and data type(type of number))
print(readings.ndim, readings.size, readings.dtype)
# The zeros tool creates a grid full of 0.0. of 2 rows and 3 columns.
# Arange is like arranging numbers. It counts from 0 up to but not including 12, in steps of 2. Output: [0, 2, 4, 6, 8, 10]
print(np.zeros((2,3)), np.arange(0, 12, 2))
# use np.linspace: Linear Space when you know exactly how many numbers you want, evenly spaced.
# starts at 0.0, ends at 1.0, and gives you exactly 5 numbers evenly spaced between them
print(np.linspace(0.0, 1.0, 5))

# Session 1.2 Index, slice, understanding views

#Pull out a row, a middle section, and the last column
first_site = readings[0] # Grabs the first row with all its columns. first_site is now a 1D array: [18.2, 18.7, 19.1, 19.5]
# The colon : before the comma = "take all rows"
# 1:3 after the comma = "take columns starting at index 1 up to but not including index 3."
middle_hours = readings[:, 1:3] #(row 0, columns 1 & 2),(row 1, columns 1 & 2),(row 3, columns 1 & 2)
# -1 in Python means "the last item."
# -1: with a colon after means "start at the last item and go to the end"
last_hour_column = readings[:, -1:]

# Create a view (window), change it, and PROVE that the original readings array changed too.
window = readings[:, :2] # [:, :2] = "all rows, columns from start (0) up to but not including index 2." So columns 0 and 1.
window[0, 0] = -999.0 # changing the value at row 0, column 0 of window to -999.0
assert readings[0, 0] == -999.0

# Use .copy() to create an independent duplicate and prove changes stay isolated.
readings[0, 0] = 18.2 # We set the first cell back to its original 18.2
safe_window = readings[:, :2].copy() #we use .copy() to make a brand new, independent array with the same values.
safe_window[0, 0] = -1.0
assert readings[0, 0] == 18.2

# Session 1.3 Reshape, concatenate, and split
## Reshape: changing the dimennsion of your data without changing its numbers
## Concatenate: putting arrays together
## Split: cut one array into multiple pieces

# create a list of numbers (a 1d array) from 0 to 23
sequence = np.arange(24)
# reshape the 1d array into a 3d array "cube" representing 2 days, 3 sites, 4 hours
cube = sequence.reshape(2, 3, 4) # days, sites, hours
# Uses an assert statement to double-check if the cube's day 1, site 2 and hour 3 is 23.
assert cube[1, 2, 3] == 23

# create a new day and glue it to the existing cube
#create a 1d array of numbers from 0 to 11, add each item to 100 then reshape into a 3d arrays of 1 day, 3sites, 4 hours
day_3 = (100 + np.arange(12)).reshape(1, 3, 4)
# putting 2 days and day_3 together
(2, 3, 4) + (1, 3, 4) = (3, 3, 4) # we now have 3 days.
three_days = np.concatenate([cube, day_3], axis=0)

# Cut the cube along the "sites" dimension into three separate pieces.
site_a, site_b, site_c = np.split(three_days, [1, 2], axis=1)
# [1, 2]:
    ## Splits BEFORE index 1 (so piece 1 gets indices 0)
    ## Splits BEFORE index 2 (so piece 2 gets indices 1)
    ## Piece 3 gets everything from index 2 onward
# axis=1: Split along the second dimension (the "sites" dimension).
assert site_a.shape == site_b.shape == site_c.shape == (3, 1, 4)

# Feature Creation: Use aggregation functions to build a 2D features table.
    ## np.column_stack(): Takes two 1D arrays and stacks them as columns to make a 2D array.
features = np.column_stack([readings.mean(1), readings.max(1)])
assert features.shape == (3, 2)