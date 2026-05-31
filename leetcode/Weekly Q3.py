from typing import List


class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        result = 0

        for r in range(n):
            for c in range(m):
                x = matrix[r][c]

                if x == 0:
                    continue

                is_local_max = True

                # Check cells within x rows and x columns
                for nr in range(max(0, r - x), min(n, r + x + 1)):
                    for nc in range(max(0, c - x), min(m, c + x + 1)):

                        # Ignore corners where both distances are exactly x
                        if abs(nr - r) == x and abs(nc - c) == x:
                            continue

                        if matrix[nr][nc] > x:
                            is_local_max = False
                            break

                    if not is_local_max:
                        break

                if is_local_max:
                    result += 1
        return result


solution = Solution()
print(solution.countLocalMaximums([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
      0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))
print(solution.countLocalMaximums([[1, 2], [3, 4]]))
print(solution.countLocalMaximums([[1, 0, 1], [0, 1, 0], [1, 0, 1]]))
print(solution.countLocalMaximums([[1, 1], [1, 1]]))
