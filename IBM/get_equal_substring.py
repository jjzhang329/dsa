# 1208. Get Equal Substrings Within Budget 
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
# Example 1:
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.

# Example 2:
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

# Example 3:
# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You cannot make any change, so the maximum length is 1.
# Approach, using sliding window, left side += 1 until reach maxCost, 
# right side += 1 if cost > maxCost
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = j = cost = 0
        max_length = 0
        while j < len(s):
            cost += abs(ord(s[j]) - ord(t[j]))
            
            while cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            max_length = max(max_length, j-i+1)
            j += 1
        
        return max_length