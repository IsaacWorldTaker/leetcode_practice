class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        def compare(s, left, right, best_left, best_right):
            return s[left:right + 1] < s[best_left:best_right + 1]
        best_left, best_right = 0, 0
        left, right = 0, 0
        best_len = 200
        n = len(s)
        if n < k:
            return ""
        count = 0
        while right < n and left <= right:
            if s[right] == '0':
                right += 1
            else:
                count += 1
                while count > k or s[left] == '0':
                    # shrink
                    if s[left] == '1':
                        count -= 1
                    left += 1
                if count == k:
                    curr_len = right-left+1

                    if curr_len < best_len or (curr_len == best_len and compare(s, left, right, best_left, best_right)):
                        best_right = right
                        best_left = left
                        best_len = best_right-best_left+1
                right += 1

        return s[best_left:best_right+1] if best_len < 200 else ""


solution = Solution()
print(solution.shortestBeautifulSubstring("100011001", 3))
print(solution.shortestBeautifulSubstring("1011", 2))
print(solution.shortestBeautifulSubstring("000", 1))
print(solution.shortestBeautifulSubstring("010", 1))
print(solution.shortestBeautifulSubstring("100", 1))
