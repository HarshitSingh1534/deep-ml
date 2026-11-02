import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    # Your code here
    x=np.min(values)
    y=np.max(values)
    values=c+(((values-x)*(d-c))/(y-x))
    return values