for _ in range(int(input())):
  n=int(input())
  r=list(map(int,input().split()))
  print((max(r)-min(r))*2)