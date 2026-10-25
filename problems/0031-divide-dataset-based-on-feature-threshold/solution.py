import numpy as np

def divide_on_feature(X, feature_i, threshold):
	# Your code here
	first=X[X[:,feature_i]>=threshold]
	second=X[X[:,feature_i]<threshold]
	return [first,second]