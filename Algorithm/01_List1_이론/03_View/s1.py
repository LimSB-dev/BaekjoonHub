t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    # 조망권이 확보된 층 수를 담을 변수를 생성한다.
    answer = 0

# 앞 뒤 2칸은 0임으로 제외시킨다.
for i in range(2, n - 2):
    # 좌우 2칸 범위에서 가장 높은 건물 다음으로 높은 건물의 높이를 담을 변수을 생성한다.
    height = 0

    # 좌우 2칸 범위에서 가장 높다면 조망권은 확보된다.
    if arr[i] > arr[i + 1] and arr[i] > arr[i + 2] and arr[i] > arr[i - 1] and arr[i] > arr[i - 2]:

        # 내장 함수 max()를 사용하지 않고 좌우 2칸 범위에서 가장 높은 건물 다음으로 높은 건물의 높이를 담는다.
        if arr[i - 2] > height:
            height = li[i - 2]
        if arr[i - 1] > height:
            height = li[i - 1]
        if arr[i + 1] > height:
            height = li[i + 1]
        if arr[i + 2] > height:
            height = li[i + 2]

            answer += arr[i] - height

print(f"#{tc} {answer}")