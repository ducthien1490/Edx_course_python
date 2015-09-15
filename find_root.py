def findRoot(x, power, epsilon):
  if x < 0 and power%2 == 0:
    return

  low = min(-1, x)
  high = max(1, x)
  ans = (high + low)/2.0

  while abs(ans**power - x) > epsilon:
    if ans**power < x:
      low = ans
    else:
      high = ans

    ans = (high + low)/2.0
  print ans
  return ans

findRoot(0.125, 3, 0.0001)
findRoot( -0.125, 3, 0.0001)
findRoot( 4, 2, 0.0001)
findRoot( -8, 3, 0.0001)
