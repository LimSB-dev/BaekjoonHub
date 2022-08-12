def solution(n, arr1, arr2):
    answer = [[''] * n for _ in range(n)]
    
    # 배열 채우기
    for i in range(n):
        answer[i] = str(int(format(arr1[i], 'b')) + int(format(arr2[i], 'b')))
        while len(answer[i]) < n:
            answer[i] = '0' + answer[i]
        
        answer[i] = answer[i].replace('0', ' ')
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('2', '#')
        
    return answer