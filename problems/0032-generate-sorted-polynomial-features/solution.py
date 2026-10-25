
import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    X = np.asarray(X, dtype=float)
    n_samples, n_features = X.shape

    features = [np.ones(n_samples)]

    for d in range(1, degree + 1):
        for combo in combinations_with_replacement(range(n_features), d):
            term = np.prod(X[:, combo], axis=1)
            features.append(term)

    result = np.column_stack(features)
    return np.sort(result, axis=1)
