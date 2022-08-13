for i in range(10):
    answer = 0
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    col = 0
    
    # 도착지점 찾기
    for index, value in enumerate(matrix[-1]):
        if value == 2:
            col = index
            break

    while row > 0:
        
        # 왼쪽 확인
        has_left = False
        while col > 0 and matrix[row][col - 1] == 1:
            has_left = True
            col -= 1

        # 오른쪽 확인
        if not has_left:
            while col < 99 and matrix[row][col + 1] == 1:
                col += 1
        
        row -= 1
    print(f'#{tc} {col}')
