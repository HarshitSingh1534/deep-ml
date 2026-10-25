import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    # Your code here
    n_samples=X.shape[0]
    sub_size=n_samples
    if not replacements:
        sub_size=n_samples//2
    ans=[]
    for _ in range(n_subsets):
        idx=np.random.choice(np.arange(X.shape[0]),sub_size,replace=replacements)
        ans.append((X[idx,:],y[idx]))
    return ans