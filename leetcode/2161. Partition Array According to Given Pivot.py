from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        mid = []

        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)

        return (left+mid+right)


solution = Solution()
print(solution.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
print(solution.pivotArray([-3, 4, 3, 2], 2))
