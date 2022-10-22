def check():
    # 간판의 높이 OR 폭 중 0이 있을 경우
    if h * w == 0:
        return False

    # 폰트 사이즈 따라 간판에 들어갈 수 있는 열의 수 만큼 0 생성
    sign = [0] * (h // font)

    # 열 INDEX
    row = 0

    for word in words:
        # 글자 가로 크기
        length = len(word)

        # 이미 행에 다른 글자가 있을 경우
        if sign[row] != 0:

            # 띄어쓰고 다음 글자가 들어가는 경우
            if sign[row] + ((length + 1) * font) <= w:
                sign[row] += ((length + 1) * font)

            # 들어가지 못하는 경우
            else:
                row += 1

                # 간판에 다음 줄이 없을 경우
                if row >= (h // font):
                    return False

                # 다음 줄에 글자를 넣을 수 있을 경우
                if sign[row] + (length * font) <= w:
                    sign[row] += length * font
                # 아무 글자도 없는데 글자가 들어가지 못하는 경우
                else:
                    return False
        # 행에 다른 글자가 없을 경우
        else:
            # 글자가 들어갈 수 있는 경우
            if sign[row] + (length * font) <= w:
                sign[row] += length * font
            # 아무 글자도 없는데 글자가 들어가지 못하는 경우
            else:
                return False

    return True


for tc in range(1, int(input()) + 1):
    h, w, n = map(int, input().split())
    words = list(input().split())
    font = 1
    answer = 0

    while True:

        # 간판에 안 들어갈 경우
        if not check():

            # 현재 폰트 사이즈는 안 되기 때문에 1 감소
            answer = font - 1
            break

        # 폰트 사이즈 키우기
        font += 1

        # 폰트 크기가 폭 혹은 높이보다 클 경우
        if font > h or font > w:

            # 현재 폰트 사이즈는 안 되기 때문에 1 감소
            answer = font - 1
            break

    print(f'#{tc} {answer}')
