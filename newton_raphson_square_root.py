y = int(raw_input('enter the number want to find the square root:'))
epsilon = 0.01
guess = y/2.0

while  abs(guess*guess - y) >= epsilon:
  guess = guess - ((guess**2 - y)/(2*guess))

print('Square root of ' + str(y) + 'is about ') + str(guess)
