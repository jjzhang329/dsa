def uncompress(s):
  result = ''
  numbers = '0123456789'
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else: 
      num = int(s[i:j])
      result += num * s[j]
      j += 1
      i = j
      
  return result

print(uncompress("2c3a1t")) # -> 'ccaaat'
print(uncompress("4s2b")) # -> 'ssssbb'
print(uncompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'

