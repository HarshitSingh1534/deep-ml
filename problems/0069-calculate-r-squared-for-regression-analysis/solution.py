
import numpy as np
from sklearn.metrics import r2_score
def r_squared(y_true, y_pred):
	# Write your code here
	return r2_score(y_true,y_pred)
