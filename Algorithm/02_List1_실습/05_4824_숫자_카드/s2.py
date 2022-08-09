t = int(input())

for tc in range(1, t + 1):
    n = input()
    num = input()
    counter = [0] * 10  # 일의 자리수를 담을 카운터 리스트 생성
    for _ in range(n):
        if not int(num[0]):
            counter[0] += 1
            num = num[1:]
    num = int(num)

    while num > 0:  # num이 0이 될 때 까지
        counter[num % 10] += 1  # num의 1의 자리를 인덱스로 한 counter에 개수를 채운다
        num //= 10  # num을 10으로 나눈 몫을 num에 넣는다

    max_c = 0  # conter에 담긴 최대 개수를 뽑을 변수 생성
    the_most_num = counter[0]  # 제일 많이 나온 숫자

    for i in counter:  # 개수가 제일 많은 숫자를 찾는다.
        if max_c <= i:
            max_c = i

    for i in range(10):  # 일의 자리 숫자(0~9)
        if counter[i] == max_c:  # counter의 인덱스와 max_c값이 같으면
            the_most_num = i  # 인덱스 값을 the_most_num에 넣는다

    print(f"#{tc} {the_most_num} {max_c}")
