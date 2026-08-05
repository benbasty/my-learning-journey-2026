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