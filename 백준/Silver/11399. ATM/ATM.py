n = int(input())
li = list(map(int,input().split()))
li.sort()
anw = [0] * n
anw[0] = li[0]

for i in range(1,n):
  anw[i] = anw[i-1] + li[i]

print(sum(anw))