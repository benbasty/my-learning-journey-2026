import numpy as np
import time

# Comparison
arr = np.array([5, 10, 15, 20])
grt_arr = np.greater(arr, 12)
print(grt_arr)

# Mix and Match
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
ab_max = np.maximum(a, b)
ab_pow = np.power(a, b)
print(ab_max)
print(ab_pow)

# Speed Test
big = np.arange(1_000_000)

# Time the NumPy ufunc
start_ufunc = time.perf_counter()
res_np = big * 2
end_ufunc = time.perf_counter()

# Time the python list comprehension
start_loop = time.perf_counter()
res_list = [x * 2 for x in big]
end_loop = time.perf_counter()

print(f"NumPy ufunc: {end_ufunc - start_ufunc:.6f} seconds")
print(f"List comprehension: {end_loop - start_loop:.6f} seconds")