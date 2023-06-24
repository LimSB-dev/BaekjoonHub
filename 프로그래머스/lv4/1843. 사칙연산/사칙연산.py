INF = 10e9

def solution(arr):
    nums, ops = [], []
    for idx, element in enumerate(arr):
        nums.append(element) if not idx % 2 else ops.append(element)

    N = len(nums)
    dp_max = [[-INF] * N for _ in range(N)]
    dp_min = [[INF] * N for _ in range(N)]

    for scope in range(N):
        for start in range(N - scope):
            end = start + scope
            if start == end:
                dp_max[start][start] = dp_min[start][start] = int(nums[start])
                continue

            for mid in range(start, end):
                if ops[mid] == '+':
                    dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid + 1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid + 1][end], dp_min[start][end])
                elif ops[mid] == '-':
                    dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid + 1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid + 1][end], dp_min[start][end])

    return dp_max[0][-1]