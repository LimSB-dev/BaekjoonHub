a, b, c = list(map(int,input().split()))
if c > b:
  
  d = c-b
  e = a//d
  print(e+1)
else:
  print('-1')