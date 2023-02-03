// 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

function solution(maps) {
    let answer = []
    let matrix = []
    
    maps.forEach(row => {
        matrix.push(row.split(''))
    })
    
    const [row, col] = [matrix.length - 1, matrix[0].length - 1]
    
    for (let i = 0; i <= row; i++) {
        for (let j = 0; j <= col; j++) {
            let value = matrix[i][j]
            
            // 방문 확인
            if (value === 'X') continue
            
            // 방문 처리
            matrix[i][j] = 'X'
            
            value = Number(value)
            
            // 큐 생성
            const queue = [[i, j]]

            while(queue.length !== 0) {

                // 큐 추출
                let [r, c] = queue.shift()
                
                // 상 하 좌 우 확인
                for(let i = 0; i < 4; i++) {
                    const [nr, nc] = [r + dr[i], c + dc[i]]
                    
                    // 범위 밖으로 나갈 경우
                    if (0 > nr || nr > row || 0 > nc || nc > col) continue

                    let nv = matrix[nr][nc]
                    
                    // 방문 확인
                    if (nv === 'X') continue

                    // 방문 처리
                    matrix[nr][nc] = 'X'
                    
                    value += Number(nv)
                    
                    // 큐 추가       
                    queue.push([nr, nc])
                }
            }
            
            answer.push(value)
        }
    }
    
    if (answer.length === 0) return [-1]
    
    answer.sort((a, b) => a - b)
    
    return answer
}