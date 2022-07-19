# 조건에는 보이지 않지만 P가 K 보다 항상 큰 것 같다.
def scert_number(P, K):
    answer = 0
    answer = P - K + 1
    return answer

P, K = map(int, input().split())

print(scert_number(P, K))