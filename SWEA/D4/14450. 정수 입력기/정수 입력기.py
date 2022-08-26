def solution(l, r, n):
    tmp_l = l
    tmp_r = r

    if r >= n:
        t = len(str(n))
        while len(str(tmp_l)) > t:
            tmp_l //= 10
            tmp_r //= 10
        if tmp_l <= n <= tmp_r:
            return True
        else:
            while n < r:
                n *= 10
                if l <= n <= r:
                    return True

            return False
    else:
        return False


for tc in range(1, int(input()) + 1):
    left, right, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = ''

    for number in numbers:
        if solution(left, right, number):
            answer += 'O'
        else:
            answer += 'X'

    print(f'#{tc} {answer}')
