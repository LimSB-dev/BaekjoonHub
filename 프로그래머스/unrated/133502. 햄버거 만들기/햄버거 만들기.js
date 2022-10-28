function solution(ingredients) {
    let answer = 0;
    const buger = [1, 2, 3, 1]
    let arr = []
    ingredients.reverse()
    
    while (ingredients.length > 0) {
        arr.push(ingredients.pop())
        if (arr.length >= 4) {
            if (arr[arr.length - 1] === 1) {
                if (arr[arr.length - 2] === 3) {
                    if (arr[arr.length - 3] === 2) {
                        if (arr[arr.length - 4] === 1) {
                            arr.pop()
                            arr.pop()
                            arr.pop()
                            arr.pop()
                            answer++
                        }
                    }
                }    
            }
        }
    }
    
    return answer
}
