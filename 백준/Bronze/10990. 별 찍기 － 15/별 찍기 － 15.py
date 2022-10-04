n=int(input())

for i in range(1,n+1):
  if i == 1:
    print(' '*(n-1),end='')
    print('*',end='')
    
  else:
    print(' '*(n-i),end='')
    print('*',end='')
    print(' '*(2*i-3),end='')
    print('*',end='')
  print()