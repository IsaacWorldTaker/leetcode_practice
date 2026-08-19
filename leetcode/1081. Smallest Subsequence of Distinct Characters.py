class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {}
        visited = set()
        result = []
        for i, c in enumerate(s):
            last_occ[c] = i
        for i, c in enumerate(s):
            if not result:
                result.append(c)
                visited.add(c)
            elif c not in visited:
                while result and last_occ[result[-1]] > i and c < result[-1]:
                    last_char = result.pop()
                    visited.remove(last_char)
                result.append(c)
                visited.add(c)
        return ''.join(result)


solution = Solution()
print(solution.smallestSubsequence('bcabc'))
print(solution.smallestSubsequence('cbacdcbc'))
print(solution.smallestSubsequence('ecbacba'))
