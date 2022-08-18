for tc in range(1, int(input()) + 1):
    arr = list(input())
    
    # 절단된 쇠막대기의 수
    answer = 0

    # 현재 쇠막대기의 수
    iron = 0

    for i in range(len(arr)):

        # 레이저
        if arr[i] == '(' and arr[i + 1] == ')':
            answer += iron
        elif arr[i] == '(':
            iron += 1
        # 레이저
        elif arr[i] == ')' and arr[i - 1] == '(':
            pass
        else:
            iron -= 1
            answer += 1

    print(f'#{tc} {answer}')
