from typing import List
from math import inf


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        dp = [[inf]*len(robot) for _ in range(len(factory))]
        robot.sort()
        factory.sort()
        for j in range(len(factory)):
            for i in range(len(robot)):
                values = []

                for k in range(1, min(factory[j][1], i+1)+1):
                    if j == 0:
                        prev = 0 if k == i+1 else inf
                    else:
                        prev = dp[j-1][i-k]
                    values.append(
                        prev + sum(abs(robot[z] - factory[j][0]) for z in range(i-k+1, i+1)))
                if j > 0:
                    values.append(dp[j-1][i])
                dp[j][i] = min(values)

        return dp[-1][-1]


solution = Solution()
# print(solution.minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]]))
print(solution.minimumTotalDistance([1, -1], [[-2, 1], [2, 1]]))
print(solution.minimumTotalDistance([789300819, -600989788, 529140594, -592135328, -840831288, 209726656, -671200998], [[-865262624, 6], [-717666169, 0], [725929046, 2], [449443632, 3], [-912630111, 0], [
      270903707, 3], [-769206598, 2], [-299780916, 4], [-159433745, 5], [-467185764, 3], [849991650, 7], [-292158515, 6], [940410553, 6], [258278787, 0], [83034539, 2], [54441577, 3], [-235385712, 2], [75791769, 3]]))
