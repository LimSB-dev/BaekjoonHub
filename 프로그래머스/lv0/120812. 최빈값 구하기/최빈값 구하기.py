def solution(array):
    counting = [0] * 1001
    
    for num in array:
        counting[num] += 1
        
    max_value = max(counting)
    
    if counting.count(max_value) > 1:
        return -1
    else:
        return counting.index(max_value)