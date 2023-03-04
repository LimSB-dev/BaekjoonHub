function solution(t, p) {
    let pl = p.length
    let answer = 0
    
    for(let i = 0; i <= t.length - pl; i++) {
        if (Number(t.substring(i, pl + i)) <= Number(p)) {
            answer++
        }
    }
    
    return answer
}
