/** 약관 판단 후 유효기간을 지나 파기되어야 한다면 ture 반환 */
function check(curYear, curMonth, curDay, year, month, day, value) {
    month += value
    
    if (month > 12) {
        year += Math.floor((month - 1) / 12);
        month = (month - 1) % 12 + 1;
    }

    
    if (curYear !== year) {
        return curYear > year
    }

    if (curMonth !== month) {
        return curMonth > month
    }

    return curDay >= day
}

function solution(today, terms, privacies) {
    let answer = []
    const [curYear, curMonth, curDay] = today.split('.').map(string => Number(string))
    let expiration = new Map()
    
    terms.map(term => {
        const [key, value] = term.split(' ')
        
        expiration[key] = Number(value)
    })
    
    privacies.map((privacie, idx) => {
        const [date, key] = privacie.split(' ')
        const [year, month, day] = date.split('.').map(string => Number(string))
        const value = expiration[key]
        
        // 유효기간 확인
        if (check(curYear, curMonth, curDay, year, month, day, value)) {
            answer.push(idx + 1)
        }
    })
    
    return answer
}