function solution(quiz) {
    let answer = []
    
    quiz.forEach(e => {
        const [X, O, Y, E, Z] = e.split(' ')
        
        if (O === '+') {
            if (Number(X) + Number(Y) === Number(Z)) {
                answer.push('O')
            } else {
                answer.push('X') 
            }
        } else if (O === '-') {
            if (Number(X) - Number(Y) === Number(Z)) {
                answer.push('O')
            } else {
                answer.push('X') 
            }
        }
    })
    return answer
}