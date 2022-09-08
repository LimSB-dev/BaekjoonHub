for i in range(int(input())):
  Y=0
  K=0
  for j in range(9):
    a,b=map(int,input().split())
    Y += a
    K += b
  if Y>K:
    print('Yonsei')
  elif Y<K:
    print('Korea')
  else:
    print('Draw')