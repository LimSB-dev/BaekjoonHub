const brackets = {
    open: ["(", "{", "["],
    close: [")", "}", "]"]
}

function check(arr) {
    const stack = []
    
    for (let i = 0; i < arr.length; i++) {
        const bracket = arr[i]
        if (brackets.open.includes(bracket)) {
            stack.push(bracket)
        } else if (stack.length > 0) {
            const openBracket = stack[stack.length - 1]
            const openIndex = brackets.open.indexOf(openBracket)
            const closeIndex = brackets.close.indexOf(bracket)
            
            if (openIndex !== closeIndex) {
                return false
            } else {
                stack.pop()
            }
            
        } else {
            return false
        }
    }
    
    if (stack.length > 0) {
        return false
    }
    
    return true
}


function solution(s) {
    let answer = 0;
    
    const s_arr = s.split('')
    
    for (let i = 0; i < s.length; i ++) {
        const head = s_arr.shift()
        s_arr.push(head)
        if (check(s_arr)) {
            answer++
        }
    }
    
    return answer;
}