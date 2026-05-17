from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(0, n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return max_reach >= n-1


solution = Solution()

print(solution.canJump([2, 5, 0, 0]))
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
print(solution.canJump([2, 0, 0]))
print(solution.canJump([2, 0]))
print(solution.canJump([2, 0, 1, 3, 0, 0, 2]))
