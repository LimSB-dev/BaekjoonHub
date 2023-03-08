function solution_(n, from, through, to) {
    if(n == 1)
        return [[from,to]]
    let result = []
    result = result.concat(solution_(n - 1, from, to, through))
    result.push([from, to])
    result = result.concat(solution_(n - 1, through, from, to))
    return result
}

function solution(n) {
    return solution_(n,1,2,3)
}