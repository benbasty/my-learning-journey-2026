# effective data driven science and computation requires understanding how data is stored and manipulated
# in programming languages such as C or Java, the data types of each variable are explicitly declared,
# while in Python the types are dynamically inferred.
# in Python we can assign any kind of data to any variables

# This sort of flexibility is what makes Python convenient and easy to use.
# Understanding how this works is important to learning to analyze data efficiently and effectively with Python.
# Python variables are more than just their values;
# they also contain extra information about the type of the value.

# a python integer is more than just an integer
# the standard python implementation is written in C
# every python object is cleverly disguised C structure.
# which contains not only its value but other types of informations as well.
# there is some overhead involved in storing an integer in Python
# PyObject_HEAD is the part of the structure containing the reference count, type code, size and digit
# A Python integer is a pointer to a position in memory containing all the Python object information,
# including the bytes that contain the integer value.
# This extra information in the Python integer structure is what allows Python to be coded so freely and dynamically.

# a python list is more than just a list
# a list is a data structure that holds many objects

# lets create a list of integers
L = list(range(10))
print(L)
print(type(L[0]))

# lets create a list of strings
L2 = [str(c) for c in L]
print(L2)
print(type(L[0]))

# with python we can create heterogenous lists
L3 = [True, "2", 3.0, 4]
print(type(item) for item in L3)

# to allow such flexibility, each item in the list must contain
# its own type, reference count, and other information.
# each item is a complete Python object.

