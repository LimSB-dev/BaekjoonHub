n = int(input())

P = [0,1,1]

for i in range(3,91):
  p = P[i-2]+P[i-1]

  P.append(p)

print(P[n])