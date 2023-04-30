from collections import deque

def find_result(price, prices):
    if len(prices) == 0:
        return 0
    result = 0
    
    for p in prices:
        result += 1
        
        if price > p:
            break
    
    return result


def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        
        result = find_result(price, prices)
        answer.append(result)
        
    return answer