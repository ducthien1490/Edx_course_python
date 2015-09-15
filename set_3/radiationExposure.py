def f(x):
  import math
  ans = 10*math.e**(math.log(0.5)/5.27 * x)
  #print ans
  return ans

def radiationExposure(start, stop, step):
  period = start
  radiation = 0
  while period < stop:
    radiation += f(period)*step
    period += step
    print radiation

  return radiation

radiationExposure(0, 5, 1)
"""
radiationExposure(5, 11, 1)
radiationExposure(0, 11, 1)
radiationExposure(40, 100, 1.5)
"""
