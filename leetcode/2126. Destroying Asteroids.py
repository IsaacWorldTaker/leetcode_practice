from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)

        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True


solution = Solution()
print(solution.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))
print(solution.asteroidsDestroyed(5, [4, 9, 23, 4]))
