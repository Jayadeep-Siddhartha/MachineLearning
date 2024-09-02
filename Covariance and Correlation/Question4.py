import numpy as np

# Create an MXN matrix
M = 3  # Number of features
N = 5  # Number of samples
feature_matrix = 10 * np.random.rand(M, N)

# Compute the covariance matrix
covariance_matrix = 10 * np.cov(feature_matrix)

# Compute the correlation matrix
correlation_matrix = 10 * np.corrcoef(feature_matrix)

print("Covariance Matrix:\n", covariance_matrix)
print("Correlation Matrix:\n", correlation_matrix)