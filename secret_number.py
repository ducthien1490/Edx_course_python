high = 100
low = 0

while True:
  guess = (high + low)/2
  print('Is your secret number ' + str(guess) + '?')
  key = str(raw_input("Enter 'h' to indicate the guess is too high." +
    " Enter 'l' to indicate the guess is too low." +
    " Enter 'c' to indicate I guessed correctly."))

  if key == "c":
    print("Game over. Your secret number was: " + str(guess))
    break
  elif key == "l":
    low = guess
  elif key == "h":
    high = guess
