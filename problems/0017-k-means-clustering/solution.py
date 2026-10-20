from sklearn.cluster import KMeans
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	kmeans=KMeans(n_clusters=k,init=initial_centroids,max_iter=max_iterations)
	kmeans.fit(points)
	final_centroids=kmeans.cluster_centers_
	return [tuple(i) for i in final_centroids.tolist()]