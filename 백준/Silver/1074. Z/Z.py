import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def Z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    subarray = (r >= half) * 2 + (c >= half)
    subarray_r = r % half
    subarray_c = c % half
    return ((subarray * half * half)
            + Z(n-1, subarray_r, subarray_c))


n, r, c = map(int, input().split())
print(Z(n, r, c))
