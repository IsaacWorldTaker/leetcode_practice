from math import inf
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        memo = [[0]*n for _ in range(n)]
        suffix_sum = piles[:]
        for i in range(n-2, -1, -1):
            suffix_sum[i] += suffix_sum[i+1]

        def best(i, m):
            if i+2*m >= n:
                return suffix_sum[i]
            if memo[i][m] > 0:
                return memo[i][m]
            res = float('inf')
            for x in range(1, 2*m+1):
                res = min(res, best(i+x, max(m, x)))
            memo[i][m] = suffix_sum[i]-res
            return memo[i][m]
        return best(0, 1)


solution = Solution()
print(solution.stoneGameII([2, 7, 9, 4, 4]))
print(solution.stoneGameII([1, 2, 3, 4, 5, 100]))
