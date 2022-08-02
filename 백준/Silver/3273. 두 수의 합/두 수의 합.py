n=int(input())
s=set(map(int,input().split()))
x=int(input().strip())
cnt = 0
for i in s:
    if x - i in s:
        cnt += 1
print(cnt//2)