from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = [False]*n
        self.graph = defaultdict(list)
        for u, v in invocations:
            self.graph[u].append(v)

        visited = [False]*n

        stack = []
        stack.append(k)
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in self.graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        return [i for i in range(n) if not visited[i]]

    def dfs(self, v, visited):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, visited)


solution = Solution()
print(solution.remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]]))
print(solution.remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))
print(solution.remainingMethods(3, 2, [[1, 2], [0, 1], [2, 0]]))
