def isPrime(num):
  if num == 1:
    return False
  for i in range(2,int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

t = int(input())

for i in range(t):

  Prime = []
  
  n = int(input())

  for j in range(2,n+1):
    if isPrime(j):
      Prime.append(j)

  l = len(Prime)
  G = []
  for k in range(l):

    anw = n - Prime[k]
    
    if anw in Prime:
    
      gap = abs(anw - Prime[k])
      G.append(gap)
  
  a = int((n - min(G))*0.5)
  b = int((n + min(G))*0.5)
  
  print(a,b)