function solution(babblings) {
    let answer = 0;
    const canSpeaks = ["aya", "ye", "woo", "ma"]
    
    for (babbling of babblings) {
        let canNotSpeak = false
        
        for (i in canSpeaks) {
            babbling = babbling.replaceAll(canSpeaks[i], i)
        }
        
        for (let i = 0; i < babbling.length; i++) {
            if (0 <= babbling[i] && babbling[i] < 4) {
            } else {
                canNotSpeak = true
                break
            }
        }
        
        if (canNotSpeak) {
            continue
        }

        if (1 < babbling.length) {
            for (let i = 0; i <= babbling.length - 2; i++) {
                if (babbling[i] === babbling[i + 1]) {
                    canNotSpeak = true
                    break
                }
            }
            
            if (!canNotSpeak) {
                answer++
            }
        } else {
            answer++
        }
    }
    return answer;
}