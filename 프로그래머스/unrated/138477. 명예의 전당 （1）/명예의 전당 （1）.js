function solution(k, score) {
    let answer = []
    let honor = []
    
    score.forEach(e => {
        honor.push(e)
        
        honor.sort((a, b) => a - b)
        
        if (honor.length > k) {
            honor.shift()
        }
        
        answer.push(honor[0])
    })
    
    return answer
}