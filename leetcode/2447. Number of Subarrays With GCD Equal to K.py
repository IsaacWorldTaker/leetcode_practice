from typing import List
import math


class Solution:

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        prev = {}
        result = 0
        n = len(nums)
        for i in range(n):
            new_groups = {}
            for g, count in prev.items():
                gcd = math.gcd(g, nums[i])
                # all previous subarrays can be joined with this
                new_groups[gcd] = new_groups.get(gcd, 0) + count
            new_groups[nums[i]] = new_groups.get(nums[i], 0) + 1
            prev = new_groups
            result += prev.get(k, 0)
        return result


solution = Solution()
print(solution.subarrayGCD([9, 3, 1, 2, 6, 3], 3))
print(solution.subarrayGCD([4], 7))
