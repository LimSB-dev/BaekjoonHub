# w ｘ h 인 격자
w, h = map(int, input().split())

# 최초 좌표
p, q = map(int, input().split())

# 움직인 시간
t = int(input())

p += (t % (2 * w))
q += (t % (2 * h))

if p > w:
    p -= w
    p = w - p
    if p < 0:
        p *= -1
if q > h:
    q -= h
    q = h - q
    if q < 0:
        q *= -1

print(p, q)
