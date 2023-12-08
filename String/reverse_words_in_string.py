# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Approach: In stead of using string.split and reverse built in function. 
# first, trim out the leading and trailing spaces, and remove extra spaces between words
# reverse the whole string
# reverse each word in the reversed string then join all chars


class Solution:
    def trimSpaces(self, s:str) -> list:
      result= []
      left, right = 0, len(s)-1
      # trim leading and trailing spaces
      while left < right and s[left] == " ":
        left += 1
      while left < right and s[right] == " ":
        right -= 1
      
      # trim multiple spaces between words, only one space needed
      while left <= right:
        if s[left] != ' ':
          result.append(s[left])
        elif result[-1] != ' ':
          result.append(s[left])
        left += 1
      return result

    def reverse(self, left: int, right: int, l: list) -> None:
      while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    
    def reverseWord(self, l:list) -> None:
      start = end = 0
      while start < len(l):
        while end < len(l) and l[end] != " ":
          end += 1
        self.reverse(start, end-1, l)
        start = end+1
        end += 1
    
    def reverseWords(self, s: str) -> str:
      l = self.trimSpaces(s)
      self.reverse(0, len(l)-1, l)
      print(l)
      self.reverseWord(l)

      return "".join(l)