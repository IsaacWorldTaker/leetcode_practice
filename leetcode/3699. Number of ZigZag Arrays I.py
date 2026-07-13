class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Edge case handling if n = 1 (though standard constraints say n >= 3)
        if n == 1:
            return m % MOD

        # dp[v] stores the number of valid sequences ending in value v
        dp = [1] * m

        for step in range(2, n + 1):
            new_dp = [0] * m

            if step % 2 == 0:
                # Step UP: A[i-1] < A[i]
                # Accumulate prefix sums from left to right
                running_sum = 0
                for v in range(m):
                    new_dp[v] = running_sum
                    running_sum = (running_sum + dp[v]) % MOD
            else:
                # Step DOWN: A[i-1] > A[i]
                # Accumulate suffix sums from right to left
                running_sum = 0
                for v in range(m - 1, -1, -1):
                    new_dp[v] = running_sum
                    running_sum = (running_sum + dp[v]) % MOD

            dp = new_dp

        # Total ZigZag arrays = 2 * (Number of Type 1 arrays)
        total_type1 = sum(dp) % MOD
        return (2 * total_type1) % MOD


solution = Solution()

print(solution.zigZagArrays(3, 4, 5))
print(solution.zigZagArrays(3, 1, 3))
