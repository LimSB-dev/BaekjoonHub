import sys
def isPrime(num):
  if num == 1:
    return False
  else:
    for i in  range(2,int(num**0.5)+1):
      if num % i == 0:
        return False
    return True
n,m = map(int,sys.stdin.readline().split())
for i in range(n,m+1):
  if isPrime(i):
    print(i)