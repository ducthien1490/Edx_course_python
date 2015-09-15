def isPalindrome(s):
  def toChars(s):
    s = s.lower()
    ans = ""

    for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans += c
    return ans

  def isPal(s):
    if len(s) <= 1:
      return True
    else:
      return s[0] == s[-1] and isPal(s[1:-1])

  return isPal(toChars(s))

s = raw_input("string to test palindrome: ")
print("new char is palindrome: " + str(isPalindrome(s)))