# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/description/
# Using collections.Counter https://docs.python.org/3/library/collections.html#counter-objects
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = Counter(words[0])
        for i in words:
            l &= Counter(i)
        
        return list(l.elements())

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]