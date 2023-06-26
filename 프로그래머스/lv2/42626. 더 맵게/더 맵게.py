from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while True:
        min_value = heappop(scoville)
        
        if min_value >= K:
            break

        if len(scoville) == 0:
            return -1
        
        second_min_value = heappop(scoville)

        new_value = min_value + (second_min_value * 2)
        heappush(scoville, new_value)
        answer += 1
    
    return answer
