for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [True] + [False] * sum(arr)
    answer = [0]

    for num in arr:
        for i in range(len(answer)):
            if not visited[answer[i] + num]:
                visited[answer[i] + num] = True
                answer.append(answer[i] + num)

    print(f'#{tc} {len(answer)}')