import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    deleted = set()

    for _ in range(k):
        operator, n = map(str, input().split())
        n = int(n)

        if operator == 'I':
            heapq.heappush(min_heap, (n, _))
            heapq.heappush(max_heap, (-n, _))
            deleted.add(_)
        elif operator == 'D' and min_heap and max_heap:
            if n == -1:
                while min_heap and min_heap[0][1] not in deleted:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted.remove(heapq.heappop(min_heap)[1])
            elif n == 1:
                while max_heap and max_heap[0][1] not in deleted:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted.remove(heapq.heappop(max_heap)[1])

    while min_heap and min_heap[0][1] not in deleted:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] not in deleted:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
