function solution(n, m, section) {
    let answer = 0;
    let wall = new Array(n).fill(true)
    let i = 0
    
    wall = wall.map((e, idx) => {
        return section.includes(idx + 1) ? false : true
    })
    
    while (true) {
        if (i > n - m) {
            break
        }
        
        if (!wall[i]) {
            for (let j = 0; j < m; j++) {
                wall[i + j] = true
            }
            
            i += m
            answer++ 
        } else {
            i++
        }
    }
    
    if (wall.includes(false)) answer++
    
    return answer;
}