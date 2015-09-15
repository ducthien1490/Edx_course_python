def semordnilap(str1, str2):
  if len(str1) != len(str2):
    return False
  elif len(str1) == len(str2) == 1:
    return str1 == str2
  elif str1[0] == str2[-1]:
    return semordnilap(str1[1:], str2[:-1])
  else:
    return False

str1 = raw_input("first string: ")
str2 = raw_input("second string: ")
print semordnilap(str1, str2)
