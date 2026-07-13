from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        count = 0
        max_right = 0

        for i, interval in enumerate(intervals):
            if interval[1] <= max_right:
                count += 1
            else:
                max_right = interval[1]

        return len(intervals)-count


solution = Solution()
print(solution.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
print(solution.removeCoveredIntervals([[1, 4], [2, 3]]))
