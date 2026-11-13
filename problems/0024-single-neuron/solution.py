import math
import numpy as np
def sigmoid(x):
    return 1/(1+np.e**(-x))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    features=np.asarray(features)
    labels=np.asarray(labels)
    logits=np.dot(features,weights).reshape(-1) + bias
    probabilities=sigmoid(logits)
    mse=(1/labels.shape[0])*np.sum((probabilities-labels)**2)
    return np.round(probabilities,4), np.round(mse,4)