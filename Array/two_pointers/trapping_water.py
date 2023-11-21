# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
# https://leetcode.com/problems/trapping-rain-water/description/

# approach: finding left_max and right_max, water trapped by min of left or right

class Solution(object):
    def trap(self, height):

        left = 0 
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        
        return water
