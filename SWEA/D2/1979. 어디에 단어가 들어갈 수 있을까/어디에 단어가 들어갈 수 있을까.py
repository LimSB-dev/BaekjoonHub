t = int(input())
for tc in range(1, t+1):
  n, k = map(int,input().split())
  li = [list(map(int, input().split())) for _ in range(n)]
  result = 0

  for col in range(n):
    count = 0
    for row in range(n):
      if li[col][row] == 1:
        count += 1
        if count == k:
          result += 1
        elif count > k:
          result -= 1
          count = 0
      else:
        count = 0

  for row in range(n):
    count = 0
    for col in range(n):
      if li[col][row] == 1:
        count += 1
        if count == k:
          result += 1
        elif count > k:
          result -= 1
          count = 0
      else:
        count = 0

  print(f"#{tc} {result}")