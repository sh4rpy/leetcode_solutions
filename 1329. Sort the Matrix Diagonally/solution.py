class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        row, col = len(mat), len(mat[0])
        for i in range(row):
            temp, n = [], min(row - i, col)
            for j in range(n):
                temp.append(mat[i + j][j])
            temp.sort()
            for j in range(n):
                mat[i + j][j] = temp[j]
        for i in range(1, col):
            temp, n = [], min(col - i, row)
            for j in range(n):
                temp.append(mat[j][i + j])
            temp.sort()
            for j in range(n):
                mat[j][i + j] = temp[j]
        return mat
