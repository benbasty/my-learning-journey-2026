# numpy array can be fast or it can be slow
# the only way to make it fast is to use vectorized operations
# generally implemented through numpy's universal functions
# they can be used to make repeated calculations on array elements much more efficient.

# Ufuncs
# Vectorized operations in NumPy are implemented via ufuncs,
# whose main purpose is to quickly execute repeated operations on values in NumPy arrays.
# we can also operate between two arrays and also multi-dimensional arrays as well

# Ufuncs exist in two flavors: unary ufuncs, which operate on a single input,
# and binary ufuncs, which operate on two inputs.

# Array Arithmetic: addition, subtraction, multiplication, and division

import numpy as np

x = np.arange(5)
print("x      =", x)
print("x + 5  =", x + 5)
print("x - 5  =", x - 5)
print("x * 2  =", x * 2)
print("x / 2  =", x / 2)
print("x // 2 =", x // 2) # floor division

# we also have ufunc for negation, a ** operator for exponentiation, and a % operator for modulus
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

# All of these arithmetic operations are simply convenient wrappers around specific ufuncs built into NumPy. 
# For example, the + operator is a wrapper for the add ufunc

# absolute value
# Just as NumPy understands Python’s built-in arithmetic operators, 
# it also understands Python’s built-in absolute value function

a = np.array([-2, -1, 0, 1, 2])
b = abs(a)
# The corresponding NumPy ufunc is np.absolute or np.abs

# Trigonometric Functions
theta = np.linspace(0, np.pi, 3) # create an array of 3 evenly spaced numbers starting at 0 and ending at \(\pi \)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))


# Inverse trigonometric functions are also available
p = [-1, 0, 1]
print("p         = ", p)
print("arcsin(p) = ", np.arcsin(p))
print("arccos(p) = ", np.arccos(p))
print("arctan(p) = ", np.arctan(p))

#exponents and logarythms
e = [1, 2, 3]
print("e   =", e)
print("e^e =", np.exp(e))
print("2^e =", np.exp2(e))
print("3^e =", np.power(3., e))

# The inverse of the exponentials, the logarithms, are also available.
# The basic np.log gives the natural logarithm;
# As well as the base-2 logarithm or the base-10 logarithm

k = [1, 2, 4, 10]
print("k        =", k)
print("ln(k)    =", np.log(k))
print("log2(k)  =", np.log2(k))
print("log10(k) =", np.log10(k))

# Advanced Ufunc Features

# Specifying Output
# it is sometimes useful to be able to specify the array where the result of the calculation 
# will be stored.

g = np.arange(5)
h = np.empty(5)
gh = np.multiply(g, 10, out=h)
# multiplies every element in the array g by 10 and stores the result in an existing array h

# Aggregations
# For binary ufuncs, aggregations can be computed directly from the object.

# if we’d like to reduce an array with a particular operation, we can use the reduce method of any ufunc. 
# A reduce repeatedly applies a given operation to the elements of an array until only a single result remains.

r = np.arange(1, 6)
ar = np.add.reduce(r)
mr = np.multiply.reduce(r)

# store all intermediate results of the computation: accumulate
cr = np.multiply.accumulate(r)
ccr = np.add.accumulate(r)

# outer products
# any ufunc can compute the output of all pairs of two different inputs using the outer method.
# This allows you, in one line, to do things like create a multiplication table

t = np.arange(1, 6)
tt = np.multiply.outer(t, t)