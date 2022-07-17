t = int(input())

for i in range(t):

  a,b=map(int,input().split())
  A=1
  B=1
  
  for i in range(a):
  
    A = A * (i+1)
  
  for i in range(a):
  
    B = B*(b-i)

  print(int(B/A))