function solution(keymap, targets) {
    let answer = [];
    let keyMap = new Map()
    
    const getMap = (keys) => {
        keys.forEach((key, idx)=> {
            const index = idx + 1
            
            if (keyMap[key] === undefined) {
                keyMap[key] = index
            } else {
                keyMap[key] = Math.min(keyMap[key], index)
            }
        })
    }
    
    keymap.forEach(keys => {
        getMap(keys.split(''))
    })
    
    console.log(keyMap)
    
    for (let i = 0; i < targets.length; i++) {
        const target = targets[i]
        let result = 0
        
        for (let j = 0; j < target.length; j++) {
            const key = target[j]
            
            if (keyMap[key] === undefined) {
                result = -1
                break
            } else {
                result += keyMap[key]
            }
        }
        
        answer.push(result)   
    }
    
    return answer
}