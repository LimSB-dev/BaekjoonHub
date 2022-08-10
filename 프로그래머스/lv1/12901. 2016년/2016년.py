# 최대 일 수 별 월 리스트
day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]
day_29 = [2]
# 1일이 금요일인 요일 리스트
days = ['FRI','SAT','SUN','MON','TUE','WED','THU']

def solution(a, b):
    # 요일을 대입할 문자열 answer 생성
    answer = ''
    
    # 모든 일 수를 더할 변수
    # 변수에 할당된 값을 0이 아닌 b - 1로 설정한 이유
    # 현재 달은 1일을 빼주어야 하기 때문 및
    # for문의 범위를 range(a)로 설정하기 위해서이다.
    date_count = b - 1
    
    # 달마다 일 수를 더하기 위한 반복문
    for i in range(a):
        if i in day_31:
            date_count += 31
        elif i in day_30:
            date_count += 30
        elif i in day_29:
            date_count += 29
    
    # 총 일 수 date_count를 7로 나눈 나머지를 index값으로 설정
    answer = days[date_count % 7]
    
    return answer