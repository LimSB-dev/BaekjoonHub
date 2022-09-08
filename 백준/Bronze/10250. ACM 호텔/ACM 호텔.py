t = int(input())
for _ in range(t):
  h,w,n=map(int,input().split())
  num = 1
  while n > h:
    n-=h
    num+=1
  if n==h:
    print(100*h+num)
  else:
    print(n*100+num)