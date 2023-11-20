def pair_sum(numbers, target_sum):
  dict = {}
  
  for idx in range(len(numbers)):
    current = numbers[idx]
    diff = target_sum - current
    if current not in dict:
      dict[diff] = idx 
    else:
      return (dict[current], idx)

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
