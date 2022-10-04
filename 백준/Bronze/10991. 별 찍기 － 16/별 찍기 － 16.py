n=int(input())

for i in range(1,n+1):
  if i == 1:
    print(' '*(n-1),end='')
    print('*',end='')
    
  else:
    
    print(' '*(n-i),end='')

    for j in range(1,i+1):
      
      print('*',end='')
      print(' ',end='')
  print()