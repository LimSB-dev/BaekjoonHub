import math

n, k = map(int, input().split())

# 방의 개수
answer = 0

# 배열 생성
school = [[0, 0] for _ in range(7)]

for i in range(n):
    # 성별, 학년
    s, y = map(int, input().split())
    school[y][s] += 1

for grade in range(7):
    for gender in range(2):
        answer += math.ceil(school[grade][gender] / k)
       
print(answer)