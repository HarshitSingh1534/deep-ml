
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	if not any(y_true) or not any(y_pred):
		return 0.0
	tp=np.sum((y_true==1) & (y_pred==1))
	fp=np.sum((y_true==0) & (y_pred==1))
	fn=np.sum((y_true==1) & (y_pred==0))
	res=(2*tp)/(2*tp + fp +fn)
	return np.round(res, 3)
