bonus = ['S', 'D', 'T']
option = ['*', '#']
def solution(dartResult):
    answer = []
    for index, value in enumerate(dartResult):
        # 보너스
        if value in bonus:
            answer[-1] **= bonus.index(value) + 1
        # 옵션
        elif value in option:
            if value == '#':
                answer[-1] *= -1
            else:
                if len(answer) == 1:
                    answer[0] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
        #숫자
        else:
            
            # 10일 경우
            if value == '1' and dartResult[index + 1] == '0':
                answer.append(10)
                
            # 0이 아닌 경우
            elif value != '0':
                answer.append(int(value))
        
            # 10에서 나오는 0일 경우
            elif index != 0 and dartResult[index - 1] == '1':
                pass
            
            # 나머지 경우 모두 0
            else:
                answer.append(0)
                
    return sum(answer)