def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    b=-matrix[0][0]-matrix[1][1]
    c=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    d = b**2 - 4*c
    lam1=(-b+(d**0.5))/2
    lam2=(-b-(d**0.5))/2

    return [lam1,lam2]