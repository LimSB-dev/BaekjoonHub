t = int(input())

for _ in range(t):

  a = []
  T=int(input())

  for i in range(1,T+1):

    if i % 2 !=0:

      a.append(i)
    
  print(sum(a))