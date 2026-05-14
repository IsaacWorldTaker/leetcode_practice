from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_legth = max(trips, key=lambda x: x[2])[2]
        road = [0]*(max_legth+1)
        for trip in trips:
            road[trip[1]] += trip[0]
            road[trip[2]] -= trip[0]

        # calculate prefix sum
        prefix_sum = 0
        for i in road:
            prefix_sum += i
            if prefix_sum > capacity:
                return False
        return True


solution = Solution()
print(solution.carPooling([[2, 1, 5], [3, 3, 7]], 4))
print(solution.carPooling([[2, 1, 5], [3, 3, 7]], 5))
print(solution.carPooling([[9, 0, 1], [3, 3, 7]], 4))
