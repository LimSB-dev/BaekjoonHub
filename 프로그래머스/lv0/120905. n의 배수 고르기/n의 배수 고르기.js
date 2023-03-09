function solution(n, numlist) {
    let answer = []
    
    numlist.forEach(num => {
        if (num % n === 0) {
            answer.push(num)
        }
    })
    
    return answer
}