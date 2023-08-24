import sys
input = sys.stdin.readline

INF = float('inf')  # 무한을 의미하는 값

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[0] * (n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] == 0:
        graph[a-1][b-1] = c
    else:
        graph[a-1][b-1] = min(graph[a-1][b-1], c)


def floyd_warshall(graph):
    """_summary_
    플로이드 워셜 알고리즘을 이용하여 모든 정점에서 모든 정점으로의 최단 경로를 구합니다.
    자기 자신으로 가는 경로는 무조건 0으로 초기화하고, 만약 갈 수 없는 경로는 0으로 표현합니다.
    """
    # 2차원 리스트를 복사하여 결과 그래프를 초기화합니다.
    result = graph

    # k = 거쳐가는 노드
    for k in range(n):
        # i = 출발 노드
        for i in range(n):
            # j = 도착 노드
            for j in range(n):
                if i == j:
                    result[i][j] = 0
                elif result[i][k] != 0 and result[k][j] != 0:
                    if result[i][j] == 0:
                        result[i][j] = result[i][k] + result[k][j]
                    else:
                        result[i][j] = min(
                            result[i][j], result[i][k] + result[k][j])

    return result


result = floyd_warshall(graph)

for i in range(n):
    print(*result[i])
