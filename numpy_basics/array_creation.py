import numpy as np

# From list
arr1 = np.array([1, 2, 3, 4])
print(arr1)

# Zeros and ones
zeros = np.zeros(5)
ones = np.ones(5)

print(zeros)
print(ones)

# Range
arr_range = np.arange(0, 10, 2)
print(arr_range)
# Linspace
arr_linspace = np.linspace(0, 1, 5)
print(arr_linspace)
# Reshape
arr_reshaped = np.arange(1, 13).reshape(3, 4)
print(arr_reshaped)
# Identity matrix
identity_matrix = np.eye(4)
print(identity_matrix)
# Random numbers
random_arr = np.random.rand(3, 3)
print(random_arr)
# Random integers
random_ints = np.random.randint(1, 10, size=(3, 3))
print(random_ints)
# From existing data
data = [10, 20, 30, 40]
arr_from_data = np.array(data)
print(arr_from_data)