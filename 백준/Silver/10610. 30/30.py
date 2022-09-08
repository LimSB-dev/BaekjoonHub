n = list(map(int,input().strip()))
n.sort(reverse=True)
if 0 in n:
  if sum(n) % 3 ==0:
    for i in range(len(n)):
      print(n[i],end='')
  else:
    print(-1)
else:
  print(-1)