class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for ch in s:
            if 97 <= ord(ch) <= 123:
                result += ch
            elif ord(ch) == 42:
                result = result[:-1]
            elif ord(ch) == 35:
                result += result
            else:
                result = result[::-1]
        return result


solution = Solution()
print(solution.processStr('a#b%*'))
print(solution.processStr('z*#'))
