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


# Profiling and Timing Code
# %time: time of execution of a single statement
# %timeit: Time repeated execution of a single statement for more accuracy
# %prun: run code with profiler
# %1prun: run code with the line by line profiler
# %memit: measure the memory use of a single statement
# %mprun: Run code with the line-by-line memory profiler

# %timeit does some clever things under the hood to 
# prevent system calls from interfering with the timing. 