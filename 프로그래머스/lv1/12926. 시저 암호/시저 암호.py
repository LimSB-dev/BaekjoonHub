def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        else:
            num_i = ord(i)
            if 65 <= num_i <= 90:
                num_i += n
                if 90 < num_i:
                    num_i %= 90
                    num_i += 64
                    answer += chr(num_i)
                    continue
                answer += chr(num_i)
            elif 97 <= num_i <= 122:
                num_i += n
                if 122 < num_i:
                    num_i %= 122
                    num_i += 96
                    answer += chr(num_i)
                    continue
                answer += chr(num_i)
                
    return answer