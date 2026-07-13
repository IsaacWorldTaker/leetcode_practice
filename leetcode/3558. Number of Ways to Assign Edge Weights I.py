from collections import deque


class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges):
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find maximum depth from root (node 1)
        q = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True

        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, depth + 1))

        # Number of odd-parity assignments = 2^(d-1)
        return pow(2, max_depth - 1, self.MOD)


solution = Solution()
print(solution.assignEdgeWeights([[1, 2]]))
print(solution.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))
