
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	num=np.sum((y_true==1)&(y_pred==1))
	den=np.sum((y_true==1)|(y_pred==1)) 
	result=num/den
	return np.round(result, 3)
