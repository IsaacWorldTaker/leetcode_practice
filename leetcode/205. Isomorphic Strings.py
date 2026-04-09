

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        last_seen_1 = 128 * [-1]
        last_seen_2 = 128 * [-1]
        for i in range(len(s)):
            index_1 = ord(s[i])
            index_2 = ord(t[i])
            if last_seen_1[index_1] != last_seen_2[index_2]:
                return False

            last_seen_1[index_1] = i
            last_seen_2[index_2] = i

        return True


solution = Solution()

print(solution.isIsomorphic("ab", "ca"))
print(solution.isIsomorphic("paper", "ttile"))
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))
print(solution.isIsomorphic("badc", "baba"))
