from bisect import bisect_left
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        converted_points = self.convert(side, points)
        perimeter = 4 * side

        low = 1
        high = side  # The max possible min-distance is roughly perimeter/k
        ans = 1

        while low <= high:
            mid = low + (high - low) // 2
            if self.pick_check(mid, converted_points, k, perimeter):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def convert(self, side: int, points: List[List[int]]):
        converted_points = []
        for x, y in points:
            if y == 0:
                converted_points.append(x)
            elif x == side:
                converted_points.append(side + y)
            elif y == side:
                converted_points.append(2 * side + (side - x))
            else:  # x == 0
                converted_points.append(3 * side + (side - y))
        converted_points.sort()
        return converted_points

    def pick_check(self, min_dist, points, k, perimeter):
        n = len(points)
        # We only need to try starting at points that could reasonably
        # be part of the first segment to optimize.
        for i in range(n):
            start_val = points[i]
            curr_idx = i

            for _ in range(k - 1):
                # Find next point at least min_dist away
                target = points[curr_idx] + min_dist
                next_idx = bisect_left(points, target)

                if next_idx >= n:
                    # Logic for wrap-around could go here,
                    curr_idx = -1
                    break
                curr_idx = next_idx

            if curr_idx != -1:
                # Crucial check: Is the gap between the LAST and FIRST point valid?
                if (start_val + perimeter) - points[curr_idx] >= min_dist:
                    return True
        return False


solution = Solution()
# Should now correctly return 3
print(solution.maxDistance(9, [[8, 0], [5, 9], [2, 0], [4, 9], [0, 1]], 4))
