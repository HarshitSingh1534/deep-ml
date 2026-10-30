
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	if not any(y_true) or not any(y_pred):
		return 0.0
	num=2*np.sum((y_true==1) & (y_pred==1))
	den=np.sum((y_true==1)) + np.sum((y_pred==1))
	res=num/den
	return np.round(res, 3)
