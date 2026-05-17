from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_reach = 0
        min_jumps = 0
        current_level = 0
        for i in range(0, n):
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
            if i == current_level and i < n-1:
                min_jumps += 1
                current_level = max_reach

        return min_jumps


solution = Solution()

print(solution.jump([0]))
print(solution.jump([1, 2]))
print(solution.jump([2, 5, 0, 0]))
print(solution.jump([2, 3, 1, 1, 4]))
print(solution.jump([2, 0, 0]))
print(solution.jump([2, 0]))
print(solution.jump([2, 5, 1, 3, 0, 0, 2]))
