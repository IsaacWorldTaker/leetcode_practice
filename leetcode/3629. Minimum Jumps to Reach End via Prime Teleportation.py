from typing import List


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        pass

    def ius_prime(self, n):
        if n <= 1:
            return False
        else:
            is_prime = True  # Flag variable
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            print(is_prime)
