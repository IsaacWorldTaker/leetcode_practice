class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = {}
        n = len(s)
        result = ['i'] * n

        for i in range(n//2):
            count[s[i]] = count.get(s[i], 0)+1
        count = dict(sorted(count.items(), key=lambda item: item[0]))
        i = 0
        for c, val in count.items():
            for _ in range(val):
                result[i] = c
                result[n-i-1] = c
                i += 1
        if n % 2 != 0:
            result[n//2] = s[n//2]
        return ''.join(result)


solution = Solution()
print(solution.smallestPalindrome('z'))
print(solution.smallestPalindrome('babab'))
print(solution.smallestPalindrome('daccad'))
print(solution.smallestPalindrome('ttdacbcadtt'))
