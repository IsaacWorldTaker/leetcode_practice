class Solution:
    def maxProduct(self, n: int) -> int:
        number = sorted(str(n))
        return int(number[-1])*int(number[-2])


solution = Solution()
print(solution.maxProduct(31))
print(solution.maxProduct(22))
print(solution.maxProduct(124))
