# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# 541. Reverse String II https://leetcode.com/problems/reverse-string-ii/description/
# Approach: move the pointer every 2k step, and it is okay if out of range, it will just point to the end
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
          text[left], text[right] = text[right], text[left]
          left += 1
          right -= 1
        return text
        
      res = list(s)

      for cur in range(0, len(s), 2 * k):
        print(cur)
        res[cur: cur + k] = reverse_substring(res[cur: cur + k])
        
      return ''.join(res)

