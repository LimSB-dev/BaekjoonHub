t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = 0
    m_s_now = 0
    for i in range(n):
        li = list(map(int, input().split()))
        if li[0] == 1:
            m_s_now += li[1]
        elif li[0] == 2:
            m_s_now -= li[1]
            if m_s_now < 0:
                m_s_now = 0

        answer += m_s_now

    print(f'#{tc} {answer}')
