special = ['-', '_', '.']
num = list(map(str, range(10)))


def solution(new_id):
    answer = ''
    
    # 1단계
    for i in new_id:
        if 65 <= ord(i) <= 90:
            answer += i.lower()
        else:
            answer += i

    # 2단계
    for i in answer:
        if i.isalpha():
            pass
        elif i in special:
            pass
        elif i in num:
            pass
        else:
            answer = answer.replace(i, '')
        
    # 3단계
    while True:
        answer = answer.replace('..', '.')
        if answer.count('..') == 0:
            break
    
    # 4단계
    if answer:
        if answer[0] == '.':
            answer = answer[1:]
    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 5단계
    if not answer:
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer