function solution(n) {
    let answer = 0
    const bin = n.toString(2)
    let stringBin = String(bin)
    
    if (stringBin.includes('0')) {
        let zero = 0
        let one = 0
        stringBin = '0' + stringBin
        
        for (let i = stringBin.length - 1; i > -1; i--) {
            if (stringBin[i] === '0') {
                zero++
                if (one >= 1) {
                    stringBin = stringBin.slice(0, i) + '10' + '0'.repeat(zero - 1) + '1'.repeat(one - 1)
                    break
                }
            } else {
                one++
            }
        }
    } else {
        stringBin = '10' + '1'.repeat(stringBin.length - 1)
    }
    
    answer = parseInt(stringBin, 2)
    
    return answer
}