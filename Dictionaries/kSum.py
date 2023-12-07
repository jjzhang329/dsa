#generic solution for KSum, k = 4 => 4Sum question

class Solution:
    def fourSum(nums, target):
      nums.sort()
      res, quad = [], []

      def kSum(k, start, target):
        if k !=2: 
          for i in range(start, len(nums)-k+1):
            if i > start and nums[i] == nums[i-1]: continue
            quad.append(nums[i])
            print(quad, start, k)
            kSum(k-1, i+1, target-nums[i])
            
            quad.pop()
          return

        l, r = start, len(nums)-1
        while l < r:
          if nums[l] + nums[r] < target:
            l += 1
          elif nums[l] + nums[r] > target:
            r -= 1
          else:
            res.append(quad + [nums[l], nums[r]])
            l += 1
            while l <  r and nums[l] == nums[l-1]:
              l += 1

      kSum(4, 0, target)
      return res
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution.fourSum([1,0,-1,0,-2,2], 0))