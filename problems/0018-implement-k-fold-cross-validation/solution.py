import numpy as np
from typing import List, Tuple
from sklearn.model_selection import KFold

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    X=np.arange(start=0, stop=n_samples, step=1).tolist()
    if shuffle:
        np.random.shuffle(X)
    idx=(n_samples//k)+(n_samples%k)
    ans=[]
    ans.append((X[idx:],X[:idx]))
    gap=n_samples//k
    for i in range(idx,n_samples,gap):
        ans.append((X[:i]+X[i+gap:],X[i:i+gap]))
    return ans
    # folds=KFold(n_splits=k)
    # final=list(folds.split(X))
    # return [(X[train],X[test]) for train,test in final]

