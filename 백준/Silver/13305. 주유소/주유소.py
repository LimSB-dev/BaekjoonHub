n = int(input())
l = list(map(int,input().split()))
p = list(map(int,input().split()))

cost = 0

for i in range(n-1):
  if p[i] < p[i+1]:
    p[i+1] = p[i]
  cost += p[i]*l[i]

print(cost)