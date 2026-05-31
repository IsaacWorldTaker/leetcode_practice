from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)

        for i, _ in enumerate(arr):
            self.dp(i, arr, d, n, dp)
        return max(dp)

    def dp(self, i, arr, d, n, dp):
        # base case
        if dp[i] != 0:
            return dp[i]
        dp[i] = 1
        # check valid jumps in 0 to d
        for x in range(1, d+1):
            if i+x < n:
                if arr[i] <= arr[i+x]:
                    break
                else:
                    self.dp(i+x, arr, d, n, dp)
                    dp[i] = max(dp[i], dp[i+x]+1)
        for x in range(1, d+1):
            if i-x >= 0:
                if arr[i] <= arr[i-x]:
                    break
                else:
                    self.dp(i-x, arr, d, n, dp)
                    dp[i] = max(dp[i], dp[i-x]+1)


solution = Solution()

print(solution.maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
print(solution.maxJumps([3, 3, 3, 3, 3], 2))
print(solution.maxJumps([7, 6, 5, 4, 3, 2, 1], 1))
