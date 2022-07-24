n = int(input())
li = []

for i in range(n):
  a = int(input())
  li.append(a)

li.sort(reverse= True)

A = []
for i in range(n):
  anw = li[i]*(i+1)
  A.append(anw)

print(max(A))