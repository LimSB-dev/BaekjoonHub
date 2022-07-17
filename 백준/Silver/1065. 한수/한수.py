n = int(input())
c = 0

if n < 100:

  print(n)

else: 

  for i in range(100, n+1):

    h = i // 100
    t = i % 100 // 10
    o = i % 10

    if o - t == t - h:

      c += 1

  print(c+99)