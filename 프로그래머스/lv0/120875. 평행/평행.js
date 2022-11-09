function solution(dots) {    
    for (let i = 1; i < 4; i++) {
        const arr = Array(4).fill(0).map((x, y) => x + y)
        
        arr.splice(i, 1)
        arr.splice(0, 1)
        
        line1 = (dots[0][1] - dots[i][1]) / (dots[0][0] - dots[i][0])
        
        const [a, b] = arr       
        line2 = (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0])
        
        if (line1 === line2) {
            return 1
        }
    }
    
    return 0
}