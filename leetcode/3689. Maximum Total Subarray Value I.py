from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums)-min(nums))


solution = Solution()
print(solution.maxTotalValue([1, 3, 2], 2))
print(solution.maxTotalValue([4, 2, 5, 1], 3))
