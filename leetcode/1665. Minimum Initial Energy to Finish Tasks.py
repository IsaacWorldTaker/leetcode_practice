from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        sorted_arr = sorted(tasks, key=lambda x: x[1]-x[0], reverse=True)
        min_energy = 0
        actual = 0
        for x in sorted_arr:
            min_energy = max(min_energy, actual+x[1])
            actual += x[0]
        return min_energy
        # arr = np.array(tasks)
        # sum_min_energy = arr[:, 1].sum()

        # # for sum((n-1-i)ai)
        # sum_actual_energy = arr[:, 0].sum()
        # weighted_sum = (np.arange(len(arr)) * arr[:, 0]).sum()

        # return (sum_min_energy+weighted_sum+(n-1)*sum_actual_energy)/n


solution = Solution()
print(solution.minimumEffort([[1, 2], [2, 4], [4, 8]]))
print(solution.minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
print(solution.minimumEffort(
    [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
