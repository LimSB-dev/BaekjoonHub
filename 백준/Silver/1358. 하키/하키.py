W, H, X, Y, P = map(int, input().split())
R = H / 2
answer = 0

for _ in range(P):
    x, y = map(int, input().split())
    # 직사각형 내부에 있는지 판단
    # x가 직사각형 가로 범위에 있는지 확인
    if X <= x and x <= (X + W):
        # y가 직사각형 세로 범위에 있는지 확인
        if Y <= y and y <= (Y + H):
            answer += 1
    # 반 원 내부에 있는지
    elif (x - (X))**2 + (y - (Y + R))**2 <= (H / 2)**2:
        answer += 1
    elif (x - (X + W))**2 + (y - (Y + R))**2 <= (H / 2)**2:
        answer += 1

print(answer)