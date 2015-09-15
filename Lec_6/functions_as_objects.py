def applyToEach(L, f):
  """ assume that L is a list, f is a function
  """
  for i in range(len(L)):
    L[i] = f(L[i])

def biggest(aDict):
    if len(aDict) == 0:
      return
    maxVal = max(map(sum, aDict.values()))
    for k in aDict.keys():
      if sumaDict[k] == maxVal:
        print aDict[k]
        return aDict[k]

biggest({'a': [15, 5, 13], 'b': [12, 6, 19, 16, 13, 16, 0]})
biggest({})
biggest({'g': []})
biggest({'a': [], 'c': [17, 17, 0, 16], 'b': [12, 20], 'e': [10, 6, 6, 16, 8, 1, 20], 'd': [2, 8, 7, 6, 7, 16, 20, 5]})
biggest({'a': [10], 'c': [3, 5, 6, 11, 0, 3, 20], 'b': [8, 14], 'd': [9, 0, 6, 11, 1, 10, 2, 12, 10]})
