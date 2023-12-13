# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

# 253. Meeting Room II https://leetcode.com/problems/meeting-rooms-ii/description/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for s, t in intervals:
            start.append(s)
            end.append(t)
        
        start.sort()
        end.sort()
        
        i = j = 0
        max_room = 0
        current_room = 0
        while i < len(start):
            if start[i] < end[j]:
                current_room += 1
                i += 1
            else:
                j += 1
                current_room -=1
            max_room = max(max_room, current_room)
        
        return max_room