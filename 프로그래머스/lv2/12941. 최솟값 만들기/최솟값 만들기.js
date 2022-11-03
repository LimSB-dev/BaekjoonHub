function solution(A,B){
    let answer = 0;
    const sortedA = A.sort((a, b) => a - b)
    const reversedB = B.sort((a, b) => b - a)

    for (let i = 0; i < A.length; i++) {
        answer += sortedA[i] * reversedB[i]    
    }
    
    return answer;
}