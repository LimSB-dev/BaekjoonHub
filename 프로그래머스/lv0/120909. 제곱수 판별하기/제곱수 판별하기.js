function solution(n) {
    const sqrtNum = Math.floor(Math.sqrt(n))
    const answer = sqrtNum * sqrtNum === n ? 1 : 2
    
    return answer
}