import sys
sys.stdin = open('input.txt')
# 원형 큐
from collections import deque


# 큐 / 방문 리스트
def bfs(queue, robot):
    global answer

    zero = 0

    while queue:
        idx, number = queue.popleft()

        
            # 한 칸 전진
            if not robot[i + 1] and queue[i + 1][1] > 1:

                # 방문 처리
                robot[i + 1] = True
                robot[i] = False

                # 내구성 하락
                queue[i + 1][1] -= 1

                # 0이 된 순간
                if queue[i + 1][1] == 0:
                    zero += 1

                # 내구도가 0인 칸의 개수가 k개 이상이면 과정 종료
                if zero >= k:
                    return

        # 3단계
        # 0이 아닌 경우 로봇 올려두기
        if number != 0:
            number -= 1
            robot[idx] = True

        # 4단계
        # 내구도가 0인 칸의 개수가 k개 이상이면 과정 종료
        if zero >= k:
            return

        queue.append([idx, number])

        answer += 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * (2 * n)

# 가장 처음 수행되는 단계는 1번째 단계
answer = 1

belt = deque()
for idx, value in enumerate(arr):
    belt.append([idx, value])

bfs(belt, visited)

print(answer)
