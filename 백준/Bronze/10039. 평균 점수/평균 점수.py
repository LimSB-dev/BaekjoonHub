arr =[]

for _ in range(5):
  a = int(input())

  if a<40:
    arr.append(40)

  else:
    arr.append(a)

print(int(sum(arr)/5))