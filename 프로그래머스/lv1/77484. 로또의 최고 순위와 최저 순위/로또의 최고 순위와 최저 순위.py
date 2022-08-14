rank = [6, 6, 5, 4, 3, 2, 1]

def solution(lottos, win_nums):
    answer = []
    
    # 변경 가능한 0의 개수
    zero = lottos.count(0)
    
    # 민우가 뽑은 당첨 번호 수
    num = 0
    
    for i in win_nums:
        if i in lottos:
            num += 1
    
    # 최고는 변경 가능이 모두 맞을 경우
    max_num = num + zero
    
    # 최저는 변경 가능이 모두 틀릴 경우
    min_num = num
    
    answer.append(rank[max_num])
    answer.append(rank[min_num])
    
    return answer