def solution(s):
    # 가운데 글자를 반환받을 변수
    answer = ''
    
    # 만약 단어의 길이가 홀수라면
    if len(s) % 2:
        # 가운데 한글자를 answer에 대입
        answer = s[len(s)//2]
        
    # 만약 단어의 길이가 짝수라면
    else:
        # 가운데 두글자를 answer에 대입
        answer = s[len(s)//2-1:len(s)//2+1]
        
    return answer