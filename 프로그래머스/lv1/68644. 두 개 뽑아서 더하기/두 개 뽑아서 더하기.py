def solution(numbers):
    answer = []
    # list out of range를 피해기 위해 범위에 -1
    for i in range(len(numbers) - 1):
        # i 이후의 값을 더하기 위해 i + 1을 범위의 시작으로 한다.
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    # 리스트 answer에서 중복되는 값을 제거 후 리스트로 변환한 뒤 오름차순으로 정렬 
    return sorted(list(set(answer)))