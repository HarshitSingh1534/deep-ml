import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

	# Sscaler=StandardScaler()
	# Mscaler=MinMaxScaler()
	# standardized_data=Sscaler.fit_transform(data)
	# normalized_data=Mscaler.fit_transform(data)
	mean=np.mean(data, axis=0)
	std=np.std(data,axis=0)
	maxi=np.max(data, axis=0)
	mini=np.min(data,axis=0)
	standardized_data=np.round((data-mean)/std,4)
	normalized_data=(data-mini)/(maxi-mini)
	return standardized_data, normalized_data