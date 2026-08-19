import math
from collections import Counter


class Solution:

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        full_counts = Counter(s)

        mid = ""
        half_counts = {}
        for char, count in sorted(full_counts.items()):
            if count % 2 != 0:
                mid = char
            half_counts[char] = count // 2

        half_length = n // 2

        def num_permutations(counts: dict) -> int:
            total_items = sum(counts.values())
            res = 1
            for count in counts.values():
                res *= math.comb(total_items, count)
                total_items -= count
            return res

        total_possible = num_permutations(half_counts)
        if k > total_possible:
            return ""

        result_half = []
        for _ in range(half_length):
            for char in sorted(half_counts.keys()):
                if half_counts[char] == 0:
                    continue

                half_counts[char] -= 1
                cnt = num_permutations(half_counts)

                if k <= cnt:
                    result_half.append(char)
                    break
                else:
                    k -= cnt
                    half_counts[char] += 1  # Backtrack

        half_str = "".join(result_half)
        return half_str + mid + half_str[::-1]


solution = Solution()
# print(solution.smallestPalindrome('abba', 2))
# print(solution.smallestPalindrome('aa', 2))
# print(solution.smallestPalindrome('bacab', 1))
print(solution.smallestPalindrome('kxk', 2))
