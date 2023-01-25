function solution(priorities, location) {
    let answer = 1;
    const pri = priorities.map((a,i) => [a,i]);
    const stack = [];


    for(let i = 0; i < pri.length ;){
        const temp = pri.shift();
        if (pri.some((a) => temp[0] < a[0])) {
            pri.push(temp)
        } else {
            stack.push(temp);
            
            if (stack[answer - 1][1] === location) {
                break
            } else {
                answer++
            }
        }
    }

    return answer;
}