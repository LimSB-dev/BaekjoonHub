t = int(input())

a = 1

c = 2

T = t

while True:

  if t > a:
  
    t -= a
  
    a += 1

    c += 1
    
  else:

    H = c - t

    if (t + H) % 2 == 0:

      print(f'{H}/{t}')
      break
    
    else:

      print(f'{t}/{H}')
      break