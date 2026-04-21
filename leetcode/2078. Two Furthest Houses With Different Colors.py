
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0

        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                max_dist = abs(i-(len(colors)-1))
                break

        for j in range(len(colors)-1, 0, -1):
            if colors[j] != colors[0]:
                max_dist = max(max_dist, abs(j))
                break
        return max_dist


solution = Solution()

print(solution.maxDistance([1, 1, 1, 6, 1, 1, 1]))
print(solution.maxDistance([1, 8, 3, 8, 3]))
print(solution.maxDistance([0, 1]))
