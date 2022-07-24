n = int(input())
c = 6
path = 1

while n > 1:
  n -= c
  path += 1
  c += 6

print(path)