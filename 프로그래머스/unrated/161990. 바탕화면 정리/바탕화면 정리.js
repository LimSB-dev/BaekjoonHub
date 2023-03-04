const INF = 999999999

function solution(wallpaper) {
    let left = INF
    let up = INF
    let right = -INF
    let down = -INF
    
    for (let row = 0; row < wallpaper.length; row++) {
        for (let col = 0; col < wallpaper[0].length; col++) {
            const element = wallpaper[row][col]
            if (element === '#') {
                left = Math.min(left, col)
                up = Math.min(up, row)
                right = Math.max(right, col + 1)
                down = Math.max(down, row + 1) 
            }
        }
    }
    
    return [up, left, down, right]
}