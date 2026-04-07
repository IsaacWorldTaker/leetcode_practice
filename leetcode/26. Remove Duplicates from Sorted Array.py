from typing import List
# Using a two pointer approach, we traverse through the num list


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([1]))
print(solution.removeDuplicates([1, 2]))
