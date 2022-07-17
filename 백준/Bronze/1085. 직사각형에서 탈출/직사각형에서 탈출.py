import sys

x,y,w,h=map(int,sys.stdin.readline().split())

l = [x,y,w-x,h-y]

print(min(l))