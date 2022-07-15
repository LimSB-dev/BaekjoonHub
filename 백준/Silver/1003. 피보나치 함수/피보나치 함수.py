t = int(input())
zero = [1,0,1,1]
one = [0,1,1,2]

for i in range(4,50):
  Z = zero[i-1]+zero[i-2]
  O = one[i-1]+one[i-2]
  zero.append(Z)
  one.append(O)

for i in range(t):
  n = int(input())
  print(zero[n],one[n])