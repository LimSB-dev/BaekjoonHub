n = set(range(1,10001))
N = set()
for i in range(1,10001):
  for j in str(i):
    i+=int(j)
  N.add(i)
s = n-N
for i in sorted(s):
  print(i)