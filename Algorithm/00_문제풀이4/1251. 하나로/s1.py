import sys
sys.stdin = open('input.txt', encoding='utf-8')
from heapq import heappush, heappop


def prim(start):
    visited = [False] * n
    heap = [(0, start)]
    cost = 0

    while heap:

        min_dist, min_node = heappop(heap)

        if not visited[min_node]:

            visited[min_node] = True
            cost += (min_dist**2) * e

            for next_node, value in enumerate(coordinate):
                nr, nc = value
                r, c = coordinate[min_node]
                dist = ((nr - r)**2 + (nc - c)**2)**0.5

                if not visited[next_node]:
                    heappush(heap, (dist, next_node))

    return cost


for tc in range(1, int(input()) + 1):
    n = int(input())

    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))

    coordinate = []
    for col, row in zip(x_arr, y_arr):
        coordinate.append([row, col])

    e = float(input())

    answer = round(prim(0))

    print(f'#{tc} {answer}')
