# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

#459. Repeated Substring Pattern https://leetcode.com/problems/repeated-substring-pattern/description/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range (1, n//2+1):
          if n % i == 0:
            pattern = s[:i]*(n//i)
            if s == pattern: return True
        
        return False