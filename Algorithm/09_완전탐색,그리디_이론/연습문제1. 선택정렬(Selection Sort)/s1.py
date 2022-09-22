# 재귀를 이용한 선택정렬

def selection_sort(i):

    # 종료 조건
    if i == len(numbers) - 1:
        return

    min_index = i  # min_index를 정렬되지 않는 부분 중 맨 앞 인덱스로 초기화

    # '맨 앞 인덱스 + 1'부터 비교하여 최소값 인덱스 찾기
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # 맨 앞의 값과 최소값을 교환
    selection_sort(i + 1)  # 재귀 호출


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(0)  # 0번째 원소부터 정렬 시작
print(numbers)
