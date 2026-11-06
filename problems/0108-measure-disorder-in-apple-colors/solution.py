from collections import Counter
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	count=Counter(apples)
	total=0
	for i in count.keys():
		total+=(count[i]/len(apples))**2
	return 1-total
