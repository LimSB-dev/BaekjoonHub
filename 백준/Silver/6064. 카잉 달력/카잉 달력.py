import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    # x와 y에 대한 최소공배수를 구합니다.
    lcm = M * N // math.gcd(M, N)
    
    answer = -1
    
    for i in range(x, lcm+1, M):
        if (i - 1) % N + 1 == y:
            answer = i
            break

    print(answer)
