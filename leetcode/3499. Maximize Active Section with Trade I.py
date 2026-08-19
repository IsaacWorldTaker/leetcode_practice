class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        runs = {}


solution = Solution()
print(solution.maxActiveSectionsAfterTrade("01"))
print(solution.maxActiveSectionsAfterTrade("0100"))
print(solution.maxActiveSectionsAfterTrade("1000100"))
print(solution.maxActiveSectionsAfterTrade("01010"))
