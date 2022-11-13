from collections import deque

n = int(input())
queue = deque([])
answer = []

for _ in range(n):
    arr = list(input().split())
    cmd = arr[0]

    if cmd == 'push':
        queue.append(arr[1])
    elif cmd == 'pop':
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif cmd == 'size':
        answer.append(len(queue))
    elif cmd == 'empty':
        if queue:
            answer.append(0)
        else:
            answer.append(1)
    elif cmd == 'front':
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif cmd == 'back':
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)

print(*answer, sep='\n')