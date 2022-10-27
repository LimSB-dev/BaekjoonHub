function solution(babblings) {
    const canSpeakList = ['aya', 'ye', 'woo', 'ma']
    let answer = 0;
    
    for (let i in babblings) {
        for (const canSpeak of canSpeakList) {
            babblings[i] = babblings[i].replaceAll(canSpeak, canSpeakList.indexOf(canSpeak))
        }

        const babblingLength = babblings[i].length
        let starCount = 0
    
        for (let j = 0; j < babblings[i].length; j++) {
            if ( babblings[i][j] < 4 ) {
                if (babblings[i][j - 1] != babblings[i][j]) {
                    starCount++
                }
            } else {
                break
            }
        }
        
        console.log(babblings[i])
        if (babblingLength === starCount) {
            answer++
        }
    }
    
    return answer
}