import numpy as np
from sklearn.metrics import recall_score
def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    return recall_score(y_true,y_pred)
