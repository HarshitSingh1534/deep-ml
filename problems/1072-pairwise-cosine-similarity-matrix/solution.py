import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    n=len(X)
    output=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            output[i][j]=np.dot(X[i],X[j])/(np.linalg.norm(X[i])*np.linalg.norm(X[j]))
    output=np.where(np.isnan(output),0.0,output)
    return np.round(output,4)