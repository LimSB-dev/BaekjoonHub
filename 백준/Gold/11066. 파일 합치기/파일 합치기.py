import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  li = list(map(int,input().split()))
  cumsum = {-1:0}
  for i in range(len(li)):
    cumsum[i] = cumsum[i-1] + li[i]

  dp = [[0 for _ in range(len(li))] for _ in range(len(li))]

  for gap in range(1,len(li)):
    for start in range(len(li)):
      end = start + gap
      if end == len(li):
        break
      dp[start][end] = math.inf
      for i in range(start, end):
        dp[start][end] = min(dp[start][end],dp[start][i] + dp[i+1][end] + cumsum[end] - cumsum[start-1])

  print(dp[0][-1])

