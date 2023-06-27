def solution(money):
    n = len(money)
    dp_1 = [0] + [0] * n
    dp_2 = [0] + [0] * n

    money_1 = money[1:]
    money_2 = money[:n-1]
    
    for i in range(2, n+1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + money_1[i-2])
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + money_2[i-2])
        
    return max(dp_1[-1], dp_2[-1])