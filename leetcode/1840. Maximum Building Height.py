from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        if not any(r[0] == n for r in restrictions):
            restrictions.append([n, n-1])

        restrictions.append([1, 0])
        restrictions = sorted(restrictions, key=lambda x: x[0])

        max_height = 0
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0]))

        for i in range(len(restrictions)-2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))

        for i in range(len(restrictions)-1):
            height = (restrictions[i+1][1]+restrictions[i]
                      [1]+(restrictions[i+1][0]-restrictions[i][0]))//2
            max_height = max(max_height, height)

        return max_height


solution = Solution()
print(solution.maxBuilding(5, [[2, 1], [4, 1]]))
print(solution.maxBuilding(6, []))
print(solution.maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
print(solution.maxBuilding(10, [[8, 5], [9, 0], [6, 2], [
      4, 0], [3, 2], [10, 0], [5, 3], [7, 3], [2, 4]]))
