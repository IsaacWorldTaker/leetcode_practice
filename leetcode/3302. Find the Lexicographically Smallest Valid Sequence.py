from collections import defaultdict
from signal import default_int_handler
from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1]*m
        j = m-1
        for i in range(n-1, -1, -1):
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
                if j < 0:
                    break

        change = False
        j = 0
        result = []
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not change and (j == m-1 or last[j+1] > i):
                change = True
                result.append(i)
                j += 1

        return result if len(result) == m else []


solution = Solution()
print(solution.validSequence("vbcca", "abc"))
print(solution.validSequence("bacdc", "abc"))
print(solution.validSequence("aaaaaa", "aaabc"))
print(solution.validSequence("abc", "ab"))
