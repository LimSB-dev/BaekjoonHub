import sys
input = sys.stdin.readline

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())
if n == 0:
    print(0)
else:
    opinion = [int(input()) for _ in range(n)]

    opinion.sort()

    exception = round2(n * 0.15)

    new_opinion = opinion[exception:n-exception]

    avg = round2(sum(new_opinion) / len(new_opinion))

    print(avg)
