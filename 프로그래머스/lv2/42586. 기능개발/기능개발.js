function solution(progresses, speeds) {
    let answer = [];
    
    while (progresses.length > 0) {
        let cnt = 0
        
        progresses.forEach((e, i) => {
            progresses[i] += speeds[i]
        })
        
        if (progresses[0] >= 100) {
            for (let i = 0; i < progresses.length; i++) {
                if (progresses[i] >= 100) {
                    cnt++
                } else {
                    break
                }
            }
            
            if (cnt !== 0) {
                answer.push(cnt)
            }
            
            for (let i = 0; i < cnt; i++) {
                progresses.shift()
                speeds.shift()
            }
        }
    }
    
    return answer;
}