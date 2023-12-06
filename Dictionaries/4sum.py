# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#18. 4Sum https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        size = len(nums)
        for i in range(size):
          if nums[i] > target and target > 0: break
          if i > 0 and nums[i] == nums[i-1]: continue

          for j in range(i+1, size):
            if nums[j] + nums[i] > target and target > 0: break
            if j > i+1 and nums[j] == nums[j-1]: continue
          
            l, r = j+1, size-1
            while l < r:
              sum = nums[i] + nums[j] + nums[l] + nums[r]
              if sum == target:
                res.append([nums[i], nums[j], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                  l += 1
                while l < r and nums[r] == nums[r-1]:
                  r -= 1
                l += 1
                r -= 1
              elif sum > target:
                r -= 1
              else:
                l += 1
          
        return res

#Time and Space: o(n^3)