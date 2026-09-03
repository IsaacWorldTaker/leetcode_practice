from typing import List

from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        litter_positions = []
        start_pos = (0, 0)
        rows, cols = len(classroom), len(classroom[0])
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_pos = (r, c)
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
        target_mask = (1 << len(litter_positions))-1
        # Queue: (moves, r,c,mask,curren_enery)
        q = deque([(0, start_pos[0], start_pos[1], 0, energy)])

        visited = {}
        visited[(start_pos[0], start_pos[1], 0)] = energy
        if target_mask == 0:
            return 0

        while q:
            moves, r, c, mask, curr_energy = q.popleft()

            if curr_energy == 0:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r+dr, c+dc
                if 0 <= new_r < rows and 0 <= new_c < cols and classroom[new_r][new_c] != 'X':
                    next_energy = curr_energy-1
                    if classroom[new_r][new_c] == 'R':
                        next_energy = energy
                    next_mask = mask
                    if classroom[new_r][new_c] == 'L':
                        litter_index = litter_positions.index((new_r, new_c))
                        next_mask |= (1 << litter_index)

                    if next_mask == target_mask:
                        return moves + 1
                    state = (new_r, new_c, next_mask)
                    if state not in visited or visited[state] < next_energy:
                        visited[state] = next_energy
                        q.append((moves+1, new_r, new_c,
                                 next_mask, next_energy))
        return -1
