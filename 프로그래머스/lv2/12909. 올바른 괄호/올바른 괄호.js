function solution(s){
    let answer = true
    let stack = []
    
    for (bracket of s) {
        
        if (bracket === '(') {
            stack.push(bracket)
            continue
        } else {
            if (stack.length > 0) {
                stack.pop()
            } else {
                answer = false
                break
            }   
        }
    }
    
    if (stack.length > 0) {
        answer = false
    }
    
    return answer
}