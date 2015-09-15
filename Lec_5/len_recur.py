def lenRecur(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
      return 0
    elif aStr.rfind(aStr[-1]) == 0:
      print(aStr + " " + aStr[-1])
      return 1
    else:
      return 1 + lenRecur(aStr[0: -1])

s = raw_input("string to test palindrome: ")
print("length of string: " + str(lenRecur(s)))
