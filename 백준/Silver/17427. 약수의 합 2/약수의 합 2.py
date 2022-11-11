def g(x):
  s = 0
  for i in range(1,x+1):
    s += i * (x//i)
  return s

n = int(input())
print(g(n))