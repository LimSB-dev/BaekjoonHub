t = int(input())
for tc in range(t):
  n, m = map(int,input().split())
  li_n = list(map(int, input().split()))
  li_m = list(map(int, input().split()))
  result = 0
  
  for i in range(abs(n-m)+1):
    sum = 0
    for j in range(min(n,m)):
      if len(li_n) > len(li_m):
        sum += li_n[i+j] * li_m[j]
      elif len(li_m) > len(li_n):
        sum += li_n[j] * li_m[i+j]
      else:
        sum += li_n[j] * li_m[j]

    if sum > result:
      result = sum

  print(f"#{tc+1} {result}")