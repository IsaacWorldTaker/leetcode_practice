from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # make randomNote into a hash
        hash_count = {}
        for i in ransomNote:
            hash_count[i] = hash_count.get(i, 0)+1

        for j in magazine:
            if hash_count.get(j, 0) > 0:
                hash_count[j] -= 1

        return all(v <= 0 for v in hash_count.values())

    def canConstructPythonic(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote)-Counter(magazine))


solution = Solution()

print(solution.canConstruct("a", "b"))
print(solution.canConstruct("aa", "ab"))
print(solution.canConstruct("aa", "aab"))
print(solution.canConstruct("abc", "aabbcc"))
print(solution.canConstruct("abd", "aabbcc"))

print(solution.canConstructPythonic("a", "b"))
print(solution.canConstructPythonic("aa", "ab"))
print(solution.canConstructPythonic("aa", "aab"))
print(solution.canConstructPythonic("abc", "aabbcc"))
print(solution.canConstructPythonic("abd", "aabbcc"))
