import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X=np.array(X)
	y=np.array(y)
	W=np.dot(np.linalg.pinv(np.dot(X.T,X)),np.dot(X.T,y))
	return np.round(W,4)