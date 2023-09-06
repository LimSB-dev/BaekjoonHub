import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
answer = [0] * 1000001
visited = [False] * 1000001

for card in cards:
    visited[card] = True

for card in sorted(cards):
    for j in range(card * 2, 1000001, card):
        if visited[j]:
            answer[card] += 1
            answer[j] -= 1

for card in cards:
    print(answer[card], end=' ')
