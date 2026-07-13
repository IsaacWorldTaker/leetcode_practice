from typing import List
from collections import deque


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 18
        depth = [0] * (n + 1)

        up = [[0] * LOG for _ in range(n + 1)]

        # 1. Single BFS to map out depths and immediate parents (2^0 ancestors)
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    up[nei][0] = node
                    q.append(nei)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j-1] != 0:
                    up[i][j] = up[up[i][j-1]][j-1]

        def get_lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            # Jump u up until it is at the same depth as v
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # 4. Process Queries
        MOD = 10**9 + 7
        ans = []
        for u, v in queries:
            lca_node = get_lca(u, v)

            # Standard tree distance formula
            d = depth[u] + depth[v] - 2 * depth[lca_node]

            if d > 0:
                ans.append(pow(2, d - 1, MOD))
            else:
                ans.append(0)

        return ans


solution = Solution()
print(solution.assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]]))
print(solution.assignEdgeWeights(
    [[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]))
