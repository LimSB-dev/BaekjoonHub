# Title: 단어 변환
# Link: https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


# 단어 변환 가능 여부
def is_possible(begin, word):
    # 다른 경우
    diff = 0

    # begin과 word의 한 글자씩 비교
    for b, w in zip(begin, word):
        # 다른 경우
        if b != w:
            # diff 1 증가
            diff += 1

    # diff가 1인 경우
    if diff == 1:
        # 변환 가능 True 반환
        return True

    # 그 외 False 반환
    return False


def solution(begin, target, words):
    # 변환할 수 없는 경우
    if target not in words:
        return 0

    # 큐 생성
    queue = deque([(begin, 0)])

    # BFS
    while queue:
        # 큐에서 단어와 변환 횟수 꺼내기
        begin, count = queue.popleft()

        # 종료 조건
        if begin == target:
            # 변환 횟수 반환
            return count

        # 다음 단어 탐색
        for word in words:
            if is_possible(begin, word):
                # 큐에 추가
                queue.append((word, count+1))
                # 중복 방지
                words.remove(word)
