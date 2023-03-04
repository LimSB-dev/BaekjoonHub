function solution(s) {
    let answer = 0
    let x = ''
    let cntX = 1
    let cntY = 0
    
    s.split('').forEach(e => {
        if (x === '') {
            x = e
        } else {
            if (x === e) {
                cntX++
            } else {
                cntY++
            }
            
            if (cntX === cntY) {
                answer++
                x = ''
                cntX = 1
                cntY = 0
            }
        }
    })
    
    if (x !== '') {
        answer++
    }
    
    return answer
}