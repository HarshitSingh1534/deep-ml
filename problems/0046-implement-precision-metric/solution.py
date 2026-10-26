import numpy as np
from sklearn.metrics import precision_score
def precision(y_true, y_pred):
	# Your code here
	return precision_score(y_true,y_pred)
