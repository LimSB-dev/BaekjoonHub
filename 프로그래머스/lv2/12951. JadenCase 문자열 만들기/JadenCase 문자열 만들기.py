def solution(s):
    answer = ' '
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        elif s[i].isalpha():
            
            if answer[-1] == ' ':
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            
        else:
            answer += s[i]
            
    return answer[1:]