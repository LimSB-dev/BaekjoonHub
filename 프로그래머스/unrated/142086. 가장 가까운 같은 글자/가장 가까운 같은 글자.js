function solution(s) {
    let answer = []
    let alphaMap = new Map()
    
    
    s.split('').forEach((e, idx) => {
        const position = alphaMap[e]
        
        if (position === undefined) {
            answer.push(-1)
        } else {
            answer.push(idx - position)
        }
        
        alphaMap[e] = idx
    })
    
    return answer
}