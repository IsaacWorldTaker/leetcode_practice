from typing import List


class Solution:

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prev_row = [[-1]*(k+1) for _ in range(n)]

        for row in range(m):
            curr_row = [[-1]*(k+1) for _ in range(n)]
            for col in range(n):
                cell_cost = 1 if grid[row][col] > 0 else 0
                cell_score = grid[row][col]
                if row == 0 and col == 0:
                    curr_row[0][cell_cost] = cell_score
                    continue

                for c in range(cell_cost, k + 1):
                    res = -1
                    # Check Top
                    if row > 0:
                        prev_val = prev_row[col][c - cell_cost]
                        if prev_val != -1:
                            res = max(res, cell_score + prev_val)
                    # Check Left
                    if col > 0:
                        prev_val = curr_row[col - 1][c - cell_cost]
                        if prev_val != -1:
                            res = max(res, cell_score + prev_val)

                    curr_row[col][c] = res

            prev_row = curr_row
            curr_row = [[-1]*(k+1) for _ in range(n)]
        return max(prev_row[-1])


solution = Solution()
print(solution.maxPathScore([[0, 1], [2, 0]], 1))
print(solution.maxPathScore([[0, 1], [1, 2]], 1))
