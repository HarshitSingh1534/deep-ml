import numpy as np
import pandas as pd

def to_categorical(x, n_col=None):
	# Your code here
	if not n_col:
		n_col=len(set(x.tolist()))
	arr=[]
	for i in range(x.shape[0]):
		curr=[0]*n_col
		curr[x[i]]=1
		arr.append(curr)
	return np.array(arr,dtype='float')
