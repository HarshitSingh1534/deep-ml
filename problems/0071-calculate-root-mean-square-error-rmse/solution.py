
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	if (y_true.size==0 or y_pred.size==0) or (y_true.shape!=y_pred.shape):
		raise ValueError
	rmse_res=np.sqrt(np.sum((y_true-y_pred)**2)/y_true.size)
	return round(rmse_res,3)
