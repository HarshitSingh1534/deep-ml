import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    if method=='batch':
        batch_size=X.shape[0]
    
    for _ in range(n_epochs):
        for i in range(0,X.shape[0],batch_size):
            inputs=(X[i:i+batch_size])
            target=(y[i:i+batch_size])
            diff_term=-2*(np.dot(inputs.T,target))+2*(np.dot(np.dot(inputs.T,inputs),weights))
            diff_term/=batch_size
            weights=weights-(learning_rate*diff_term)
    return weights

        
