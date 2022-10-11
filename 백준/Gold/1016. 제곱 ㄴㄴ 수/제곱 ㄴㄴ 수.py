def solution(min_value, max_value):
    answer = max_value - min_value + 1
    check = [False] * answer
    i = 2
    while i**2 <= max_value:
        square_number = i**2
        remain = 0 if min_value % square_number == 0 else 1
        j = min_value // square_number + remain
        while square_number * j <= max_value:
            if not check[square_number * j - min_value]:
                check[square_number * j - min_value] = True
                answer -= 1
            j += 1
        i += 1
    print(answer)


a, b = map(int, input().split())

solution(a, b)