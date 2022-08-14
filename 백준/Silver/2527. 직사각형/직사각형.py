for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    answer = 'a'

    # 공통부분이 없을 경우
    if p2 < x1 or q2 < y1 or p1 < x2 or q1 < y2:
        answer = 'd'
    # 점이 겹칠 경우
    elif (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2):
        answer = 'c'
    # 선분이 겹칠 경우
    elif (x1 < p2 and y1 == q2) or (x1 == p2 and q1 > y2) or (p1 > x2 and q1 == y2) or (p1 == x2 and y1 < q2):
        answer = 'b'
    # 직사각형이 겹칠 경우
    else:
        answer = 'a'

    print(answer)