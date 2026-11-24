import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a=np.asarray(a)
    b=np.asarray(b)
    x,y=a.shape
    m,n=b.shape
    if y!=m:
        return -1
    else:
        return a@b