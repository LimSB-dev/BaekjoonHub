import sys

a, b ,v = list(map(int,sys.stdin.readline().split()))
day = (v - b)/(a-b)

print(int(day)
if day == int(day) else int(day)+1)