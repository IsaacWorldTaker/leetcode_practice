from collections import deque
from typing import List


class Solution:

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        max_health = [[0] * n for _ in range(m)]

        q = deque()
        q.append([0, 0])
        max_health[0][0] = health-grid[0][0]

        while q:
            row, col = q.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_health = max_health[row][col] - grid[new_row][new_col]
                    if new_health > 0 and new_health > max_health[new_row][
                            new_col]:
                        if new_row == m - 1 and new_col == n - 1:
                            return True
                        q.append([new_row, new_col])
                        max_health[new_row][new_col] = new_health

        return False


solution = Solution()
print(solution.findSafeWalk(
    [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))
print(solution.findSafeWalk([[0, 1, 1, 0, 0, 0], [
      1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], 3))
print(solution.findSafeWalk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))
print(solution.findSafeWalk([[1, 1, 1, 1]], 4))
