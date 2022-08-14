n = int(input())
arr = list(map(int, input().split()))
for _ in range(int(input())):
    gender, switch = map(int, input().split())

    # 남자
    if gender == 1:
        for i in range(switch, n + 1, switch):
            arr[i - 1] = (arr[i - 1] + 1) % 2

    # 여자
    else:
        for i in range(min(switch, n - switch + 1)):
            # 중앙
            if i == 0:
                arr[switch - 1] = (arr[switch - 1] + 1) % 2
            # 좌우 대칭
            elif arr[switch - 1 + i] == arr[switch - 1 - i]:
                arr[switch - 1 + i] = (arr[switch - 1 + i] + 1) % 2
                arr[switch - 1 - i] = (arr[switch - 1 - i] + 1) % 2
            # 좌우 비대칭
            else:
                break

while arr:
    print(*arr[:20])
    arr = arr[20:]