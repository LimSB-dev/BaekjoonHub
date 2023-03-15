K, N = map(int, input().split())
lan_cables = [int(input()) for _ in range(K)]

# 이진 탐색을 이용하여 가장 긴 길이 구하기
start, end = 1, max(lan_cables)

while start <= end:
    # 중간값 계산
    mid = (start + end) // 2
    # 랜선 길이별로 자른 개수 합산
    cnt = sum([cable // mid for cable in lan_cables])
    if cnt >= N:
        # 자른 개수가 목표 개수보다 크거나 같으면
        # 더 긴 길이의 랜선으로 잘라봄
        start = mid + 1
    else:
        # 자른 개수가 목표 개수보다 작으면
        # 더 짧은 길이의 랜선으로 잘라봄
        end = mid - 1

print(end)  # 가장 긴 길이 출력