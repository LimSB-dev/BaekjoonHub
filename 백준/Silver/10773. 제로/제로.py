import sys
input = sys.stdin.readline
print = sys.stdout.write

k = int(input())
li = []
for _ in range(k):
  n = int(input())
  if n == 0:
    li.pop()
  else:
    li.append(n)
print(f'{sum(li)}')