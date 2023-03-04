function solution(t, p) {
    let pl = p.length
    let tl = t.length
    let answer = 0

    if (tl < pl) {
        return 0
    }

    for(let i = 0; i <= tl - pl; i++) {
        if (Number(t.substring(i, pl + i)) <= Number(p)) {
            answer++
        }
    }

    return answer
}