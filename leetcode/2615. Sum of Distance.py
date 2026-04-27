
from typing import List


class Solution:

    def distance(self, nums: List[int]) -> List[int]:
        val_sums = {}
        val_count = {}
        right_sum, left_sum = [0] * len(nums), [0] * len(nums)
        right_count, left_count = [0] * len(nums), [0] * len(nums)
        result = [0] * len(nums)

        # First pass: move from right to left and calculate sums and counts
        for i in range(len(nums) - 1, -1, -1):
            if val_sums.get(nums[i]) is None:
                val_sums[nums[i]] = i
                val_count[nums[i]] = 1
            else:
                val_sums[nums[i]] += i
                val_count[nums[i]] += 1

            right_count[i] = val_count[nums[i]]
            right_sum[i] += val_sums[nums[i]]
        val_sums = {}
        val_count = {}
        # Second pass: move from left to right. Remove the count and value from the right while adding them to the left.
        # Finally calculate the sum by adding the sums of the distances in both left and right. We're using running variables to store and modify left and right arrays
        for j in range(len(nums)):
            if val_sums.get(nums[j]) is None:
                val_sums[nums[j]] = j
                val_count[nums[j]] = 1
            else:
                val_sums[nums[j]] += j
                val_count[nums[j]] += 1

            right_count[j] -= 1
            right_sum[j] -= j

            left_count[j] = val_count[nums[j]]
            left_sum[j] = val_sums[nums[j]]

            result[j] = ((j*left_count[j])-left_sum[j]) + \
                (right_sum[j]-(j*right_count[j]))

        return result


solution = Solution()

print(solution.distance2([1, 3, 1, 1, 2]))
print(solution.distance2([0, 5, 3]))
