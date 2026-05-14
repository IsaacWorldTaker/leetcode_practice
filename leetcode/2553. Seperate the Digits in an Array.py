from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:

            result.extend(self.get_digits(i))

        return result

    def get_digits(self, num):
        result = []
        while num > 0:
            result.append(num % (10))
            num = num//10
        return result[::-1]


solution = Solution()
print(solution.separateDigits([10, 25, 83, 77]))
print(solution.separateDigits([7, 1, 3, 9]))
