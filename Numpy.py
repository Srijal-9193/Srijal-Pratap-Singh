# Numpy Array Operations

import numpy as np

# Create a NumPy array of 10 numbers
arr = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8,])

# Find dimension and shape
print("Dimension:", arr.ndim)
print("Shape:", arr.shape)

# Print elements greater than 5
print("Elements greater than 5:")
print(arr[arr > 5])
