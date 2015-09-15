def printMove(fr, to):
  print("Move from " + str(fr) + 'to' + str(to))

def Towers(n, fr, to, spare):
  if n == 1:
    printMove(fr, to)
  else:
    Towers(n - 1, fr, spare, to)
    Towers(1, fr, to, spare)
    Towers(n - 1, spare, to, fr)

inputVal = raw_input("input level of Tower, from, to and spare separated by comma: ").split(",")
Towers(int(inputVal[0]), inputVal[1], inputVal[2], inputVal[3])
