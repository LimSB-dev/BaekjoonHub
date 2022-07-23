n = int(input())
li = []

for i in range(n):
  s,e = map(int,input().split())
  li.append([s,e])

li.sort(key = lambda x: x[0])
li.sort(key = lambda x: x[1])

end = 0
count = 0

for i in li:
  if i[0] >= end:
    end = i[1]
    count += 1

print(count)