function solution(msg) {
    let answer = []
    let wordMap = new Map()
    let idx = 27
    
    for (let i = 1; i <= 26; i++) {
        const code = i + 64
        
        wordMap[String.fromCharCode(code)] = i
    }
    
    while (msg !== '') {
        for (let i = msg.length; i >= 0; i--) {    
            const w = msg.slice(0, i)
            const wc = msg.slice(0, i + 1)
            
            if (wordMap[w]) {
                
                answer.push(wordMap[w])
                
                msg = msg.slice(i, msg.length)

                wordMap[wc] = idx
                
                idx++
                break
            }
        }
    }
    return answer
}