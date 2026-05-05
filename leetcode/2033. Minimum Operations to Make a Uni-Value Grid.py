from typing import List
0


class Solution:

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Sort and flatten the array.
        flat_sorted = sorted([x for row in grid for x in row])
        median = flat_sorted[len(flat_sorted) // 2]
        count = 0
        for i in flat_sorted:
            diff = abs(i - median) % x
            if diff > 0:
                return -1
            else:
                count += abs(i - median) // x

        return count

    def minOperations2(self, grid: List[List[int]], x: int) -> int:
        # Sort and flatten the array.
        mod = None
        # if two elements a and b are reachable from each other via steps of x, then they must have the same a%x and b%x
        for row in grid:
            for val in row:
                if mod is None:
                    mod = val % x
                elif val % x != mod:
                    return -1  # They don't have the same mod so there is at least one element that can not reach the same value other values can get to in steps of x

        flat_sorted = sorted([x for row in grid for x in row])

        median_index = len(flat_sorted) // 2
        if median_index == 0:
            return 0
        return (sum(flat_sorted[median_index+1:]) -
                sum(flat_sorted[:median_index])) // x


solution = Solution()
print(solution.minOperations2([[2, 4], [6, 8]], 2))
print(solution.minOperations2([[1, 5], [2, 3]], 1))
print(solution.minOperations2([[1, 2], [3, 4]], 2))
print(solution.minOperations2([[1, 1, 10000]], 1))
