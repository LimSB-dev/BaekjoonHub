m = int(input())
n = int(input())
li = []

for i in range(1,101):
  if i**2 >= m and i**2 <= n:
   li.append(i**2)

if sum(li) == 0:
  print(-1)

else:
  print(f'{sum(li)}\n{min(li)}')