from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                    matrix[n-1-j][i], matrix[i][j], matrix[j][n -
                                                              1-i], matrix[n-1-i][n-1-j]
                # 1 swap
                temp = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                # 2 swap
                temp2 = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = temp
                # 3 swap
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = temp2
                # 4 swap
                matrix[i][j] = temp


solution = Solution()
solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solution.rotate(
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
