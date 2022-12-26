function solution(s) {
    let answer = 0
    let stack = []
    let queue = s.split('')
    
    while (queue.length !== 0) {
        nextString = queue.pop()
        
        if (stack.length !== 0) {
            if (stack[stack.length - 1] === nextString) {
                stack.pop()            
            } else {
                stack.push(nextString)  
            }
        } else {
            stack.push(nextString)        
        }
    }
    
    if (stack.length === 0) {
        answer = 1
    }
    
    return answer
}