
import numpy as np
from collections import Counter
def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	count=Counter(y)
	sub=0
	for i in count.keys():
		sub+=(count[i]/len(y))**2
	val=1-(sub)
	return round(val,3)