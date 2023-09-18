import sys
input = sys.stdin.readline

n, min_avg_score = map(float, input().split())
grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

score = 0
credit = 0

for _ in range(int(n) - 1):
    c, g = input().split()
    credit += int(c)
    score += int(c) * grade[g]

l = int(input())

for g in sorted(grade.keys(), reverse=True):
    cur_avg_score = int(
        int(((score + l * grade[g]) / (credit + l)) * 1000) / 10) / 100
    if cur_avg_score > min_avg_score:
        print(g)
        break
else:
    print('impossible')
