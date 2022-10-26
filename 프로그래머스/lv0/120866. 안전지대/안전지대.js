function solution(board) {
    let answer = 0
    const n = board.length
    
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            let area = board[row][col]
            
            if (area === 0) {
                for (let r = -1; r < 2; r++) {
                    for (let c = -1; c < 2; c++) {
                        const nr = row + r
                        const nc = col + c
                        if (0 <= nr && nr < n && 0 <= nc && nc < n) {
                            if (board[nr][nc] === 1) {
                                board[row][col] = 2
                            }
                        }
                    }
                }
            }
        }    
    }
    
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            let area = board[row][col]
            
            if (area === 0) {
                answer++
            }
        }
    }
    
    return answer
}