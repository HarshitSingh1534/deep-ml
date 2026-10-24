import numpy as np
from sklearn.decomposition import PCA
def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """

    mean=data.mean(axis=0)
    std=data.std(axis=0)
    data_norm=(data-mean)/std
    covar=np.cov(data_norm.T)
    evalue,evector=np.linalg.eigh(covar)
    ans=[]
    for i in range(-1,-k-1,-1):
        ans.extend([[j] for j in evector[:,i].tolist()])
    ans=np.array(ans).reshape(data.shape[1],k)

    for i in range(k):
        for j in range(ans.shape[0]):
            if np.abs(ans[j, i]) > 1e-10:
                if ans[j, i] < 0:
                    ans[:, i] *= -1
                break
    return np.round(ans,4)

    # Cant solve with this 
    # p=PCA(n_components=k,svd_solver='full')
    # p.fit(data)
    # return np.round((p.components_).reshape(data.shape[1],k),4)
