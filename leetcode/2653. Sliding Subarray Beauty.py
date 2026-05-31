
from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        freq = {x: 0 for x in range(-50, 1)}
        # # first window
        count = x
        for i in range(k):
            if nums[i] < 0:
                freq[nums[i]] += 1

        for item in freq.items():
            count -= item[1]
            if count <= 0:
                result.append(item[0])
                break
        if len(result) < 1:
            result.append(0)

        for i in range(1, n-k+1):
            count = x
            window = nums[i:i+k]
            if nums[i-1] < 0:
                freq[nums[i-1]] -= 1
            if window[-1] < 0:
                freq[window[-1]] += 1

            for item in freq.items():
                count -= item[1]
                if count <= 0:
                    result.append(item[0])
                    break
            if len(result) != i+1:
                result.append(0)

        return result


solution = Solution()
print(solution.getSubarrayBeauty([-50, 14], 2, 2))
print(solution.getSubarrayBeauty([5], 1, 1))
print(solution.getSubarrayBeauty([-44, 20, -29, -44, 39, -2], 5, 4))
print(solution.getSubarrayBeauty([-38, -37, 44], 2, 2))
print(solution.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))
print(solution.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2))
print(solution.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1))
