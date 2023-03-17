import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

selected = []

def back_track(start):
    if len(selected) == m:
        print(' '.join(map(str, selected)))
        return
    
    for i in range(start, n + 1):
        selected.append(i)
        back_track(i + 1)
        selected.pop()

back_track(1)