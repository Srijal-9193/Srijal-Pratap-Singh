# Assignment 3: StandardScaler Example

from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([
    [10, 200],
    [20, 300],
    [30, 400]
])

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Original Data:\n", X)
print("\nScaled Data:\n", X_scaled)