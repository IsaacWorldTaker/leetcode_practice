from typing import List
import math


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = {}
        longest_result = 1
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for num, count in freq.items():
            if num == 1:
                longest_result = max(
                    longest_result, count if count % 2 == 1 else count - 1)
                continue
            root = math.sqrt(num)
            if int(root) ** 2 != num or int(root) not in freq:
                result = num
                chain = 0
                while freq.get(result, 0) >= 2:
                    result *= result
                    chain += 1
                if freq.get(result) == 1:
                    longest_result = max(longest_result, 2*chain+1)
                else:
                    longest_result = max(longest_result, 2*chain-1)
        return longest_result


solution = Solution()
# print(solution.maximumLength([5, 4, 1, 2, 2]))
# print(solution.maximumLength([1, 3, 2, 4]))
print(solution.maximumLength([16, 16, 256, 256, 65536, 65536]))
print(solution.maximumLength([14, 14, 196, 196, 38416, 38416]))
print(solution.maximumLength(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]))
