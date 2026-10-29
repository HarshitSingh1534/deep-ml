
from collections import Counter
import numpy as np
def confusion_matrix(data):
	# Implement the function here
	y_pred=[]
	y_true=[]
	for i in data:
		y_true.append(i[0])
		y_pred.append(i[1])
	y_true=np.asarray(y_true,dtype='int')
	y_pred=np.asarray(y_pred,dtype='int')
	tp=np.sum((y_true==1) & (y_pred==1))
	tn=np.sum((y_true==0) & (y_pred==0))
	fp=np.sum((y_true==0) & (y_pred==1))
	fn=np.sum((y_true==1) & (y_pred==0))
	return [[tp,fn],[fp,tn]]
