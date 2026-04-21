from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            i += nums1[i] > nums2[j]
            j += 1

        return max(0, j - i - 1)


solution = Solution()
print(solution.maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(solution.maxDistance([2, 2, 2],  [10, 10, 1]))
print(solution.maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
