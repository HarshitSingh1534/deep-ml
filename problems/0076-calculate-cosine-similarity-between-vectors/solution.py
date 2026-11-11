import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    a=np.linalg.norm(v1)
    b=np.linalg.norm(v2)
    if not a or not b or v1.size==0 or v2.size==0 or v1.shape!=v2.shape:
        return 
    return np.dot(v1,v2)/(a*b)
    