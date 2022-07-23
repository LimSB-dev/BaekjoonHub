t = int(input())
for _ in range(t):
  n = int(input())
  li = []
  for i in range(n):
    a,b = map(int,input().split())
    li.append([a,b])
  li.sort(key = lambda x: x[0])
  cnt = 1
  min = li[0][1]
  for j in range(1,n):
    if li[j][1] < min:
      cnt += 1
      min = li[j][1]
  print(cnt)