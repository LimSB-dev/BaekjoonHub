def dfs(now, length, visited):
    global answer

    for i in range(n):

        if not visited[i]:

            visited[i] = True

            length += abs(now[0] - client[i][0]) + abs(now[1] - client[i][1])

            # 가지치기
            if answer <= length:
                visited[i] = False
                return

            # 종료 조건
            if visited == [True] * n:
                length += abs(client[i][0] - end[0]) + abs(client[i][1] - end[1])
                if answer > length:
                    answer = length
                visited[i] = False
                return

            dfs(client[i], length, visited)

            # 가지치기나 끝까지 간 후
            visited[i] = False

            length -= abs(now[0] - client[i][0]) + abs(now[1] - client[i][1])


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * n
    answer = INF
    start = arr[:2]
    end = arr[2:4]
    arr = arr[4:]
    client = []

    for k in range(n):
        client.append(arr[k * 2:(k * 2) + 2])

    dfs(start, 0, visited)

    print(f'#{tc} {answer}')
