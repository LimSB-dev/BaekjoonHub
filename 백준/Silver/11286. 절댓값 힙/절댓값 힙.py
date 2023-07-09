import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
positive_heap = []
negative_heap = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(positive_heap, x)
    elif x < 0:
        heappush(negative_heap, -x)
    else:
        if positive_heap and negative_heap:
            if positive_heap[0] < negative_heap[0]:
                print(heappop(positive_heap))
            else:
                print(-heappop(negative_heap))
        elif positive_heap:
            print(heappop(positive_heap))
        elif negative_heap:
            print(-heappop(negative_heap))
        else:
            print(0)