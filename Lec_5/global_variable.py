def fibMetterd(x):
  global numCalls
  numCalls += 1
  if x == 0 or x == 1:
    return 1
  else:
    return fibMetterd(x - 1) + fibMetterd(x - 2)

def testFib(n):
  for i in range(n + 1):
    global numCalls
    numCalls = 0
    print('fib of ' + str(i) + ' = ' + str(fibMetterd(i)))
    print('fib called ' + str(numCalls) + ' times')

n = int(raw_input("n: "))
testFib(n)
