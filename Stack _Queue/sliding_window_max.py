# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Approach, monotonic descending queue
# using deque, numbers in the window should be decreasing, so dq[0] is always the largest
# 1. put in first k nums to find the first max
# 2. push if new num is less than the last ele in queue, otherwise pop
# 3. pop from the left if left side is out of window bound, i - k == dq[0]
# Note: save the indices in dq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
        
            dq.append(i)
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            # i = 3
            if dq and dq[0] == i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        return res