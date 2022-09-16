def r_s_p(num_1, num_2):
    # 비기면 앞
    if num_1 == num_2:
        return num_1
    # 가위
    if num_1 == 1:
        # 바위
        if num_2 == 2:
            return num_2
        # 보
        else:
            return num_1
    # 바위
    if num_1 == 2:
        # 보
        if num_2 == 3:
            return num_2
        # 가위
        else:
            return num_1
    # 보
    if num_1 == 3:
        # 가위
        if num_2 == 1:
            return num_2
        # 바위
        else:
            return num_1


def find_winner(arr):

    num = len(arr)

    if num == 1:
        return arr[0]

    elif num == 2:

        winner = r_s_p(arr[0][1], arr[1][1])

        if winner == arr[0][1]:
            return arr[0]
        else:
            return arr[1]

    else:
        mid = (1 + num) // 2

        front = arr[:mid]
        back = arr[mid:]

        f = find_winner(front)
        b = find_winner(back)

        winner = r_s_p(f[1], b[1])

        if winner == f[1]:
            return f
        else:
            return b


for tc in range(1, int(input()) + 1):
    n = int(input())
    students = list(map(int, input().split()))
    answer = 0
    array = []

    for index, value in enumerate(students):
        array.append([index + 1, value])

    answer = find_winner(array)

    print(f'#{tc} {answer[0]}')
