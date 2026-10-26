import numpy as np
from sklearn.metrics import precision_score
def precision(y_true, y_pred):
	# Your code here
	tp=np.sum((y_true==1) & (y_pred==1))
	den=np.sum(y_pred==1)
	if den==0:
		return 0.0
	return tp/den
