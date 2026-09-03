from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # result = [0]*len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        arr1.extend(arr2)
        return arr1


solution = Solution()
print(solution.resultArray([2, 1, 3]))
print(solution.resultArray([5, 4, 3, 8]))
