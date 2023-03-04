function solution(k, m, score) {
    let answer = 0
    let boxs = [] 
    
    score = score.sort((a, b) => b - a)
    
    score.forEach(apple => {
        boxs.push(apple)
        
        if (boxs.length === m) {
            const minValue = boxs[m - 1]
            answer += minValue * m
            boxs = []
        }
    })
    
    return answer
}