#다른 행성의 숫자 리스트
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(int(input())):
    tc, N = input().split()
    arr = list(input().split())

    # 카운팅 정렬을 담을 리스트
    counter = [0] * 10

    # 카운팅 정렬
    for i in arr:
        counter[nums.index(i)] += 1

    answer = ''    
    for i in range(10):
        answer += (nums[i] + ' ') * counter[i]

    print(f'{tc}\n', answer)