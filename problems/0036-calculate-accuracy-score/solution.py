import numpy as np
from sklearn.metrics import accuracy_score as ac

def accuracy_score(y_true, y_pred):
	# Your code here
	return np.sum(y_pred==y_true)/y_true.shape[0]