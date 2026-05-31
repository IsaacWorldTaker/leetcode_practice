from typing import List
from collections import deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Using a regular BFS
        repeat = {}
        for i, num in enumerate(arr):
            if num in repeat:
                repeat[num].append(i)

            else:
                repeat[num] = [i]

        path = deque([(0, 0)])
        visited = {0}
        while path:
            node, dist = path.popleft()
            if node == len(arr)-1:
                return dist
            window = repeat.pop(arr[node], [])
            for nei in window:
                if nei not in visited:
                    visited.add(nei)
                    path.append((nei, dist + 1))
            if node+1 < len(arr) and node+1 not in visited:
                path.append((node+1, dist + 1))
                visited.add(node+1)

            if node-1 >= 0 and node-1 not in visited:
                path.append((node-1, dist + 1))
                visited.add(node-1)

    def minJumps2(self, arr: List[int]) -> int:
        # Using a bidirectional BFS
        repeat_start = {}
        total_distance = []
        repeat_end = {}
        for i, num in enumerate(arr):
            if num in repeat_start:
                repeat_start[num].append(i)
                repeat_end[num].append(i)
            else:
                repeat_end[num] = [i]
                repeat_start[num] = [i]

        path_start = deque([(0, 0)])
        path_end = deque([(len(arr)-1, 0)])
        # Create two separete sets of visited lists
        visited_start = {0: 0}
        visited_end = {len(arr)-1: 0}

        while path_start and path_end:
            if len(path_start) > len(path_end):
                node, dist = path_end.popleft()

                if node in visited_start:
                    total_distance.append(dist+visited_start[node])

                window = repeat_end.get(arr[node], [])

                for nei in window:
                    if nei not in visited_end:
                        visited_end[nei] = dist+1
                        path_end.append((nei, dist + 1))
                if node+1 < len(arr) and node+1 not in visited_end:
                    path_end.append((node+1, dist + 1))
                    visited_end[node+1] = dist + 1

                if node-1 >= 0 and node-1 not in visited_end:
                    path_end.append((node-1, dist + 1))
                    visited_end[node-1] = dist + 1
                repeat_end.pop(arr[node], None)
            else:
                node, dist = path_start.popleft()
                if node in visited_end:
                    total_distance.append(dist+visited_end[node])
                window = repeat_start.get(arr[node], [])
                for nei in window:
                    if nei not in visited_start:
                        visited_start[nei] = dist+1
                        path_start.append((nei, dist + 1))
                if node+1 < len(arr) and node+1 not in visited_start:
                    path_start.append((node+1, dist + 1))
                    visited_start[node+1] = dist+1

                if node-1 >= 0 and node-1 not in visited_start:
                    path_start.append((node-1, dist + 1))
                    visited_start[node-1] = dist+1
                repeat_start.pop(arr[node], None)
        return min(total_distance)


solution = Solution()
print(solution.minJumps2([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))  # 2
print(solution.minJumps2([7]))  # 0
print(solution.minJumps2([7, 6, 9, 6, 9, 6, 9, 7]))  # 1
print(solution.minJumps2([1, 6, 9, 6, 9, 6, 7, 5, 8, 7]))  # 4
print(solution.minJumps2([-68, 59, 59, 25, -38, 25, -56, -77, -17, -17, 72, -76, -74, -38, 12, -96, -74, -38, 72, -96, 1, 81, -17, 66, -76, -17, 70, 16, -17, 36, -68, 70, 1, -68, 25, -12, 12, -74, 36, -56, 16, 82,
      72, -96, -17, 45, -12, -12, -38, -17, 25, -76, -17, 35, 76, 76, 45, -76, -17, -96, 70, -38, 35, -17, 1, 81, -38, -17, -17, -56, -38, 25, 16, 12, 57, -74, -74, -76, 57, -17, 1, 12, -96, -38, 70, -38, 16, 25, -17]))  # 4
