from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(len(s)+1):
            result_check = []
            for k in range(i):
                if dp[k] and s[k: i] in wordDict:
                    result_check.append(True)
                else:
                    result_check.append(False)
            if any(result_check):
                dp[i] = True

        return dp[-1]


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if s.startswith(w, i):
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]


solution = Solution2()
print(solution.wordBreak("leetcode", ["leet", "code"]))
print(solution.wordBreak("applepenapple", ["apple", "pen"]))
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
