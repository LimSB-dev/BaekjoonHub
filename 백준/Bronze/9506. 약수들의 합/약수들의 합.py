while True:
  a = 1
  T = []
  c = 0
  n = float(input())
  
  if n == -1:
  
    break

  else:
        
    while True:
    
      if n == a:

        if sum(T) == n:
          print(int(n),'=',1,end=' ')

          for i in range(1,c):
            print('+',T[i],end=' ')
          break

        else:    

          print(int(n),'is NOT perfect.')

          break

      elif n % a == 0:

        T.append(a)
        a += 1
        c += 1

      else:
        
        a += 1