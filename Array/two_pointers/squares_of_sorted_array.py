# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# approach: the max will only be on the left or on the right, 
# so create a new array, and starting to fill in number from the right -> left (largest -> smallest)
# everytime we only need to compare left and right value of the original array and fill in the new array with the bigger num

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        reorder = [0]*len(nums)

        left, right, k = 0, len(nums) - 1, len(nums) - 1
        while k >= 0:
            if nums[left] ** 2 < nums[right] ** 2:
                reorder[k] = nums[right] ** 2
                k -= 1
                right -= 1
            else:
                reorder[k] = nums[left] ** 2
                k -= 1
                left += 1
        
        return reorder