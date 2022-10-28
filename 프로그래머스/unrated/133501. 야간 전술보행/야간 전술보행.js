function check(s1, s2, t1, t2) {
    let answer = 10000000
    const totalTime = t1 + t2
    const cnt = parseInt(s1 / totalTime)
    const startTime = totalTime * cnt
    const fristWorkTimes = Array.from(Array(t1).keys()).map(x => x + startTime + 1)
    const secondWorkTimes = Array.from(Array(t1).keys()).map(x => x + startTime + totalTime + 1)
    
    const workTimes = fristWorkTimes.concat(secondWorkTimes)
    
    for (workTime of workTimes) {
        
        if (s1 <= workTime && workTime <= s2) {
            answer = workTime
            break
        }
    }
    
    return answer
}


function solution(distance, scope, times) {
    let answer = distance
    
    for (let i = 0; i < scope.length; i++) {
        const [a, b] = scope[i]
        const [c, d] = times[i]
        
        const dist = check(Math.min(a, b), Math.max(a, b), c, d)
        
        if (dist < answer) {
            answer = dist
        }
    }
    
    return answer
}