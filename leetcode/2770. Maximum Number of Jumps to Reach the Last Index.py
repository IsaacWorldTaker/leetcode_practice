from typing import List


class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            jumps = []
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:
                    jumps.append(j)
                    break
