from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence = []
        result = []
        for n in range(1, 10):
            for start in range(1, 10):
                if start+n-1 <= 9:
                    sequence.append(self.build_number(start, n))
                    if sequence[-1] >= low and sequence[-1] <= high:
                        result.append(sequence[-1])
        return result

    def build_number(self, start, n):
        result = start*(10**(n-1))
        start += 1
        for i in range(n-2, -1, -1):
            result += start*(10**i)
            start += 1

        return result


solution = Solution()
# print(solution.sequentialDigits(100, 300))
print(solution.sequentialDigits(1000, 13000))
print(solution.sequentialDigits(1234, 13000))
print(solution.sequentialDigits(1235, 13000))
print(solution.sequentialDigits(6799, 13000))
