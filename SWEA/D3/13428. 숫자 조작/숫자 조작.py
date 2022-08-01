from itertools import combinations

t = int(input())

for tc in range(1, t + 1):
    n = list(input())
    tmp = [int("".join(n))]

    for a, b in combinations(range(len(n)), 2):
        n[a], n[b] = n[b], n[a]

        if n[0] != "0":
            tmp.append(int("".join(n)))
        n[b], n[a] = n[a], n[b]

    print(f"#{tc} {min(tmp)} {max(tmp)}")