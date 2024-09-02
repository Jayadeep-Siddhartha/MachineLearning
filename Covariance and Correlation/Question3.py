import numpy as np

# Create two 1XM vectors
N = 5
vector1 = 10 * np.random.rand(N)
vector2 = 10 * np.random.rand(N)

# Compute the covariance
correlation = np.corrcoef(vector1, vector2)[0, 1]

print("Covariance:", correlation)