n,k = map(int,input().split())
cnt = 0
j = 0
while j != n:
  j += 1
  cnt = (cnt + k) % j


print(cnt + 1)