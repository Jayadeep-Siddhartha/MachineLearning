import numpy as np

# Create a 1XN vector
N = 5
feature_vector = 10 * np.random.rand(N)

# Compute the mean
mean = np.mean(feature_vector)

# Compute the variance
variance = np.var(feature_vector)

print("Mean:", mean)
print("Variance:", variance)