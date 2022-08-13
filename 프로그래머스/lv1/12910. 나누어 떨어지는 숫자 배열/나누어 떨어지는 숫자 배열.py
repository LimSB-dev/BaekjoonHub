def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer