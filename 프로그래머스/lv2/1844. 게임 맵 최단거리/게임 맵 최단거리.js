// 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

function solution(maps) {
    const [row, col] = [maps.length - 1, maps[0].length - 1]
    
    const queue = [[0, 0, 1]]
    
    // 방문 처리
    maps[0][0] = 0
    
    while(queue.length !== 0) {
        
        // 큐 추출
        let [r, c, count] = queue.shift()

        // 종료
        if(r === row && c === col) return count
        
        // 상 하 좌 우 확인
        for(let i = 0; i < 4; i++) {
            const [nr, nc] = [r + dr[i], c + dc[i]]
            
            // 범위 밖으로 나갈 경우
            if (0 > nr || nr > row || 0 > nc || nc > col) continue
   
            // 방문 확인
            if (maps[nr][nc] === 0) continue
            
            // 방문 처리
            maps[nr][nc] = 0
            
            // 큐 추가       
            queue.push([nr, nc, count + 1])
        }
    }
    
    return -1
}