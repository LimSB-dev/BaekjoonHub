import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input()))
    answer = []

    while arr:
        result = 0
        arr1 = arr[:7]
        arr = arr[7:]
        for i in range(7):
            if arr1[i] == 1:
                result += 2**(6 - i)
        answer.append(result)

    print(*answer)
