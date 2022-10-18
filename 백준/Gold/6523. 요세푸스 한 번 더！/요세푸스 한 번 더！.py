while True:
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        break

    n, a, b = arr
    x = 0

    drink = {
        x: 1
    }

    while True:
        next_person = (a * (x**2) + b) % n

        if next_person in drink:
            drink[next_person] += 1
            if drink[next_person] == 3:
                break
        else:
            drink[next_person] = 1

        x = next_person

    answer = list(drink.values()).count(1)

    print(n - len(drink) + answer)