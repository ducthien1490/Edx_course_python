def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    midInd= len(aStr) / 2
    if aStr == '':
      return False
    if char == aStr[midInd]:
      return True
    elif len(aStr) == 1:
      return char == aStr
    elif char > aStr[midInd]:
      print aStr[midInd: -1]
      return isIn(char, aStr[midInd:])
    elif char < aStr[midInd]:
      return isIn(char, aStr[0: midInd])

s = str(raw_input("source string: "))
c = str(raw_input("char to check: "))
print isIn(c, s)
