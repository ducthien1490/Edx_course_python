s = str(raw_input('input the string: '))
base_string = 'abcdefghijklmnopqrstuvwxyz'
ans = ''

for i in range(len(s)):
  current_ind = next_ind = base_string.index(s[i])
  j = i
  while next_ind >= current_ind:
    current_ind = base_string.index(s[j])
    j += 1
    if j == len(s):
      break
    else:
      next_ind = base_string.index(s[j])

  if len(ans) < len(s[i:j]):
    ans = s[i:j]

print ans
