t = int(input())
for tc in range(1,t+1):
  n = int(input())
  li = sorted(list(map(int, input().split())))

  m = li[0]
  M = li[n-1]
  
  if n > 1:
    print(f"#{tc} {M-m}")
  else:
    print(f"#{tc} {m}")