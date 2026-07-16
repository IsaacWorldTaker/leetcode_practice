class Solution:

    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_even = n * (n + 1)
        sum_odd = n**2
        while sum_even > 0:
            sum_odd, sum_even = sum_even, sum_odd % sum_even

        return sum_odd


solution = Solution()
print(solution.gcdOfOddEvenSums(4))
print(solution.gcdOfOddEvenSums(5))
