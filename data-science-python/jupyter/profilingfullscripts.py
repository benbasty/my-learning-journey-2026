def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total

# The result is a table that indicates, in order of total time on each function call,
# where the execution is spending the most time.