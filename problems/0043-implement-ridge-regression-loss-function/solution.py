import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	loss=(y_true-np.dot(X,w.T))
	squared_loss=(np.dot(loss,loss.T))/X.shape[0]
	ridge_loss=squared_loss+alpha*np.dot(w,w.T)
	return ridge_loss