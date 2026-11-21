# class Solution:
#     def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
#         lists= [list(x) for x in zip(*matrix)] # here the zip take teh first element from each row and then make their tuple
#         return lists
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows= len(matrix)
        column= len(matrix[0])
        output = [[0]*rows for _ in range(column) ]
        for i in range(rows):
            for j in range(column):
                output[j][i]= matrix[i][j]
        return output