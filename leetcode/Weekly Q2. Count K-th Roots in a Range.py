

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        count = 0
        for i in range(round(l**(1/k)), round(r**(1/k))+1):
            if i**k in range(l, r+1):
                count += 1

        return count


solution = Solution()
# print(solution.countKthRoots(1, 9, 3))
# print(solution.countKthRoots(8, 30, 2))
print(solution.countKthRoots(30, 64, 3))
