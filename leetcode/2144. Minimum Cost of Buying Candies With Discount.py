from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(0, len(cost), 3):
            total_cost += sum(cost[i : min(i + 2, len(cost))])
        return total_cost


solution = Solution()
print(solution.minimumCost([1, 2, 3]))
print(solution.minimumCost([6, 5, 7, 9, 2, 2]))
print(solution.minimumCost([5, 5]))
print(solution.minimumCost([3, 3, 3, 1]))
