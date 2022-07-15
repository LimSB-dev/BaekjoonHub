t = int(input())


for i in range(1,t+1):
  n = int(input())
  li = list(map(int,input().split()))
  max = 0
  sum = 0
  for j in range(n-1,-1,-1):
    if li[j] > max:
      max = li[j]
    else:
      sum += max - li[j]
  
  print('#%d %d'%(i, sum))