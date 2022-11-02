import math
n = int(input())
li = list(map(int,input().split()))
a,b = map(int,input().split())
s = sum(li)
cnt = 0
cnt += len(li)

for i in range(n):
  li[i] -= a

  if li[i] > 0:
    cnt += math.ceil(li[i] / b)
  
print(cnt)