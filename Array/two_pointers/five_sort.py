def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while i != j:
    num = nums[i]
    if num == 5:
      nums[i] = nums[j]
      nums[j] = num
      j -= 1
    else:
      i += 1  
  return nums
five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]

five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
# -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 
