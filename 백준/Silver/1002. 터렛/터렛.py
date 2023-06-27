import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())

    r_squared = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2

    if r_squared > (r_1 + r_2) ** 2:  # 두 원이 서로 떨어져 있는 경우
        print(0)
    elif r_squared < (r_1 - r_2) ** 2:  # 한 원이 다른 원을 포함하고 있는 경우
        print(0)
    elif r_squared == 0 and r_1 == r_2:  # 두 원이 일치하는 경우
        print(-1)
    elif r_squared == (r_1 + r_2) ** 2 or r_squared == (r_1 - r_2) ** 2:  # 내접 또는 외접하는 경우
        print(1)
    else:
        print(2)
