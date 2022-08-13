def solution(array, commands):
    answer = []
    for i in commands:
        
        start = i[0]
        end = i[1]
        target = i[2]
        
        cut_array = array[start - 1:end]
        
        sorted_cut_array = sorted(cut_array)
        
        answer.append(sorted_cut_array[target - 1])
        
    return answer