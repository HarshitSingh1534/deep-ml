import numpy as np
def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp=np.sum((y_true==1) & (y_pred==1))
	pp=np.sum(y_pred==1)
	ap=np.sum(y_true==1)
	pre=tp/pp
	rec=tp/ap
	return np.round((1+beta**2)*pre*rec/((beta**2)*pre + rec),3)
