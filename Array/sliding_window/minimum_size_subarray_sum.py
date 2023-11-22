# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Approach: have a sliding window, once sum in the window is greater than target, shrink the window from left

def minSubArrayLen(target, nums):
    left = 0
    right = 0
    sum = 0
    min_sub = float('inf')
    while right < len(nums):
        sum += nums[right]
        if sum >= target:
            min_sub = min(min_sub, right-left-1)
            left += 1
            sum -= nums[left]
        
        right += 1
    
    return min_sub if min_sub != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))            