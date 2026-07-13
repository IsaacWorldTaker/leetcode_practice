from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            # meaning the item is higher than the previous by more than 1
            if abs(arr[i]-arr[i-1]) > 1:
                arr[i] = arr[i-1]+1
        return arr[-1]


solution = Solution()
print(solution.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))
print(solution.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]))
print(solution.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]))
print(solution.maximumElementAfterDecrementingAndRearranging([73, 98, 9]))
