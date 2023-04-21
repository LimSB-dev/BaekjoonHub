def solution(arr, query):
    s = e = 0
    for index, value in enumerate(query):
        if index % 2 == 0:
            e = s + value
        else:
            s += value
            
    return arr[s:e] if s != e else [-1]