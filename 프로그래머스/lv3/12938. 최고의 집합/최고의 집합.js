function solution(n, s) {
    let answer = []
    
    while (n !== 0) {
        // 종료 조건
        if (n > s) {
            return [-1]
        }
        
        
        const result = Math.floor(s / n)
        s -= result
        n--
        answer.push(result)
    }
    
    return answer
}