from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        rs = []
        result = ''
        mapped_range = {}
        counter = 0
        prefix = [0]
        prefix_val = [0]
        MOD = 10**9+7
        for i, char in enumerate(s):
            if char != '0':
                result += char
                prefix.append(prefix[-1]+int(char))
                prefix_val.append((prefix_val[-1] * 10 + int(char)) % MOD)
                counter += 1
            mapped_range[i] = counter

        for query in queries:
            l = mapped_range[query[0]-1] if query[0] > 0 else 0
            r = mapped_range[query[1]]
            if l == r:
                rs.append(0)
            else:
                prefix_sum = prefix[r]-prefix[l]
                x = (prefix_val[r] - prefix_val[l] * pow(10, r-l, MOD)) % MOD
                num = x*(prefix_sum % MOD)
                rs.append(num % MOD)
        return rs


solution = Solution()
print(solution.sumAndMultiply("10203004", [
      [0, 7], [1, 3], [4, 6]]) == [12340, 4, 9])
print(solution.sumAndMultiply("1000",  [[0, 3], [1, 1]]) == [1, 0])
print(solution.sumAndMultiply("9876543210", [[0, 9]]) == [444444137])
