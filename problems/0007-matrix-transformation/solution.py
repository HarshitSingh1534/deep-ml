import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A=np.asarray(A)
    T=np.asarray(T)
    S=np.asarray(S)
    t=np.linalg.det(T)
    s=np.linalg.det(S)
    if t==0 or s==0:
        return -1
    Tinv=np.linalg.inv(T)
    transformed_matrix=(Tinv @ A) @ S
    return transformed_matrix