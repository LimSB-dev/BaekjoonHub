def counter_check(arr):
    counter = [0] * 4
    arr = arr[1:]

    for i in range(4):
        counter[i] = arr.count(i + 1)

    return counter


def who_is_winner(arr_1, arr_2):
    answer = 'D'
    counter_a = counter_check(arr_1)
    counter_b = counter_check(arr_2)
    for i in range(4):
        if counter_a[3 - i] == counter_b[3 - i]:
            continue
        elif counter_a[3 - i] > counter_b[3 - i]:
            answer = 'A'
            break
        else:
            answer = 'B'
            break

    print(answer)


n = int(input())

for _ in range(n):
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    who_is_winner(arr_a, arr_b)
