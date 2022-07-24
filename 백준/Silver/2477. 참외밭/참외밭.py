# 큰 직사각형에서 작은 직각사각형을 뺀다고 생각

k = int(input())
infos = []

# 동 서 남 북 별 길이 리스트 따로 저장
for _ in range(6):
    direction, length = map(int, input().split())
    infos.append(length)

# 가장 길이가 긴 가로변 및 변의 인덱스값
max_width = max(infos)
max_width_index = infos.index(max_width)

# 가장 길이가 가로변 양 옆 중 하나는 길이가 가장 긴 세로변
max_height = max(infos[max_width_index - 1], infos[(max_width_index + 1) % 6])

# 양쪽 세로변의 차이는 뺄 직사각형의 세로변
min_height = abs(infos[max_width_index - 1] -
                 infos[(max_width_index + 1) % 6])

# 가장 길이가 세로변의 인덱스값
max_height_index = infos.index(max_height)

# 세로변의 양쪽 가로변의 차이는 뺄 직사각형의 가로변
min_width = abs(infos[max_height_index - 1] -
                infos[(max_height_index + 1) % 6])

# 큰 직각사각형과 작은 직각사각형을 구하고 넓이의 차이
max_scale = max_width * max_height
min_scale = min_width * min_height

total_scale = max_scale - min_scale

print(total_scale * k)
