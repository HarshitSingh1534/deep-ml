import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
	# Your code here
	mean=X.mean(axis=-1,keepdims=True)
	std=X.std(axis=-1,keepdims=True)
	x_norm=(X-mean)/std
	return gamma*x_norm + beta