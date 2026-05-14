from typing import List


class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        def get_layer(layer):
            # Extract perimeter of layer as a flat list (counter-clockwise)
            r0, c0 = layer, layer
            r1, c1 = m - 1 - layer, n - 1 - layer
            elems = []
            # Top row: left to right
            for c in range(c0, c1 + 1):
                elems.append((r0, c))
            # Right col: top+1 to bottom
            for r in range(r0 + 1, r1 + 1):
                elems.append((r, c1))
            # Bottom row: right-1 to left
            for c in range(c1 - 1, c0 - 1, -1):
                elems.append((r1, c))
            # Left col: bottom-1 to top+1
            for r in range(r1 - 1, r0, -1):
                elems.append((r, c0))
            return elems

        num_layers = min(m, n) // 2
        for layer in range(num_layers):
            coords = get_layer(layer)
            L = len(coords)
            shift = k % L
            # Counter-clockwise rotation = shift values forward in the list
            vals = [grid[r][c] for r, c in coords]
            vals = vals[shift:] + vals[:shift]
            for (r, c), v in zip(coords, vals):
                grid[r][c] = v

        return grid


solution = Solution()
# print(solution.rotateGrid([[40, 10], [30, 20]], 1))
print(solution.rotateGrid(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 2))
