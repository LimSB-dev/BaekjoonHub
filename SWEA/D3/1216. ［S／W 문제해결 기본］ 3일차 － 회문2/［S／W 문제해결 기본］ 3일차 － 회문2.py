def solution(array, L):
    for word in array:  # 1 ~ 100
        for i in range(100 - L + 1):
            for j in range(L // 2):
                if word[i + j] != word[i + L - 1 - j]:
                    break
            else:
                return L
    return 0


for _ in range(10):
    tc = int(input())
    arr1 = [input() for _ in range(100)]
    arr2 = [''.join(i) for i in zip(*arr1)]
    answer = 1
    
    for length in range(2, 101):
        if length > answer + 2:
            break
        # 가로 확인
        if answer < solution(arr1, length):
            answer = length

    length = answer + 1
    for length in range(length, 101):
        if length > answer + 2:
            break
        # 세로 확인
        if answer < solution(arr2, length):
            answer = length
            
    print(f'#{tc} {answer}')
