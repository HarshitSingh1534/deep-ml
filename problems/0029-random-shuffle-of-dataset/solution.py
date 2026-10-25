import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	x=np.asarray(X)
	y=np.asarray(y)
	if seed:
		np.random.seed(seed)
	x=np.append(x,y.reshape(-1,1),axis=1)
	np.random.shuffle(x)
	y=(x[:,-1]).reshape(-1)
	x=np.delete(x,-1,axis=1)

	return x,y
	
