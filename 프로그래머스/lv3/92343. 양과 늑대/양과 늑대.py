answer = 0
def solution(info, edges):
    visited = [False] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            global answer
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

    visited[0] = True
    dfs(1, 0)

    return answer