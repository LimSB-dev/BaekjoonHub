def solution(arr):
    min_number = min(arr)
    arr.remove(min_number)
    if len(arr) == 0:
        return [-1]
    else:
        return arr