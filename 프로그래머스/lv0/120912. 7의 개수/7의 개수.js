function solution(array) {
    let answer = 0
    
    array.forEach(num => {
        while (num >= 1) {
            answer = num % 10 === 7 ? answer + 1 : answer 
            num = Math.floor(num / 10)
        }
    })
    
    return answer
}