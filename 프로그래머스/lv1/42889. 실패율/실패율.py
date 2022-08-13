'''
실패율: 스테이지 도달했지만 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
N: 전체 스테이지 개수
stage: 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호
'''


def solution(n, stages):

    # 실패율 내림차순 리스트
    answer = []

    # 카운팅 정렬
    # index: 스테이지 / value: 아직 클리어하지 못한 플레이어의 수
    counter = [0] * (n + 2)
    # n = 5 / [0, 0, 0, 0, 0, 0, 0]

    for i in stages:
        # stages에는 1이상 n + 1 이하의 자연수가 담겨있다.
        counter[i] += 1
        # [0, 1, 3, 2, 1, 0, 1]

    # 스테이지에 도달한 플레이어 수를 담을 변수
    stage_arrival = counter[-1]
    # 1

    # 실패율
    fail = 0

    # stage 번호가 key값이고 실패율이 value값인 dictonary 생성
    dict_fail = {}

    for i in range(n):
        stage_arrival += counter[n - i]

        # 스테이지에 도달한 사람이 있을 경우
        if stage_arrival != 0:
            fail = counter[n - i] / stage_arrival

        dict_fail[f'{n - i}'] = fail
        # dict_fail = {'1': 1/8, '2': 3/7, '3': 2/4, '4': 1/2, '5': 0}

    # value값을 기준으로 key값 내림차순
    sorted_fail = sorted(dict_fail.items(), key = lambda item: item[1], reverse = True)
    # sorted_fail = [('4', 1/2), ('3', 2/4), ('2', 3/7), ('1', 1/8), ('5', 0)]

    # 버블 정렬
    # 만약 value값이 같다면 낮은 stage가 앞으로...
    for i in range(n-1, 0, -1):
        for j in range(i):
            # 만약 두 value값(실패율)이 같고 key값(스테이지)이 내림차순일 경우
            if sorted_fail[j][1] == sorted_fail[j+1][1] and int(sorted_fail[j][0]) > int(sorted_fail[j+1][0]):
                # 두 값을 변경하여 오름차순으로 만든다.
                sorted_fail[j], sorted_fail[j+1] = sorted_fail[j+1], sorted_fail[j]
    # sorted_fail = [('3', 2/4), ('4', 1/2), ('2', 3/7), ('1', 1/8), ('5', 0.0)]

    # 조건에 맞게 정렬된 dictionary에서 key값(스테이지)만 저장
    for i in sorted_fail:
        answer.append(int(i[0]))

    return answer
