from heapq import heappush, heappop

n, k = map(int, input().split())

gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

gems.sort()
bags.sort()

tmp = []
answer = 0

for bag in bags:

    while gems and bag >= gems[0][0]:
        heappush(tmp, -gems[0][1])
        heappop(gems)

    if tmp:
        answer += heappop(tmp)

print(-answer)