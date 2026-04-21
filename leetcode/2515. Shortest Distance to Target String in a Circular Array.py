from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        path_1 = 0
        path_2 = 0
        i = startIndex
        # moving forward
        while path_1 <= len(words):
            if words[i] == target:
                break
            i = (i + 1) % len(words)
            path_1 += 1

        if path_1 >= len(words):
            return -1
        i = startIndex
        # moving backward
        while path_2 <= len(words):
            if words[i] == target:
                break
            i = (i - 1 + len(words)) % len(words)
            path_2 += 1

        return min(path_1, path_2)


solution = Solution()
print(solution.closestTarget(
    ["hello", "i", "am", "leetcode", "hello"], "hello", 1))
print(solution.closestTarget(
    ["a", "b", "leetcode"], "leetcode", 0))
print(solution.closestTarget(
    ["i", "eat", "leetcode"], "ate", 0))
