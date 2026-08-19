from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def max_diff(left, right):
            if left == right:
                return piles[left]
            if (left, right) in memo:
                return memo[(left, right)]

            pick_left = piles[left]-max_diff(left+1, right)
            pick_right = piles[right]-max_diff(left, right-1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return max_diff(0, len(piles)-1) >= 0


solution = Solution()
print(solution.stoneGame([5, 3, 4, 5]))
print(solution.stoneGame([3, 7, 2, 3]))
