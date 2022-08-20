# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    # 최고 높이의 좌표 리스트
    max_positions = []
    max_height = 1

    # 완전 탐색으로 최고 높이 좌표 탐색
    for row in range(n):
        for col in range(n):

            # 최고 높이 이상일 경우
            if arr[row][col] > max_height:
                max_height = arr[row][col]
                max_positions = []
                max_positions.append((row, col))

            # 최고 높이와 같을 경우
            elif arr[row][col] == max_height:
                max_positions.append((row, col))

            # 낮을 경우
            else:
                continue
    
    # 최고 높이의 정보를 담을 리스트
    position_status = []
    
    # 최고 높이
    max_distance = 0
    

    for position in max_positions:
        x, y = position
        position_status.append((x, y, max_height, 1))

    # 모든 최고 높이 좌표를 탐색하면 반복문 종료
    while position_status:
        
        # 좌표 / 현재높이 / 깍을 수 있는지 여부
        x, y, height, dig = position_status.pop()
        stack =[]

        #좌표 / 높이 / 상태 / 등산로의 길이 / 오기 전 좌표
        stack.append((x, y, height, dig, 1, []))


        while stack:
            x, y, height, dig, distance, visited = stack.pop()
            new_visit = visited.copy()
            new_visit.append((x, y))

            # 최고 길이 대소 비교
            if distance > max_distance:
                max_distance = distance
            
            # 상 하 좌 우 탐색
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                
                # 범위 밖일 경우 continue
                if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                    continue

                # 방문 했다면 continue
                if (nx, ny) in new_visit:
                    continue

                # 현재 저장된 높이 보다 낮다면
                if arr[nx][ny] < height:
                    stack.append((nx, ny, arr[nx][ny], dig, distance + 1, new_visit))

                # 저장된 높이 보다 높거나 같고 삽질이 가능할 경우
                elif arr[nx][ny] >= height and dig == 1:
                    # 삽질해도 여전히 높거나 같을 경우
                    if arr[nx][ny] >= height + k:
                        continue
                    # 삽질하면 지나갈 수 있을 경우
                    else:
                        # 최대한 현재 저장된 높이랑 비슷하게 삽질해준다.
                        # 삽질 가능 여부를 0으로 변경
                        stack.append((nx, ny, height - 1, 0, distance + 1, new_visit))
 
    print(f'#{tc} {max_distance}')