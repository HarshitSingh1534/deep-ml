import numpy as np

def kernel_function(x1, x2):
	# Your code here
	return (x1.reshape(1,-1)@x2.reshape(-1,1)).item()
