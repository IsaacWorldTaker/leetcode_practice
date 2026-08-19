from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        total = 2*n
        rows = defaultdict(int)
        for seat in reservedSeats:
            rows[seat[0]] |= (1 << seat[1])

        for bits in rows.values():
            free25 = (0b1111 & (bits >> 2) & 0b1111) == 0
            free69 = (0b1111 & (bits >> 6) & 0b1111) == 0
            free47 = (0b1111 & (bits >> 4) & 0b1111) == 0
            if free25 and free69:
                continue
            elif free25 or free69 or free47:
                total -= 1
            else:
                total -= 2
        return total


solution = Solution()
print(solution.maxNumberOfFamilies(
    3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(solution.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]]))
print(solution.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
