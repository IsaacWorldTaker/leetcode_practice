from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count_A = {}
        count_B = {}
        result = []
        prefix_sum = set()
        for i in range(len(A)):
            count_A[A[i]] = count_A.get(A[i], 0) + 1
            count_B[B[i]] = count_B.get(B[i], 0) + 1
            if A[i] in count_B:
                prefix_sum.add(A[i])
            if B[i] in count_A:
                prefix_sum.add(B[i])
            result.append(len(prefix_sum))
        return result


solution = Solution()
print(solution.findThePrefixCommonArray([1, 3, 2, 4],  [3, 1, 2, 4]))
print(solution.findThePrefixCommonArray([2, 3, 1],   [3, 1, 2]))
