A = [9*1,7*3,8*1,0*3,9*1,2*3,1*1,4*3,1*1,8*3]

c = 1

for _ in range(3):
  
  a = int(input())
  
  if c % 2 != 0:
    a = a * 1
    c += 1
  else:
    a = a * 3
    c += 1
  A.append(a)

n = sum(A)

print('The 1-3-sum is %s'%n)