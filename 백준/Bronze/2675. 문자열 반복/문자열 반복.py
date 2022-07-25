t = int(input())
for i in range(t):
  r, a = input().split()
  r = int(r) 
  b = ''
  for i in a:
    b += r*i
  print(b)