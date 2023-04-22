import math

def solution(n, stations, w):
    answer = 0
    s = 1

    for station in stations:
        e = station - w
        total = e - s
        if e > 1 and total > 0:
            answer += math.ceil(total / ((2 * w) + 1))
        
        s = station + w + 1
    
    if s <= n:
        total = (n + 1) - s
        answer += math.ceil(total / ((2 * w) + 1))

    return answer