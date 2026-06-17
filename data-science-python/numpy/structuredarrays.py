import numpy as np

name = ['Alice', 'Anna', 'Bob', 'Cathy', 'Doug']
age = [25, 34, 36, 38, 28]
weight = [55.0, 85.5, 68.0, 61.5, 65.5]

# We can create a structured array using a compound data type specification
# this will also show that the arrays are related

# an empty container been created
data = np.zeros(5, dtype={'names': ('name', 'age', 'weight'),
                          'formats': ('U10', 'i4', 'f8')})
print(data.dtype)

# 'U10' => “Unicode string of maximum length 10,”
# 'i4' => “4-byte (i.e., 32-bit) integer,”
# 'f8' => “8-byte (i.e., 64-bit) float.”

# lets fill the array with our lists of values
data['name'] = name
data['age'] = age
data['weight'] = weight

print(data)

# For clarity, numerical types can be specified using Python types or NumPy dtypes instead

#instead of U10 => np.str_
#instead of i4 => int
#instead of f8 => np.float32

np.dtype({'names':('name', 'age', 'weight'),
          'formats':((np.str_, 10), int, np.float32)})

# RECORD ARRAYS with a Twist

# np.recarray

# they are almost identical to the structured arrays just described, but with one additional feature: fields can be accessed as attributes rather than as dictionary keys.

print(data['age'])
data_rec = data.view(np.recarray)
print(data_rec.age)

#If we view our data as a record array instead, we can access this with slightly fewer keystrokes