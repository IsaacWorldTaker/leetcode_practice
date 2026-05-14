from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        frequency = [0]*(2*limit+2)
        diff = [0]*(2*limit+2)

        for i in range(n//2):
            target_sum = nums[i] + nums[n-1-i]
            start = min(nums[i], nums[n-1-i])+1
            end = max(nums[i], nums[n-1-i])+limit
            diff[start] += 1
            diff[end+1] -= 1
            frequency[target_sum] += 1

        one_move_sum = 0
        min_moves = float('inf')
        for i in range(2, 2*limit+1):
            one_move_sum += diff[i]
            moves = n-one_move_sum-frequency[i]
            if moves < min_moves:
                min_moves = moves

        return min_moves


solution = Solution()
print(solution.minMoves([1, 2, 3, 4, 5, 6], 8))
