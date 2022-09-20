import sys
sys.stdin = open('input.txt', encoding='utf-8')

answer = []
for tc in range(int(input())):
    N, M = map(int, input().split())
    answer.append(f"#{tc+1} {'ON' if M % (2**N)==2**N-1 else 'OFF'}")

print('\n'.join(answer))
