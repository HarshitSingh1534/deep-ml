import numpy as np

def sigmoid(logits):
	return 1/(1 + np.e ** (-logits))

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	# Your code here
	X=np.insert(X,0,1,1)
	coeff=np.zeros(X.shape[1]).reshape(-1,1)
	coeff[0,0]=0
	losses=[]
	for _ in range(iterations):
		ypred=sigmoid(np.dot(X,coeff))
		L=-np.dot(y,np.log(ypred.flatten()))
		L-=np.dot(1-y,np.log((1-ypred).flatten()))
		coeff=coeff-learning_rate*(np.dot(X.T,ypred-y.reshape(-1,1)))
		losses.append(L)
	return np.round(coeff.flatten(),4),np.round(losses,4)