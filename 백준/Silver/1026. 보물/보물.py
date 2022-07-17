n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse = True)
# print(A,B)

s =[]
for i in range(n):
  s.append(A[i]*B[i])

print(sum(s))