n, m = map(int, input().split())

packs = []
singles = []

for i in range(m):
    pack, single = map(int, input().split())
    packs.append(pack)
    singles.append(single)

min_pack = min(packs)
min_single = min(singles)

answer = 0

if min_pack < min_single * 6:
    answer += (n // 6) * min_pack
    n %= 6
    answer += min(min_pack, (n * min_single))
else:
    answer += n * min_single

print(answer)
