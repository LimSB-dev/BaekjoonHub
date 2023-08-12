import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:
    time = {n: 0}
    queue = deque([n])

    while queue:
        position = queue.popleft()

        if position == k:
            print(time[position])
            break

        for next_position in (position * 2, position - 1, position + 1):
            if next_position not in time and 0 <= next_position <= 100000:
                if next_position == 2 * position:
                    time.setdefault(next_position, time[position])
                else:
                    time.setdefault(next_position, time[position] + 1)
                queue.append(next_position)
