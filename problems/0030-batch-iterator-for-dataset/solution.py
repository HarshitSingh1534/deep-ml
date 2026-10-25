import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	batches=[]
	i=0
	flag=False
	if y is not None:
		flag=True
	while i+batch_size<X.shape[0]:
		if flag:
			batches.append([X[i:i+batch_size,:],y[i:i+batch_size]])
		else:
			batches.append(X[i:i+batch_size,:])
		i=i+batch_size
	# if X.shape[0]%batch_size!=0:
	if flag:
		batches.append([X[i:,:],y[i:]])
	else:
		batches.append(X[i:,:])
	return batches
