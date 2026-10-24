import numpy as np
from sklearn.cluster import KMeans
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	points=np.asarray(points)
	initial_centroids=np.asarray(initial_centroids,dtype=float)
	for _ in range(max_iterations):
		output_diff=points[:,np.newaxis,:]-initial_centroids[np.newaxis,:,:]
		output_norm=np.linalg.norm(output_diff,axis=2)
		labels=np.argmin(output_norm,axis=1)
		new_centroids=initial_centroids.copy()
		for i in range(k):
			clusters=points[labels==i]
			if len(clusters)>0:
				new_centroids[i]=clusters.mean(axis=0)
		initial_centroids=new_centroids.copy()
	return [tuple(i) for i in np.round(initial_centroids,4).tolist()]