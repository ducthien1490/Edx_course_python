def gcdIter(a, b):
  result = min(a, b)
  while result >= 1:
    if b % result == 0 and a % result == 0:
      break
    result -= 1
  return result

def gcdRecur(a, b):
  if a > b:
    return gcdRecur(b, a)
  if b % a == 0:
    return a
  else:
    return gcdRecur(a, b%a)
x = float(raw_input("x: "))
y = float(raw_input("y: "))
print("greatest divisor of x and y is: " + str(gcdRecur(x, y)))
