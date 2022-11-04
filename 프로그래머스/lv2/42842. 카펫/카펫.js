function solution(brown, yellow) {
    let answer = []
    const total = brown + yellow
    
    for (let i = 1; i < brown; i++) {
        const [a, b] = [i, total / i]
        const edge = (a + b) * 2
        
        if (brown + 4 === edge && a * b === total) {
            answer = [b, a]
            break
        }
    }
    return answer
}