t = int(input())
for tc in range(1,t+1):
  n, m = map(int, input().split())
  li = [list(map(int, input().split())) for _ in range(n)]
  result = 0
  for row in range(n-m):
    for col in range(n-m):
      sum = 0
      for i in range(m):
        for j in range(m):
          sum += li[col+i][row+j]
              
          if sum > result:
            result = sum
          
  print(f"#{tc} {result}")