# this chapter covers algorithms related to sortinng values in NumPy arrays
# frequently mentionned algorithms topis:
# insertion sorts, selection sorts, merge sorts, quick sorts, bubble sorts ....
# all serve to accomplish a similar task: sorting the values in a list or array

# python built-in functions and methods for sorting lists:
# sorted and sort

# the sorted function takes a list and return a sorted version of it
# the sort method will sort the list in plave

import numpy as np

L = [3, 1, 4, 1, 5, 9, 2, 6]
L1 = sorted(L) #function
L2 = L.sort() #method
P = sorted('pyhton')

# Fast sorthing in Numpy
# np.sort function return a sorted copy of an array 
# and is analogous to pyhton's built in sorted function
# you can also sort and array using the sort method
# the function argsoft returns the argument of the sorted elemets

x = np.array([1,2,4,5,6])
x1 = np.sort(x)
x2 = x.sort()
i = np.argsort(x)

#sorting along rows or columns

# np.sort(X, axis=0)

# np.sort(X, axis=1)

# sometimes we want to find the k smallest values in the array.

# instead of sorting the entire array

# we use np.partition, it takes an array and a number

y = np.array([7, 2, 3, 1, 6, 5, 4])
y1 = np.partition(x, 3)
# it takes the first 3 smallest value in the array, so the array starts with them before showing the houe. 