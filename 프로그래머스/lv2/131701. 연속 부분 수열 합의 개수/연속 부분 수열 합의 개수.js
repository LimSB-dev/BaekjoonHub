function solution(elements) {
    let answer = []
    const cnt = elements.length
    
    for (let i = 0; i < cnt; i++) { 
        elements.push(elements[i])
    }
    
    for (let i = 0; i < cnt; i++) {
        for (let j = 1; j < cnt; j++) {        
            const newElements = elements.slice(i, i + j)
            
            let sumValue = newElements.reduce((a, b) => a + b, 0)
        
            answer.push(sumValue)
        }
    }
    
    answer = [...new Set(answer)]
    
    // console.log(answer)
    
    return answer.length + 1
}