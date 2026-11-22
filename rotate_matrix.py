def rotate(self, matrix: list[list[int]]) -> None:
    n= len(matrix)
    

    for i in range(0,(n+1)//2):
        for j in range(0,n//2):
            matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j], matrix[n-1-j][i] =matrix[n-1-j][i],matrix[i][j], matrix[j][n-1-i],matrix[n-1-i][n-1-j]