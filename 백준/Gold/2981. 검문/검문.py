import sys
input = sys.stdin.readline

def isGCD(num1,num2):
  while num2 != 0:
    num1,num2 = num2,(num1 % num2)
  return num1

n = int(input())
li = []

for i in range(n):
  num = int(input())
  li.append(num)
li.sort()

gcd = li[1] - li[0]

for i in range(2,n):
  gcd = isGCD(gcd,li[i] - li[i-1])

for i in range(2,gcd//2+1):
  if gcd % i == 0:
    print(i,end=' ')
print(gcd)
