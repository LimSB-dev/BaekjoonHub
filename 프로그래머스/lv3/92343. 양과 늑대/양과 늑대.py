def solution(info, edges):
    global answer
    answer = 0
    visited = [False] * len(info)
    visited[0] = True
    
    
    def dfs(sheep, wolf):
        global answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return 

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = False


    dfs(1, 0)

    return answer
