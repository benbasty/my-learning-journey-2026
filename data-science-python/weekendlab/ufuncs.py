import numpy as np
# ufuncs stands for Universal functions.
# a ufunc is a lightning-fast, element-wise math robot.

# "Element-wise" means it takes your array, goes to the very first number,
# does a math operation on it, then goes to the second number, does the same operation,
# and so on, until it has processed every single number.

# "Lightning-fast" means it does all of this in super-fast C code (behind the scenes),
# rather than slow Python loops.

# so aa ufunc excute an operation faster and on a larger scale

# they come in two flavors
    # unary ufuncs => Takes one array as input. => operation that only need one set of numbers => square roots, rounding, negations
    # binary ufuncs => Takes two arrays (or one array and a single number) => operation that combine or compare two sets of numbers - multiplication, addition, greater than ...

# example
    # we have two arrays
temperatures = [12.3, 25.6, 27.5]
temps2 = np.array([1.0, 2.0, 3.0])
    # unary functions
# takes each array's element and calculate its sqrt and returns a result
temp_sq_rt = np.sqrt(temperatures)
# other unary functions we can use: np.abs() (absolute value), np.exp() (e^x), np.log() (natural log), np.sin() ...

    # binary functions
# takes each array's elements from the first array and multiply it with each elements from at each corresponding index
temp-mltp = np.multiply(temperatures, temps2)

# broadcastings and methods





