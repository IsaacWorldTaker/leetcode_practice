from typing import List
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        solution = []
        positions = {}
        for i, num in enumerate(nums):
            if positions.get(num):
                positions[num].append(i)
            else:
                positions[num] = [i]
        for i, num in enumerate(queries):
            # paths = []
            index = bisect.bisect_left(positions[nums[num]], num)
            next = positions[nums[num]][(index+1) % len(positions[nums[num]])]
            prev = positions[nums[num]][(index-1+len(positions[nums[num]])
                                         ) % len(positions[nums[num]])]
            path_1 = min(abs(num - next), len(nums) - abs(num - next))
            path_2 = min(abs(num - prev), len(nums) - abs(num - prev))
            min_value = min(path_1, path_2)
            solution.append(min_value if min_value else -1)
        return solution

    def solveQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries


solution = Solution()
print(solution.solveQueries2([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
print(solution.solveQueries2([1, 2, 3, 4], [0, 1, 2, 3]))
print(solution.solveQueries2([12, 19, 12, 8, 12, 10], [0, 5, 3, 1]))
print(solution.solveQueries2([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
