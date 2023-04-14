# 약관 판단 후 유효기간을 지나 파기되어야 한다면 True 반환
def check(cur_year, cur_month, cur_day, year, month, day, value):
    month += value

    if month > 12:
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1

    if cur_year != year:
        return cur_year > year

    if cur_month != month:
        return cur_month > month

    return cur_day >= day

def solution(today, terms, privacies):
    answer = []
    cur_year, cur_month, cur_day = map(int, today.split('.'))
    expiration = {}

    for term in terms:
        key, value = term.split(' ')
        expiration[key] = int(value)

    for idx, privacie in enumerate(privacies):
        date, key = privacie.split(' ')
        year, month, day = map(int, date.split('.'))
        value = expiration[key]

        # 유효기간 확인
        if check(cur_year, cur_month, cur_day, year, month, day, value):
            answer.append(idx + 1)

    return answer
