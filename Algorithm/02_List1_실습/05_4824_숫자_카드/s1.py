t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = input()
    answer = 0
    count_arr = [0] * 10

    for number in numbers:
        count_arr[int(number)] += 1

    max_number = count_arr[0]
    index = 0

    for i in range(10):
        if count_arr[i] >= max_number:
            max_number = count_arr[i]
            index = i

    print(f'#{tc} {index} {max_number}')
