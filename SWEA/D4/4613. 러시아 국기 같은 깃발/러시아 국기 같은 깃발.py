for tc in range(1, int(input()) + 1):
    answer = 0
    h, w = map(int, input().split())
    flag = [list(input()) for _ in range(h)]
    colors = []

    # white, blue, red 개수
    for i in range(h):
        white_cnt = flag[i].count('W')
        blue_cnt = flag[i].count('B')
        colors.append([white_cnt, blue_cnt, w - (white_cnt + blue_cnt)])

    # 가장 위는 white 고정
    for i in range(1, h):
        colors[i][0] += colors[i - 1][0]
        colors[i][1] += colors[i - 1][1]
        colors[i][2] += colors[i - 1][2]

    # white를 제외하고 최소 2줄은 있어야 한다. 
    for i in range(h - 2):
        
        # blue가 가능한 영역
        for j in range(i + 1, h - 1):
            white = colors[i][0]
            blue = colors[j][1] - colors[i][1]
            red = colors[h - 1][2] - colors[j][2]
            
            # 변경하지 않고 유지 가능한 최대 수
            total = white + blue + red
            
            # 대소 비교
            if answer < total:
                answer = total

    print(f'#{tc} {(h * w) - answer}')
