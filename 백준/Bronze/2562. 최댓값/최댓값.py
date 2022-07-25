A = []
for i in range(9):
  A.append(int(input()))
max = max(A)
index=A.index(max)+1
print(max)
print(index)