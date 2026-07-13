class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0]
        current_len = 0

        for char in s:
            if char.islower():
                current_len += 1
            elif char == '*':
                if current_len > 0:
                    current_len -= 1
            elif char == '#':
                current_len *= 2
            elif char == '%':
                # Reversal doesn't change the length
                pass
            lengths.append(current_len)

        # Edge case: If k is completely out of bounds of the final string
        if k < 0 or k >= lengths[-1]:
            return '.'

        # Pass 2: Trace k backward
        for i in range(len(s) - 1, -1, -1):
            char = s[i]

            # If the string was empty at this point, we can't look back further
            if lengths[i+1] == 0:
                continue

            if char.islower():
                # If k is pointing to the very last character added
                if k == lengths[i+1] - 1:
                    return char
                # Otherwise, this character wasn't the one, it just shifted things by 1
                # (Implicitly handled because lengths[i] will be lengths[i+1] - 1)

            elif char == '*':
                # If the current character was deleted by a '*', it means
                # the backward pass needs to skip the character that gets deleted.
                # The forward pass accounted for this reduction.
                pass

            elif char == '#':
                prev_len = lengths[i]
                # If k falls in the duplicated second half, wrap it back to the first half
                if k >= prev_len:
                    k -= prev_len

            elif char == '%':
                prev_len = lengths[i]
                # Reverse maps index k to: (length - 1) - k
                if prev_len > 0:
                    k = prev_len - 1 - k

        return '.'


solution = Solution()
print(solution.processStr('a#b%*', 1))
print(solution.processStr("cd%#*#", 3))
print(solution.processStr("z*#", 0))
