import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    n,m=len(a),len(a[0])
    if (n*m)!=(new_shape[0]*new_shape[1]):
        return []
    output=[[0]*new_shape[1] for _ in range(new_shape[0])]
    count=0
    for i in range(n):
        for j in range(m):
            output[count//new_shape[1]][count%new_shape[1]]=a[i][j]
            count+=1
    return output