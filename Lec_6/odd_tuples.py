def oddTuples(aTup):
    ans = ()
    for i in range(0, len(aTup)):
      if (i+1) % 2 != 0:
        ans += (aTup[i],)
    return ans

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
