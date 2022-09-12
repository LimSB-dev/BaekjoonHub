n = int(input())

P = [0,1,1]

for i in range(1,n+1):
  p = P[1]+P[2]

  P.append(p)
  P.remove(P[0])

print(P[0])