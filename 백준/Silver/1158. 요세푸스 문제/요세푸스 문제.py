import sys
input = sys.stdin.readline

n,k = map(int,input().split())
li = [i for i in range(1,n+1)]
anw = []

num = 0 # 제거할 사람 인덱스 번호

while len(li) != 0:
  num = (num + (k - 1)) % len(li)
  anw.append(li.pop(num))

print('<',end='')
print(*anw,sep=', ',end='')
print('>',end='')