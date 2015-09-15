def recurFactorial(x):
  if x == 1:
    return 1
  return x*recurFactorial(x-1)

def recurPower(base, exp):
  if exp == 0:
    return 1
  return base*recurPower(base, exp - 1)

def recurPowerNew(base, exp):
  if exp == 0:
    return 1
  elif exp % 2 == 0:
    return recurPowerNew(base*base, exp/2)
  else:
    return base*recurPowerNew(base, exp - 1)

x = float(raw_input("x or base: "))
exp = int(raw_input("exp: "))

print("recursion x! = " + str(recurFactorial(x)))
print("recursion x^base = " + str(recurPower(x, exp)))
print("recursion new x^base = " + str(recurPowerNew(x, exp)))
