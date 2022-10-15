n = int(input())
li = []
for i in range(n):
  x, y = map(int, input().split())
  li.append([x, y])

li.sort(key = lambda x: (x[0],x[1]))

for i in range(n):
  print(f'{li[i][0]} {li[i][1]}')