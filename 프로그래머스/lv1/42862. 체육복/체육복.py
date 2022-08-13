def solution(n, lost, reserve):
    answer = 0
    students= [1] * n

    # 도난 학생과 여분의 옷 학생 선발
    # 카운팅 정렬
    for i in range(n):
        if i + 1 in lost:
            students[i] -= 1
        if i + 1 in reserve:
            students[i] += 1

    # greedy
    # 1번 학생부터 n번 학생까지 탐색
    for i in range(n):

        # index값이 0인 경우 앞번호 학생이 없음
        if i != 0:
            if students[i] == 0 and students[i - 1] == 2:
                students[i] += 1
                students[i - 1] -= 1

        # index값이 n - 1인 경우 뒷번호 학생이 없음
        if i != n - 1:
            if students[i] == 0 and students[i + 1] == 2:
                students[i] += 1
                students[i + 1] -= 1

    # 수업을 들을 수 있는 학생 수
    for student in students:
        if student != 0:
            answer += 1

    return answer
