from math import floor, sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        win = [False]*(n+1)

        for i in range(n+1):
            for s in range(1, floor(sqrt(i))+1):
                if win[i-(s*s)] == False:
                    win[i] = True
                    break
        return win[n]


solution = Solution()
print(solution.winnerSquareGame(1))
print(solution.winnerSquareGame(2))
print(solution.winnerSquareGame(4))
print(solution.winnerSquareGame(3))
print(solution.winnerSquareGame(90))
