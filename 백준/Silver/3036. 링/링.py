n = int(input())
rings = list(map(int,input().split()))

def isGreatest(num1,num2):
  while num2 != 0:
    remain = num1 % num2
    num1 = num2
    num2 = remain
  return num1

for i in range(1,n):
  num = isGreatest(rings[0],rings[i])
  print('{}/{}'.format(rings[0]//num,rings[i]//num))