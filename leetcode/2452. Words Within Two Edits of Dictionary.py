from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        results = []
        for word in queries:
            for match in dictionary:
                max_mismatch = 0
                for compare in zip(word, match):
                    if compare[0] != compare[1]:
                        max_mismatch += 1
                        if max_mismatch > 2:
                            break
                if max_mismatch <= 2:
                    results.append(word)
                    break
        return results


solution = Solution()

print(solution.twoEditWords(
    ["word", "note", "ants", "wood"], ["wood", "joke", "moat"]))
print(solution.twoEditWords(["yes"], ["not"]))
