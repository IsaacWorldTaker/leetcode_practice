from typing import List
from collections import Counter


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_base = max(nums)
        counter = Counter(nums)
        if len(nums) != max_base+1:
            return False
        if len(counter) != max_base:
            return False
        if counter[max_base] != 2:
            return False
        return True
    #     base = self.get_base(max_base)
    #     if len(nums) != max_base+1:
    #         return False
    #     nums.pop(max_idx)

    #     for i in nums:
    #         if i not in base:
    #             return False
    #         base.remove(i)
    #     return True

    # def get_base(self, num):
    #     base = {i+1 for i in range(num)}
    #     base.add(num)
    #     return base


solution = Solution()
print(solution.isGood([2, 1, 3]))
print(solution.isGood([1, 3, 3, 2]))
print(solution.isGood([1, 1]))
print(solution.isGood([3, 4, 4, 1, 2, 1]))
print(solution.isGood([5, 7, 3, 1, 5, 2, 6, 4]))
