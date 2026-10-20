import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	Sscaler=StandardScaler()
	Mscaler=MinMaxScaler()
	standardized_data=Sscaler.fit_transform(data)
	normalized_data=Mscaler.fit_transform(data)
	return standardized_data, normalized_data