t = int(input())
cnt = 0

while True:
  if cnt == t - 1:
    print('*' * ((t * 2) - 1))
    break
  
  elif cnt == 0:
    print(' ' * (t - 1),end='')
    print('*')
    cnt += 1

  else:
    print(' ' * (t - 1 - cnt),end='')
    print('*',end='')
    print(' ' * ((cnt * 2) - 1),end='')
    print('*')
    cnt += 1