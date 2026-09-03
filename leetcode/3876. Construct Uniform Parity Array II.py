from typing import List


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)
        even_count = 0
        odd_count = 0
        even_num = float('inf')
        for n in nums1:
            if n % 2 == 0:
                even_count += 1
                even_num = min(n, even_num)
            else:
                odd_count += 1
        if even_count == 0 or odd_count == 0:
            return True
        return even_num > min_num


solution = Solution()
print(solution.uniformArray([1, 4, 7]))
print(solution.uniformArray([2, 3]))
print(solution.uniformArray([4, 6]))
