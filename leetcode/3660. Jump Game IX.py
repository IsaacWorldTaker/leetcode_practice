from turtle import st
from typing import List


class Solution:

    def maxValue2(self, nums: List[int]) -> List[int]:
        left_max_list = [0]*len(nums)
        left_max = nums[0]
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] >= left_max:
                left_max = nums[i]
            left_max_list[i] = left_max
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    result[i] = max(result[i], left_max_list[j])

        return result

    def maxValue(self, nums: List[int]):
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(n):
            curr_val = nums[i]
            curr_left = i
            curr_right = i
            while stack and stack[-1][0] > nums[i]:
                top_val, top_left, top_right = stack.pop()
                curr_val = max(top_val, curr_val)
                curr_left = top_left

            stack.append((curr_val, curr_left, curr_right))
        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2]+1):
                ans[j] = stack[i][0]

        return ans


solution = Solution()
print(solution.maxValue([2, 1, 3]))
print(solution.maxValue([2, 3, 1]))
print(solution.maxValue([8, 5, 3, 6, 4, 10, 1, 13, 9]))
