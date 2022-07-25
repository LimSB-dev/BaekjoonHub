import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
dp = []

if n == 1:
  print(li[0])

elif n == 2:
  print(li[0]+li[1])

elif n == 3:
  print(max(li[0]+li[2],li[1]+li[2]))

else:
  dp.append(li[0])
  dp.append(li[0]+li[1])
  dp.append(max(li[0]+li[2], li[1]+li[2]))
  for i in range(3,n):
    dp.append(max(li[i] + li[i-1] + dp[i-3], li[i] + dp[i-2]))
  print(dp[-1])