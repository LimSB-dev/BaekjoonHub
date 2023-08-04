import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().strip())) for _ in range(n)]

sets = [0, 1]
dr = [0, 1]
dc = [1, 0]

answer = 0

for case in product(sets, repeat=n * m):
    area_case = [[] for _ in range(n)]
    for idx, di in enumerate(case):
        area_case[idx // m].append(di)

    visited = [[False] * m for _ in range(n)]
    num_sum = 0

    for r in range(n):
        for c in range(m):
            if visited[r][c]:
                continue

            num = area[r][c]
            visited[r][c] = True
            di = area_case[r][c]
            rr, cc = r, c
            while True:
                nr = rr + dr[di]
                nc = cc + dc[di]

                if 0 <= nr < n and 0 <= nc < m and area_case[nr][nc] == di:
                    visited[nr][nc] = True
                    num = num * 10 + area[nr][nc]
                    rr = nr
                    cc = nc

                else:
                    num_sum += num
                    break

    answer = max(answer, num_sum)

print(answer)
