def solution(numbers):
    # 숫자를 문자열로 변환하여 배열에 저장
    numbers = list(map(str, numbers))
    
    # 문자열을 비교하여 정렬하는 함수 정의
    numbers.sort(key=lambda x: x*3, reverse=True)
    # x*3을 하는 이유는 문자열 비교 시 "3"이 "30"보다 작아야 하기 때문
    
    # 정렬된 문자열 배열을 이어붙여 가장 큰 수 생성
    answer = ''.join(numbers)
    
    # 결과를 문자열로 반환
    return answer if int(answer) != 0 else "0"
