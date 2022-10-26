function solution(a, b, n) {
    let answer = 0;
    while (n >= a) {
        let newBottles = parseInt(n / a)
        newBottles *= b
        n = n % a
        n += newBottles
        answer += newBottles

    }
    return answer;
}