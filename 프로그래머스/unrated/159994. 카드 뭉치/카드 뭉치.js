function solution(cards1, cards2, goal) {
    let answer = 'Yes';
    
    for (let i = 0; i < goal.length; i++) {
        word = goal[i]
        
        if (word === cards1[0]) cards1.shift()
        else if (word === cards2[0]) cards2.shift()
        else {
            answer = 'No'
            break
        }
    }
    
    return answer;
}