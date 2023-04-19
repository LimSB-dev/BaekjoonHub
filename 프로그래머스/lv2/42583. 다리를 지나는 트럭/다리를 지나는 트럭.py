from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    bridge = deque([0] * bridge_length)
    sum_bridge = 0
    queue = deque(truck_weights)
    
    while queue:
        exit = bridge.popleft()
        sum_bridge -= exit
        
        # 다리 위의 총 무게 + 들어올 트럭의 무게의 합이 견딜 수 있는 무게보다 작을 경우
        if sum_bridge + queue[0] <= weight:
            truck_weight = queue.popleft()
            sum_bridge += truck_weight
            bridge.append(truck_weight)
        else:
            bridge.append(0)
        
        answer += 1    
    
    return answer