from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        lo, hi = 0, n-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
print(solution.findMin([11, 13, 15, 17]))
print(solution.findMin([1]))
