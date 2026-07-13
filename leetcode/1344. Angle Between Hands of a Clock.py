class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # caclulate hour angle with 12
        min_angle = 360*minutes/60
        h_angle = 360*((hour/12)+(minutes/(60*12)))
        angle = abs(h_angle-min_angle)
        return min(angle, abs(360-angle))


solution = Solution()
print(solution.angleClock(12, 30))
print(solution.angleClock(3, 30))
print(solution.angleClock(3, 15))
