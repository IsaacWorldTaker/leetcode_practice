from typing import List


class Solution:
    def canReach(self, nums: List[int], start: int) -> int:
        n = len(nums)
        visited = [False]*n

        queue = []
        queue.append(start)

        while queue:
            node = queue.pop()
            if not visited[node]:
                if nums[node] == 0:
                    return True
                visited[node] = True
                if node+nums[node] < n:
                    queue.append(node+nums[node])
                if node-nums[node] >= 0:
                    queue.append(node-nums[node])

        return False


solution = Solution()
print(solution.canReach([4, 2, 3, 0, 3, 1, 2], 5))
print(solution.canReach([4, 2, 3, 0, 3, 1, 2], 0))
print(solution.canReach([3, 0, 2, 1, 2], 2))
