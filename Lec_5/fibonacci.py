def fib(x):
  """asssumes x an int x >= 0
  returns Fibonacci of x"""
  assert type(x) == int and x >= 0
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x - 1) + fib(x - 2)

x = int(raw_input("input for Fibonacci sequences: "))
print("Value corresond with input in Fibonacci squence: " + str(fib(x)))
print("Fibonacci squence: " + str(map(fib, range(x + 1))))
