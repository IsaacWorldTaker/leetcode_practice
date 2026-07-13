class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum_digits = 0
        x = 0
        i = 0
        while n > 0:
            mod = n % 10
            n //= 10
            if mod != 0:
                x += mod*(10**i)
                i += 1
                sum_digits += mod
        return sum_digits*x


solution = Solution()
print(solution.sumAndMultiply(10203004))
print(solution.sumAndMultiply(1000))
