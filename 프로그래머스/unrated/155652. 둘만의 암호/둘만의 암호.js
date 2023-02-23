function decode(word, skipMap, index) {
    let cnt = 0
    while (cnt !== index) {
        cnt++
        
        nextIndex = word.charCodeAt() + 1
        
        if (nextIndex > 122) nextIndex = 97
        
        word = String.fromCharCode(nextIndex)

        if (skipMap.get(word)) cnt-- 
    }
    
    return word
}

function solution(s, skip, index) {
    let answer = '';
    
    const skipMap = skip.split('').reduce((map, word) => {
        map.set(word, true);
        return map;
    }, new Map)
    
    s.split('').map(word => {
        answer = answer + decode(word, skipMap, index)
    })
    
    return answer;
}