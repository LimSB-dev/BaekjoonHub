function solution(n, words) {
    let answer = [0, 0];
    let curWords = [];
    let idx = 1
    let order = 1
    let curLast = words[0][0] 
    
    for (let i = 0; i < words.length; i++) {
        const word = words[i]
        const curFirst = word[0]
        
        if (curWords.includes(word)) {
            answer = [idx, order]
            break
        }
        
        if (curFirst !== curLast) {
            answer = [idx, order]
            break
        }
        
        idx++
        if (idx > n) {
            idx = 1
            order++
        }
        
        curWords.push(word)
        curLast = word[word.length - 1]
    }
    
    return answer;
}