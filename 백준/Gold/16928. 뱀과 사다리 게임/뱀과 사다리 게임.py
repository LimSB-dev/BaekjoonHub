import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ladder_list = [list(map(int, input().split())) for _ in range(n)]
snake_list = [list(map(int, input().split())) for _ in range(m)]

def bfs():
    queue = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True

    while queue:
        position, cnt = queue.popleft()

        if position == 100:
            return cnt

        for i in range(1, 7):
            next_position = position + i
            if next_position > 100:
                break

            # 사다리
            for x, y in ladder_list:
                if next_position == x:
                    next_position = y
                    break

            # 뱀
            for u, v in snake_list:
                if next_position == u:
                    next_position = v
                    break
            
            if not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, cnt + 1))

answer = bfs()
print(answer)
