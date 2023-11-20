def compress(s):
  s += '!'
  result = ''
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      count = j - i
      if count == 1:
        result += s[i]
      else:
        result += str(count) + s[i]
      i = j
  return result 

print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('ssssbbz')) # -> '4s2bz'
