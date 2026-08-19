from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_bit = len("{0:b}".format(len(nums)))
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2

        return 2**max_bit-1


solution = Solution()

print(solution.uniqueXorTriplets([1, 2]))
print(solution.uniqueXorTriplets([3, 1, 2]))
