from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid[0]), len(grid)
        result = [[0]*n for _ in range(m)]
        total_len = m*n
        for i in range(m):
            for j in range(n):
                pos = (i*n)+j
                new_pos = (pos+k) % total_len
                r = new_pos//n
                c = new_pos % n
                result[r][c] = grid[i][j]
        return result


solution = Solution()
print(solution.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(solution.shiftGrid(
    [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(solution.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
