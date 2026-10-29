
import numpy as np
def r_squared(y_true, y_pred):
	# Write your code here

	r2=1-(np.sum((y_true-y_pred)**2)/np.sum((y_true-y_true.mean())**2))

	return r2
