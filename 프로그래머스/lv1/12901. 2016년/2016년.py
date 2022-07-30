day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]
day_28 = [2]
days = ['FRI','SAT','SUN','MON','TUE','WED','THU']

def solution(a, b):
    answer = ''
    date_count = b - 1
    for i in range(a):
        if i in day_31:
            date_count += 31
        elif i in day_30:
            date_count += 30
        elif i in day_28:
            date_count += 29
    answer = days[date_count % 7]
    
    return answer