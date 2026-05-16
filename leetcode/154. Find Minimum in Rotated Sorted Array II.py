from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] == nums[hi]:
                hi -= 1
            else:
                hi = mid
        return nums[lo]


solution = Solution()

print(solution.findMin([1, 3, 5]))
print(solution.findMin([2, 2, 2, 0, 1]))
print(solution.findMin([2, 2, 2, 0, 2]))
