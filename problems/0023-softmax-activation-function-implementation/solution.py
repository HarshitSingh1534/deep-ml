import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores=np.asarray(scores)
    return np.e**(scores-np.max(scores))/np.sum(np.e**(scores - np.max(scores)))
