from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        end = n-1
        sums = sum(nums)
        rotation = 0
        max_rotation = float('-inf')
        for i in range(n):
            if i == 0:
                rotation = sum([x*nums[x] for x in range(n)])
                max_rotation = rotation
            else:
                rotation += sums-(n*nums[end])
                if max_rotation < rotation:
                    max_rotation = rotation
                # go backwards
                end = (end - 1 + n) % n
        return max_rotation


solution = Solution()
print(solution.maxRotateFunction([4, 3, 2, 6]))
print(solution.maxRotateFunction([100]))
