function solution(food) {
    let answer = ''
    for (let i = 1; i < food.length; i++) {
        const cnt = food[i]
        
        answer += `${i}`.repeat(parseInt(cnt / 2))
    }
    
    const reversedAnswer = answer.split('').reverse().join('')
    
    answer += '0' + reversedAnswer
    
    return answer
}