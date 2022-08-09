t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = input()
    answer = 0
    # 카운팅 정렬을 담을 리스트 생성
    count_arr = [0] * 10

    # 문자열 numbers를 순회하면서
    for number in numbers:
        # 카운팅 정렬의 int(number)에 해당하는 인덱스에 1을 추가
        count_arr[int(number)] += 1

    # 가장 많은 카드에 적힌 숫자
    index = 0
    # 그 카드가 몇 장인지
    max_number = count_arr[0]

    # count_arr의 0 ~ 9 까지 index를 순회
    for i in range(10):
        if count_arr[i] >= max_number:
            max_number = count_arr[i]
            index = i

    print(f'#{tc} {index} {max_number}')
