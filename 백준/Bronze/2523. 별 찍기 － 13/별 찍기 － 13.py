n=int(input())

for i in range(1,n+1):
  print('*'*i,end='')
  print()  
for i in range(1,n):
  print('*'*(n-i),end='')
  print()