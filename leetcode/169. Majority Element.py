from typing import List
# Using the Boyer-Moore Voting Algorithm
# When an algorithm appears more than half the list's length, that mean it appears more than all the other elements combined.
# Moving from the left to the right, every time we see the same element, we support it (basically ignore) and when we see a different element, we cancel that one out.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]
        for i in nums:
            if i != prev:
                count -= 1
                if count == 0:
                    prev = i
                    count += 1
            else:
                count += 1

        return prev


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([3, 3, 4]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
