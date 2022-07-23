import heapq

t = int(input())
li = []
anw = 0

for _ in range(t):
  heapq.heappush(li,int(input()))

while len(li) > 1:
  num = 0
  
  for i in range(2):
    num += heapq.heappop(li)
  
  anw += num
  heapq.heappush(li,num)

print(anw)