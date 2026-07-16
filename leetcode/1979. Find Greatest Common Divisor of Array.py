from typing import List


class Solution:

    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        while min_num > 0:
            max_num, min_num = min_num, max_num % min_num
        return max_num


solution = Solution()
print(solution.findGCD([2, 5, 6, 9, 10]))
print(solution.findGCD([7, 5, 6, 8, 3]))
print(solution.findGCD([3, 3]))
