def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n=len(matrix)
    m=len(matrix[0])
    means=[]
    if mode=='column':
        means=[0]*m
        for i in range(n):
            for j in range(m):
                means[j]+=matrix[i][j]
        for i in range(m):
            means[i]/=n
    else:
        means=[0]*n
        for i in range(n):
            for j in range(m):
                means[i]+=matrix[i][j]
        for i in range(n):
            means[i]/=m
    return means