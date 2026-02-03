import numpy as np

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Mean:", np.mean(data))
print("Row-wise mean:", np.mean(data, axis=1))
print("Column-wise mean:", np.mean(data, axis=0))
print("Max:", np.max(data))
print("Standard Deviation:", np.std(data))
