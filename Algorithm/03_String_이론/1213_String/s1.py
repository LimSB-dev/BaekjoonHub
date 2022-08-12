import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for _ in range(1, 11):
    answer = 0
    tc = int(input())    
    target_word = input()
    words = input()
    
    # out of range error를 피하기 위해 뒤집어서 검토
    words = words[::-1]
    target_word = target_word[::-1]
    
    # 찾고자하는 단어의 길이
    target_word_cnt = 0
    
    for i in target_word:
        target_word_cnt += 1
    
    # 단어의 개수 탐색
    for i, word in enumerate(words):
        # 일치하는 단어의 수
        cnt = 0
        # 첫단어가 일치할 경우, 뒤의 단어도 검증
        if word == target_word[0]:
            # 반복문을 통해 뒤단어 검토
            for j in range(target_word_cnt):
                if words[i + j] == target_word[j]:
                    cnt += 1
                # 만약 다르다면 반복문 탈출
                else:
                    break
            # 만약 일치하는 단어의 수와 찾고자하는 단어의 길이가 같다면 answer 1 증가
            if cnt == target_word_cnt:
                answer += 1
    
    print(f'#{tc} {answer}')
