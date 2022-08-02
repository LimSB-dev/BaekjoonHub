import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

li = sorted(list(map(int, input().split())))

x = int(input().rstrip())

start,end=0,n-1
cnt = 0

while start < end:
  if li[start] + li[end] == x:
    cnt += 1
    start += 1
    end -= 1
  elif li[start] + li[end] < x:
    start += 1
  elif li[start] + li[end] > x:
    end -= 1

print(f'{cnt}')