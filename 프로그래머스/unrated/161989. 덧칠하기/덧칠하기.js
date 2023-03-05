function solution(n, m, section) {
    let answer = 0
    let cur = 0
    
    section.forEach(e => {
        if (cur < e) {
            cur = e + m - 1
            answer++
        }
    })
    
    return answer
}