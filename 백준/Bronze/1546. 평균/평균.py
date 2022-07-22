n = int(input())
a = list(map(int,input().split()))
b=[]

for i in range(n):
  b.append(a[i]/max(a)*100)

print(round(sum(b)/len(b),7))