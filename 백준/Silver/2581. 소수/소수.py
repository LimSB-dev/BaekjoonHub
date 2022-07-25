n = int(input())
m = int(input())
P = []


for i in range(n,m+1):
  c = 0
  
  if i == 1:

    continue
    
  for j in range(2,i+1): 

    if i % j == 0:
      c += 1
  if c == 1:
     P.append(i)

if sum(P) == 0:
  
  print(-1)

else:
  
  print(sum(P))
  print(P[0])