t= int(input())
for tc in range(1,t+1):
  p, q, r, s, w = map(int, input().split())
  a = p * w
  if w <= r:
    b = q
  else:
    b = q + ((w - r) * s)
    
  print(f"#{tc} {min(a, b)}")
