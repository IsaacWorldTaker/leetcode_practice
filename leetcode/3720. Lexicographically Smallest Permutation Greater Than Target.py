
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0]*26
        n = len(s)
        for i in s:
            freq[ord(i)-ord('a')] += 1
        result = []
        for c in target:
            order = ord(c)-ord('a')
            if freq[order] != 0:
                freq[order] -= 1
                result.append(c)
            else:
                break
        backtrack_point = len(result) if len(result) < n else n - 1
        first_attempt = (len(result) < n)
        while backtrack_point >= 0:
            if not first_attempt:
                ch = result.pop()
                freq[ord(ch)-ord('a')] += 1
            first_attempt = False
            order = ord(target[backtrack_point]) - ord('a')
            found = -1
            for i in range(order+1, 26):
                if freq[i]:
                    found = i
                    break
            if found != -1:
                freq[found] -= 1
                result.append(chr(found+97))
                break
            else:
                backtrack_point -= 1
        if backtrack_point < 0:
            return ''
        for i in range(26):
            while freq[i]:
                result.append(chr(i+97))
                freq[i] -= 1

        return ''.join(result)


solution = Solution()
print(solution.lexGreaterPermutation("abc", "bba"))
print(solution.lexGreaterPermutation("leet", "code"))
print(solution.lexGreaterPermutation("baba", "bbaa"))
print(solution.lexGreaterPermutation("ab", "ab"))
