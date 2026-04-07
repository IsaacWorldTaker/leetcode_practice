from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = val

        return k


solution = Solution()

# test 1
nums = [3, 2, 2, 3]
val = 3
expected_answer = [2, 2]

k, asnwer = solution.removeElement(nums, val)

assert k == len(expected_answer)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
expected_answer = [0, 1, 4, 0, 3]

k, asnwer = solution.removeElement(nums, val)

assert k == len(expected_answer)
