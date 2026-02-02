import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Row
print(arr[1])

# Column
print(arr[:, 1])

# Sub-matrix
print(arr[0:2, 1:3])

