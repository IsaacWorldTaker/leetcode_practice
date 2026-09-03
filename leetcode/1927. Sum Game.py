class Solution:
    def sumGame(self, num: str) -> bool:
        left = 0
        right = 0
        sum_left = 0
        sum_right = 0
        half = len(num)//2
        for i in num[:half]:
            if i == '?':
                left += 1
            else:
                sum_left += int(i)
        for i in num[half:]:
            if i == '?':
                right += 1
            else:
                sum_right += int(i)
        extra = left - right

        if extra > 0:
            sum_left += 9*(extra/2)
        if extra < 0:
            sum_right += 9*(-extra/2)

        final_diff = sum_left-sum_right
        if extra == 0 and final_diff == 0:
            return False
        return final_diff != 0


solution = Solution()
# print(solution.sumGame("5023"))
# print(solution.sumGame("25??"))
# print(solution.sumGame("?3295???"))
print(solution.sumGame(
    "?0?3105????1834??7382?997?3?????7?63116?566?701?065?13?3??38?7?488?????9"))
