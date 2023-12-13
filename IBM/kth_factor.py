# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

# Example 1:
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

# Example 2:
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example 3:

# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

# 1492. The kth Factor of n https://leetcode.com/problems/the-kth-factor-of-n/description/
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Math logic here is that N // diviros[len(divisor) - k] when k > divisor list but <= factor list
        # divisor list only up to the sqrt of N, and factor list is the full list of factors

        divisor = []
        sqrt = int(n**0.5)
        for i in range(1, sqrt+1):
            if n % i == 0:
                k -=1
                divisor.append(i)
            if k == 0:
                return i

        # now if k is not yet 0, and we dont want to double count sqrt factor twice
        if sqrt**2 == n:
            k += 1
        
        return n // divisor[len(divisor)-k] if k <= len(divisor) else -1