def solution(s):
    li = []
    count = 0
    for i in s:
        if i == ' ':
            li.append(i)
            count = 0
        else:
            if not li:
                if count % 2 == 0:
                    li.append(i.upper())
                else:
                    li.append(i.lower())
            elif i != ' ':
                if count % 2 == 0:
                    li.append(i.upper())
                else:
                    li.append(i.lower())
            count += 1                
    
    answer = ''
    
    for i in li:
        answer += i
    
    return answer