from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        result = [['.']*m for _ in range(n)]

        for i in range(m):
            last = n-1
            for j in range(n-1, -1, -1):
                value = boxGrid[i][j]
                if value == '#':
                    result[last][m-1-i] = value
                    last = last-1
                elif value == '*':
                    result[j][m-1-i] = value
                    last = j-1
        return result


solution = Solution()

# solution.rotateTheBox([["#", ".", "#"]])
# solution.rotateTheBox([["#", ".", "*", "."],
#                        ["#", "#", "*", "."]])
solution.rotateTheBox([["#", "#", "*", ".", "*", "."],
                       ["#", "#", "#", "*", ".", "."],
                       ["#", "#", "#", ".", "#", "."]])
