def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            while delivery < deliveries[i] or pickup < pickups[i]:
                delivery += cap
                pickup += cap
                answer += (i + 1) * 2
            delivery -= deliveries[i]
            pickup -= pickups[i] 
    return answer
