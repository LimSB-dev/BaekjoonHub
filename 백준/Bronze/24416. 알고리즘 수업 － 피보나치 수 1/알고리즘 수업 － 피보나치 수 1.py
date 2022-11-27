def fib(num):
    global cnt1
    if num == 1 or num == 2:
        return 1  # 코드1
    else:
        cnt1 += 1
        return fib(num - 1) + fib(num - 2)


def fibonacci(num):
    global cnt2
    f[1] = f[2] = 1

    for i in range(3, num + 1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]

    return f[num]


n = int(input())
f = [0] * (n + 1)
cnt1 = 1
cnt2 = 0

fib(n)
fibonacci(n)

print(cnt1, cnt2)