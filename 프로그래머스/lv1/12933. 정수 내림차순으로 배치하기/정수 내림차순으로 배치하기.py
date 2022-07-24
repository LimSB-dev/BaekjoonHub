def solution(n):
    answer = 0
    li = list(map(int, str(n).strip()))
    length = len(li)
    for _ in range(length):
        answer *= 10
        max_li = max(li)
        li.remove(max_li)
        answer += max_li
        
    return answer