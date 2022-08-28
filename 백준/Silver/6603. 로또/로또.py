from itertools import combinations

while True:
  li = list(map(int,input().split()))
  k = li[0]

  if k == 0:
    break

  s = li[1:]
  
  for i in combinations(s,6):
    for j in i:
      print(j,end=' ')
    print() 
  print()