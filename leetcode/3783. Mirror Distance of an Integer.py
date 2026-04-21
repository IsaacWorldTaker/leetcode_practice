
class Solution:
    def mirrorDistance(self, n: int) -> int:
        reversed_n = int(str(n)[::-1])
        return abs(n-reversed_n)


solution = Solution()

print(solution.mirrorDistance(25))
print(solution.mirrorDistance(10))
print(solution.mirrorDistance(7))
