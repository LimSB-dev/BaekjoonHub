import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    bins = list(map(int, input()))
    tris = list(map(int, input()))
    answer = 0

    for i, bi in enumerate(bins):
        tmp_b = bins[i]
        bins[i] = (bi + 1) % 2

        for j, tri in enumerate(tris):
            for k in range(1, 3):
                b = 0
                t = 0
                tmp_t = tris[j]
                tris[j] = (tri + k) % 3

                for index, value in enumerate(bins[::-1]):
                    b += value * (2 ** index)
                for index, value in enumerate(tris[::-1]):
                    t += value * (3 ** index)

                if b == t:
                    answer = b
                    break

                tris[j] = tmp_t
            if answer != 0:
                break
        bins[i] = tmp_b
        if answer != 0:
            break

    print(f'#{tc} {answer}')
