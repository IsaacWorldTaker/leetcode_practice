from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_1 = nums[-1]*nums[-2]*nums[-3]
        max_2 = nums[0]*nums[1]*nums[-1]
        return max(max_1, max_2)


solution = Solution()
print(solution.maximumProduct([1, 2, 3]))
print(solution.maximumProduct([1, 2, 3, 4]))
print(solution.maximumProduct([-1, -2, -3]))
print(solution.maximumProduct([-10, 1, 3, 5]))
print(solution.maximumProduct([-10, -1, 3, 5]))
