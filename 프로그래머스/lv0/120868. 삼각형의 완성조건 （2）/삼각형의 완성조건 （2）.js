function solution(sides) {
    let answer = 0
    const [a, b] = sides
    const min_side = Math.abs(a - b) + 1
    const max_side = (a + b)
    
    answer = max_side - min_side
    
    return answer;
}