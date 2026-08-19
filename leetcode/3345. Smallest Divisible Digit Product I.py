class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            prod = 1
            number = i
            while number > 0:
                prod *= number % 10
                number //= 10
            if prod % t == 0:
                return i


solution = Solution()
print(solution.smallestNumber(10, 2))
print(solution.smallestNumber(15, 3))
