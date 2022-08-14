length, height = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
person = list(map(int, input().split()))

# 최단 거
answer = 0

# 동근의 방향
pos = person[0]

# 북: 1 / 남: 2 / 서: 3 / 동: 4
for i in range(n):

    # 현재 가게의 방
    store_pos = stores[i][0]

    # 동근이와 가게가 같은 방향에 위치한 경우
    if store_pos == pos:
        answer += abs(stores[i][1] - person[1])
    # 마주보는 방향에 위치한 경우
    # 북 / 남
    elif store_pos + pos == 3:
        answer += height + min((stores[i][1] + person[1]), ((length * 2) - (stores[i][1] + person[1])))
    # 동 / 서
    elif store_pos + pos == 7:
        answer += length + min((stores[i][1] + person[1]), ((height * 2) - (stores[i][1] + person[1])))
    # 인접한 방향에 위치한 경우
    else:
        # 가게의 위치
        # 북
        if store_pos == 1:
            # 서
            if pos == 3:
                answer += stores[i][1] + person[1]
            # 동
            else:
                answer += length - stores[i][1] + person[1]
        # 남
        elif store_pos == 2:
            # 서
            if pos == 3:
                answer += height + stores[i][1] - person[1]
            # 동
            else:
                answer += length + height - stores[i][1] - person[1]
        # 서
        elif store_pos == 3:
            # 북
            if pos == 1:
                answer += stores[i][1] + person[1]

            # 남
            else:
                answer += height - stores[i][1] + person[1]
        # 동
        else:
            # 북
            if pos == 1:
                answer += length + stores[i][1] - person[1]

            # 남
            else:
                answer += length + height - stores[i][1] - person[1]

print(answer)
