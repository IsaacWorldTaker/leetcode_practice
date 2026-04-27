from typing import List


class Solution:
    DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.m, self.n = len(grid), len(grid[0])
        visited = [[False]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j]:
                    if self.dfs(grid, visited, i, j, i, j):
                        return True
        return False

    def dfs(self, grid, visited, row, col, parent_row, parent_col):
        visited[row][col] = True
        curr = grid[row][col]

        for dr, dc in self.DIRS:
            i, j = row + dr, col + dc

            if 0 <= i < self.m and 0 <= j < self.n:
                if (i, j) != (parent_row, parent_col) and visited[i][j] and grid[i][j] == curr:
                    return True

                if not visited[i][j] and grid[i][j] == curr:
                    if self.dfs(grid, visited, i, j, row, col):
                        return True
        return False


solution = Solution()
print(solution.containsCycle([["a", "a", "a", "a"], [
      "a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))
print(solution.containsCycle([["c", "c", "c", "a"], [
      "c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(solution.containsCycle(
    [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
