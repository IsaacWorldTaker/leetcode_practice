class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase_freq = set()  # To store the appearance of lowercase characters
        highercase_freq = set()
        blacklist = set()
        for ch in word:
            ascii_code = ord(ch)
            if ascii_code >= 97:
                if ascii_code-32 not in lowercase_freq:
                    lowercase_freq.add(ascii_code-32)
                if ascii_code-32 in highercase_freq:
                    blacklist.add(ascii_code-32)
            else:
                if ascii_code in lowercase_freq:
                    highercase_freq.add(ascii_code)
                else:
                    blacklist.add(ascii_code)
        return len(highercase_freq - blacklist)


solution = Solution()
print(solution.numberOfSpecialChars('aaAbcBC'))
print(solution.numberOfSpecialChars('abc'))
print(solution.numberOfSpecialChars('AbBCab'))
print(solution.numberOfSpecialChars('AbcbDBdD'))
print(solution.numberOfSpecialChars('dcbCC'))
print(solution.numberOfSpecialChars('dDDadDddCE'))
