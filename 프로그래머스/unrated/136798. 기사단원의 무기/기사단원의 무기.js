function find(number) {
    let power = 0
    const sqrtNum = Math.sqrt(number)
    
    for (let i = 1; i <= sqrtNum; i++) {
        if (number % i === 0) {
            power += 2
        }
        
        if (i === sqrtNum) {
            power--
        }
    }
    
    return power
}

function solution(number, limit, power) {
    let answer = 0
    
    for (let i = 1; i <= number; i++) {
        let weapon = find(i)
        
        if (weapon > limit) {
            weapon = power
        }
        
        answer += weapon
    }
    
    return answer
}