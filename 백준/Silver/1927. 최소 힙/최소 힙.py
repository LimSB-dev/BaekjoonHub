import sys
from heapq import heappop, heappush
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x)
