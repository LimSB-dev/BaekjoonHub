import sys
sys.stdin = open('input.txt')

dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def possible(s, L):
    arr = s[(-L) * 56:]
    ret = [0]
    for i in range(0, L * 56, L * 7):
        temp = dct.get(arr[i:i + (7 * L):L], -1)
        if temp == -1:
            return
        ret.append(temp)
    return ret


def solve():
    for password in passwords:
        bins = format(int(password, 16), 'b').strip('0')
        length = 1
        while bins:
            while len(bins) < 56 * length:
                bins = '0' + bins
            code = possible(bins, length)
            if code:
                bins = bins[:len(bins) - length * 56].strip('0')
                res.add(tuple(code))
                length = 0
            length += 1
    answer = 0

    for num in res:
        tmp = 0
        for i in range(1, 9):
            tmp += num[i] + num[i] * (i & 1) * 2
        if not tmp % 10:
            answer += sum(num)

    return answer


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    passwords, res = set(), set()
    for _ in range(n):
        tmp = input().strip().strip('0')
        if tmp:
            passwords.add(tmp)
    print(f'#{tc}', solve())
