def subset(arr: list, depth: int, total: int) -> None:

    # 가지치기(pruning): 합이 10 초과면 더 진행할 필요가 없다.
    if total > 10:
        return

    # 전체 원소의 개수만큼 재귀가 진행됐다면 종료
    if depth == len(powerset):

        # 원소의 합이 10이라면 부분집합 출력
        if total == 10:
            print(arr)
        return

    # 1. 현재 원소를 뽑고 재귀
    subset(arr + [powerset[depth]], depth + 1, total + powerset[depth])

    # 2. 현재 원소를 뽑지 않고 재귀
    subset(arr, depth + 1, total)


powerset = list(range(1, 11))
subset([], 0, 0)
