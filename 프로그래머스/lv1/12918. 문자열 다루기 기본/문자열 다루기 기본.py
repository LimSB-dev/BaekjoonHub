def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    else:
        for i in s:
            if i in ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']:
                continue
            
            answer = False
    return answer