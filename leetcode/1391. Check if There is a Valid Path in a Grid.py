from typing import List

# right=1, left=-1
# top=2, bot=-2


class Solution:
    streets = {
        1: [(0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(1, 0), (0, 1)],
        5: [(-1, 0), (0, -1)],
        6: [(-1, 0), (0, 1)],
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return True
        visited = [[False]*col for _ in range(row)]

        i, j = 0, 0
        return self.dfs(grid, visited, i, j, row, col)

    def dfs(self, grid, visited, i, j, row, col):
        visited[i][j] = True
        if i == row-1 and j == col-1:
            return True
        for dr, dc in self.streets[grid[i][j]]:
            nr, nc = i+dr, j+dc
            if 0 <= nr < row and 0 <= nc < col:
                if not visited[nr][nc] and (-dr, -dc) in self.streets[grid[nr][nc]]:
                    if self.dfs(grid, visited, nr, nc, row, col):
                        return True
        return False

        # paths = streets[grid[0][0]].copy()
        # paths.discard(2)
        # paths.discard(-1)
        # if not paths:
        #     return False
        # prev_path = paths.pop()
        # i, j = self.orientation[prev_path][0], self.orientation[prev_path][1]

        # if not (i < len(grid) and j < len(grid[0])) or -1*prev_path not in streets[grid[i][j]]:
        #     return False
        # visited[0][0] = True
        # while i < len(grid) and j < len(grid[0]):
        #     paths = streets[grid[i][j]].copy()
        #     if -1*prev_path in paths and not visited[i][j]:
        #         paths.discard(-1*prev_path)
        #         prev_path = paths.pop()
        #         # one path remaining
        #         visited[i][j] = True
        #         i, j = i + \
        #             self.orientation[prev_path][0], j + \
        #             self.orientation[prev_path][1]

        #     else:
        #         return False

        # return True


solution = Solution()
print(solution.hasValidPath([[2, 4, 3], [6, 5, 2]]))
print(solution.hasValidPath([[1, 2, 1], [1, 2, 1]]))
print(solution.hasValidPath([[1, 1, 2]]))
print(solution.hasValidPath([[2, 6]]))
print(solution.hasValidPath([[4, 3, 3], [6, 5, 2]]))
