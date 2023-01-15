function solution(citations) {
    let answer = 0;
    const n = citations.length
    
    for (let i = 0; i <= n; i++) {
        let hUp = 0
        let hDown = 0
        
        citations.forEach((citation) => {
            if (citation > i) {
                hUp++
            } else if (citation === i) {
                hUp++
                hDown++
            } else {
                hDown++
            }
        })
        
        if (hUp >= i && hDown <= i) {
            answer = i
        }
    }
    
    return answer;
}