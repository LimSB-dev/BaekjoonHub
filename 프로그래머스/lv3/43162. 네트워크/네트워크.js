function solution(n, computers) {
    let answer = 0
    let visited = new Array(n).fill(false)
    
    // DFS 함수
    const dfs = (computers, visited, idx) => {
        visited[idx] = true
        for (let i = 0; i < computers.length; i++) {
            if (computers[idx][i] === 1 && !visited[i]) {
                dfs(computers, visited, i)
            }
        }
    }  
    
    // 모든 컴퓨터에 대해 DFS 수행
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(computers, visited, i)
            answer++
        }
    }
    
    return answer
}