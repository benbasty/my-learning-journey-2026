def square(x):
    return x ** 2
for num in range(1,4):
    print(f"{num} squared is {square(num)}")

# %xmode magic function (short for exception mode)
# %xmode takes a single argument, the mode,
# and there are three possibilities: Plain, Context, and Verbose.
# The default is Context, which gives output like that just shown.
# Plain is more compact and gives less information
# Verbose mode adds some extra information,
# including the arguments to any functions that are called