from typing import List
import math


class Solution:
    MOD = 10**9 + 7

    def subsequencePairCount(self, nums: List[int]) -> int:
        limit = max(nums)+1
        dp = [[0] * limit for _ in range(limit)]
        dp[0][0] = 1

        for n in nums:
            new_dp = [[0] * limit for _ in range(limit)]
            for g1 in range(limit):
                for g2 in range(limit):

                    # choice 1
                    new_dp[math.gcd(g1,
                                    n)][g2] = (new_dp[math.gcd(g1, n)][g2] +
                                               dp[g1][g2]) % self.MOD

                    # choice 2
                    new_dp[g1][math.gcd(g2,
                                        n)] = (new_dp[g1][math.gcd(g2, n)] +
                                               dp[g1][g2]) % self.MOD

                    # choice 3
                    new_dp[g1][g2] = (new_dp[g1][g2] + dp[g1][g2]) % self.MOD
            dp = new_dp.copy()
        result = 0
        for i in range(1, limit):
            result += (dp[i][i] % self.MOD)
        return result % self.MOD


solution = Solution()
print(solution.subsequencePairCount([1, 2, 3, 4]))
print(solution.subsequencePairCount([10, 20, 30]))
print(solution.subsequencePairCount([1, 1, 1, 1]))
print(solution.subsequencePairCount([26, 30, 22, 27, 24]))
