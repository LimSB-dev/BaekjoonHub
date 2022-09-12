t = int(input())
A=[]
for _ in range(t):
  a,b = map(int,input().split())
  A.append(b%a)
print(sum(A))