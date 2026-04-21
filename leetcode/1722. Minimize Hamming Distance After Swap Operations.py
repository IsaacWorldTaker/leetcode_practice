from tokenize import group
from typing import List
from collections import defaultdict, Counter


class UnionFind:
    def __init__(self, size):

        self.parent = list(range(size))

    def find(self, i):

        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):

        irep = self.find(i)

        jrep = self.find(j)

        self.parent[irep] = jrep


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = self.make_adjacency_list(allowedSwaps)
        visited = [False] * len(source)
        hamming_dist = len(source)
        for i in range(len(source)):
            if not visited[i]:
                # Start a new component
                component = []
                island_counter = Counter()

                stack = [i]
                visited[i] = True  # Mark when pushing!

                while stack:
                    node = stack.pop()
                    component.append(node)
                    island_counter[source[node]] += 1

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                """
                If the component contains indices [0, 4, 2], then:
                    source[0], source[4], source[2] are the values we have. (You put these in the island_counter).
                    target[0], target[4], target[2] are the values we need to fill those exact same positions to get a Hamming distance of 0.
                """
                for i in component:
                    if island_counter[target[i]]:
                        hamming_dist -= 1
                        island_counter[target[i]] -= 1
        return hamming_dist

    def make_adjacency_list(self, nodes):
        graph = defaultdict(list)
        for node in nodes:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        return graph

    def minimumHammingDistanceUnion(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]):
        union = UnionFind(len(source))
        hamming_dist = len(source)
        # We avoid using defaultdict and Counter as they add up significant overhead in large iterations (100000+)
        groups = {}
        for pair in allowedSwaps:
            union.unite(pair[0], pair[1])

        for i, value in enumerate(source):
            root = union.find(i)
            if not groups.get(root):
                groups[root] = {}
            if groups[root].get(value):
                groups[root][value] += 1
            else:
                groups[root][value] = 1

        for i in range(len(target)):
            root = union.find(i)
            if groups[root].get(target[i]):
                hamming_dist -= 1
                groups[root][target[i]] -= 1
        return hamming_dist


example_1 = [[0, 1], [2, 3]]
example_2 = [[0, 4], [4, 2], [1, 3], [1, 4]]
example_3 = [[24, 30], [27, 46], [7, 12], [9, 41], [35, 41], [46, 17], [42, 24], [14, 31], [35, 20], [45, 3], [11, 22], [25, 6], [11, 27], [0, 4], [23, 44], [27, 10], [20, 13], [35, 10], [12, 37], [37, 41], [18, 46], [8, 21], [24, 5], [26, 28], [19, 24], [40, 1], [32, 35], [29, 37], [41, 6], [17, 39], [33, 15], [14, 5], [20, 42], [1, 43], [32, 22], [6, 39], [18, 2], [1, 26], [19, 44], [44, 38], [33, 1], [31, 24], [14, 22], [27, 21], [32, 45], [42, 25], [35, 38], [2, 43], [39, 35], [
    25, 37], [43, 3], [2, 33], [42, 10], [33, 31], [11, 39], [27, 4], [26, 10], [33, 4], [31, 43], [19, 2], [28, 17], [25, 13], [30, 2], [38, 14], [13, 4], [18, 38], [38, 4], [7, 27], [33, 6], [23, 17], [1, 4], [0, 12], [44, 34], [41, 15], [3, 26], [0, 34], [21, 32], [13, 7], [21, 29], [33, 10], [0, 46], [42, 33], [43, 7], [25, 36], [5, 6], [37, 30], [24, 11], [1, 29], [34, 18], [8, 20], [35, 2], [12, 21], [46, 41], [31, 2], [12, 38], [38, 0], [4, 20], [26, 27], [36, 45], [32, 24], [4, 30]]


solution = Solution()
print(solution.minimumHammingDistanceUnion(
    [1, 2, 3, 4], [2, 1, 4, 5], example_1))
print(solution.minimumHammingDistanceUnion([1, 2, 3, 4],  [1, 3, 2, 4], []))
print(solution.minimumHammingDistanceUnion(
    [5, 1, 2, 4, 3], [1, 5, 4, 2, 3], example_2))

print(solution.minimumHammingDistanceUnion(
    [7, 13, 53, 16, 56, 16, 73, 31, 82, 8, 67, 97, 40, 16, 54, 35, 55, 36, 95, 48, 71, 72, 70, 44, 51, 42, 27, 28, 18, 71, 17, 99, 92, 98, 2, 34, 29, 30, 18, 86, 13, 92, 11, 76, 29, 29, 72], [7, 89, 53, 62, 56, 16, 73, 32, 41, 5, 8, 93, 69, 16, 44, 26, 97, 82, 92, 48, 8, 69, 28, 85, 60, 42, 7, 99, 19, 59, 64, 7, 27, 10, 58, 48, 29, 83, 4, 84, 55, 65, 96, 26, 31, 89, 39], example_3))
