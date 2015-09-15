def iterPower(base, exp):
  result = 1
  while exp > 0:
    result *= base
    exp -= 1
  return result

def recurMul(a, b):
  if b == 1:
    return a
  else:
    return a + recurMul(a, b - 1)

x = float(raw_input("x: "))
y = float(raw_input("y: "))
print("x^y = " + str(iterPower(x, y)))
print("recursion x*y = " + str(recurMul(x, y)))
