def findDivisors(x , y):
  divisors = ()
  for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
      divisors += (i,)
  print divisors
  return divisors

findDivisors(12, 16)
findDivisors(7, 9)
findDivisors(60, 48)
