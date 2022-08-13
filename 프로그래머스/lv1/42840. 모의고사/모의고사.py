'''
수포자 1
1, 2, 3, 4, 5, 1, 2 ...

수포자 2
2, 1, 2, 3, 2, 4, 2, 5, 2, 1 ...
index: value
1: 1 / 3: 3 / 5: 4 / 7: 5 / 9: 1 ...
(index // 2) % 4
0: 1 / 1: 3 / 2: 4 / 3: 5 / 0: 1 ...

수포자 3
3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3 ...
'''

two = [1, 3, 4, 5]
three = [3, 1, 2, 4 ,5]


def solution(answers):
    # 등수를 담을 리스트
    answer = []
    
    # 카운팅 정렬
    counter = [0] * 4
    
    # 점수 계산
    for index, value in enumerate(answers):
        # 수포자 1
        if (index % 5) + 1 == value:
            counter[1] += 1
        
        # 수포자 2
        # 짝수
        if index % 2 == 0 and value == 2:
            counter[2] += 1
        # 홀수
        elif index % 2 != 0 and two[(index//2) % 4] == value:
            counter[2] += 1
        
        # 수포자 3
        if three[(index//2) % 5] == value:
            counter[3] += 1
    
    # 최대 점수
    max_value = max(counter)
    
    # 오름차순으로 탐색하기 때문에 자동 오름차순
    for i in range(1, 4):
        # 최대 점수와 동점일 경우 answer에 저장
        if counter[i] == max_value:
            answer.append(i)
        
    return answer