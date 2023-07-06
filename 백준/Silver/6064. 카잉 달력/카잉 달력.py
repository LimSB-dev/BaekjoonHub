import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    answer = -1
    for i in range(x, M*N+1, M):
        if i % N == y % N:
            answer = i
            break

    print(answer)
