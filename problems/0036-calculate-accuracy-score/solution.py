import numpy as np
from sklearn.metrics import accuracy_score as ac

def accuracy_score(y_true, y_pred):
	# Your code here
	return ac(y_true,y_pred)