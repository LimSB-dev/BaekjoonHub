import sys
input = sys.stdin.readline

MOD = 1000000007
N = 8
matrix = dict()
D = int(input())
matrix[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

def solution(d, start, end):
    if d <= 1:
        return matrix[d][start][end]
    
    matrix.setdefault(d, [[0] * N for _ in range(N)])
    if matrix[d][start][end]:
        return matrix[d][start][end]
    
    half = d // 2
    other = half + 1 if d % 2 else half

    for k in range(N):
        matrix[d][start][end] += solution(half, start, k) * solution(other, k, end)
        matrix[d][start][end] %= MOD

    return matrix[d][start][end]

print(solution(D, 0, 0))